from fastapi import FastAPI, HTTPException, Depends
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
from npi import npi
from sqlalchemy.orm import Session
from database import SessionLocal, engine
import models
import csv
from datetime import datetime, timezone
from io import StringIO
import schemas

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

class Operation(BaseModel):
    expression: str

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get('/')
async def root():
    return {'message': 'Test'}

@app.post('/cal', response_model=schemas.Result)
async def cal(operation: Operation, db: Session = Depends(get_db)):
    try:
        result = npi(operation.expression)
        db_operation = models.Operation(
            timestamp=datetime.now(timezone.utc),
            expression=operation.expression, 
            result=result
        )
        db.add(db_operation)
        db.commit()
        db.refresh(db_operation)
        # return result
        return db_operation
    except Exception as e:
        raise HTTPException(status_code=400, detail='Invalid Expression')


@app.get('/export/')
def export_operations(db: Session = Depends(get_db)):
    operations = db.query(models.Operation).all()

    # save in memory instead of server disk
    output = StringIO()
    writer = csv.writer(output)
    writer.writerow(['id', 'timestamp', 'expression', 'result'])

    for operation in operations:
        writer.writerow([operation.id, operation.timestamp, operation.expression, operation.result])
    
    output.seek(0)
    response = StreamingResponse(output, media_type='text/csv')
    response.headers['Content-Disposition'] = 'attachment; filename=operations.csv'
    return response

    # return {'message': 'CSV exported'}