from pydantic import BaseModel
from datetime import datetime

class Result(BaseModel):
    id: int
    timestamp: datetime
    expression: str
    result: float

    class Config:
        orm_mode = True