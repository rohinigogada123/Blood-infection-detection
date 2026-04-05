from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class PatientHistory(Base):
    __tablename__ = "patient_history"
    id = Column(Integer, primary_key=True, index=True)
    patient_name = Column(String, index=True)
    age = Column(Integer)
    temperature = Column(Float)
    heart_rate = Column(Float)
    wbc = Column(Float)
    platelets = Column(Float)
    result = Column(String)
    probability = Column(Float)
    timestamp = Column(DateTime, default=datetime.utcnow)
