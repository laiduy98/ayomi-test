from sqlalchemy import Column, Integer, String, Float, DateTime
from database import Base
import datetime

class Operation(Base):
    __tablename__ = 'list_operations'

    id = Column(Integer, primary_key=True, index=True)
    timestamp = Column(DateTime, default=datetime.datetime.now(datetime.UTC))
    expression = Column(String, index=True)
    result = Column(Float)