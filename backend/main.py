from fastapi import FastAPI, Depends, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy import create_engine
from pydantic import BaseModel
import models
from ml_model import MLModelManager

engine = create_engine("sqlite:///./sql_app.db", connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Blood Infection Predictor API")
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_credentials=True, allow_methods=["*"], allow_headers=["*"])

ml_manager = MLModelManager()

class PredictionRequest(BaseModel):
    patient_name: str
    age: int
    Temperature: float
    Heart_Rate: float
    Blood_Pressure: float
    WBC_Count: float
    Platelets: float
    Hemoglobin: float
    SpO2: float
    model_type: str = "Random Forest"

class SaveRequest(BaseModel):
    patient_name: str
    age: int
    temperature: float
    heart_rate: float
    wbc: float
    platelets: float
    result: str
    probability: float

def get_db():
    db = SessionLocal()
    try: yield db
    finally: db.close()

@app.post("/api/predict")
def predict(request: PredictionRequest, db: Session = Depends(get_db)):
    features = {
        'Temperature_C': request.Temperature,
        'Heart_Rate_bpm': request.Heart_Rate,
        'WBC_count': request.WBC_Count,
        'Platelet_Count': request.Platelets,
        'Hemoglobin_g_dL': request.Hemoglobin,
        'Systolic_BP_mmHg': request.Blood_Pressure,
        'SpO2_percent': request.SpO2
    }
    prob, pred = ml_manager.predict(request.model_type, features)
    result_str = "Infected" if pred == 1 else "Healthy"
    
    new_record = models.PatientHistory(
        patient_name=request.patient_name,
        age=request.age,
        temperature=request.Temperature,
        heart_rate=request.Heart_Rate,
        wbc=request.WBC_Count,
        platelets=request.Platelets,
        result=result_str,
        probability=prob
    )
    db.add(new_record)
    db.commit()
    db.refresh(new_record)
    
    return {
        "prediction": result_str,
        "probability": prob,
        "record_id": new_record.id,
        "accuracies": ml_manager.get_model_accuracies()
    }

@app.post("/api/save")
def manual_save(request: SaveRequest, db: Session = Depends(get_db)):
    rec = models.PatientHistory(**request.dict())
    db.add(rec)
    db.commit()
    return {"status": "saved"}

@app.get("/api/history")
def get_history(db: Session = Depends(get_db)):
    return db.query(models.PatientHistory).order_by(models.PatientHistory.timestamp.desc()).all()

@app.get("/api/search")
def search_patient(name: str = Query(""), db: Session = Depends(get_db)):
    if not name:
        return get_history(db)
    return db.query(models.PatientHistory).filter(models.PatientHistory.patient_name.ilike(f"%{name}%")).order_by(models.PatientHistory.timestamp.desc()).all()

@app.delete("/api/history/{record_id}")
def delete_record(record_id: int, db: Session = Depends(get_db)):
    record = db.query(models.PatientHistory).filter(models.PatientHistory.id == record_id).first()
    if not record:
        raise HTTPException(status_code=404, detail="Record not found")
    db.delete(record)
    db.commit()
    return {"status": "deleted"}

@app.get("/api/feature-importance")
def get_importance():
    return ml_manager.get_feature_importance()
