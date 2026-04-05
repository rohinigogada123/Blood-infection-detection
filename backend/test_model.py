import sys
import os
from ml_model import MLModelManager

print("Initializing ML Manager...")
ml_manager = MLModelManager()

# Exact Case 1 from spec
case_1_healthy = {
    'Temperature_C': 36.8, 'Heart_Rate_bpm': 72, 'WBC_count': 7000, 
    'Platelet_Count': 250000, 'Hemoglobin_g_dL': 14.5, 'Systolic_BP_mmHg': 120, 'SpO2_percent': 98
}

print("\nExecuting Test Case 1 (Healthy):")
prob, pred = ml_manager.predict("Random Forest", case_1_healthy)
res = "Infection" if pred == 1 else "Healthy"
print(f"CASE 1 RESULT: {res} | Probability: {prob:.4f}")

# Exact Case 2 from spec
case_2_critical = {
    'Temperature_C': 39.5, 'Heart_Rate_bpm': 120, 'WBC_count': 16000, 
    'Platelet_Count': 100000, 'Hemoglobin_g_dL': 10, 'Systolic_BP_mmHg': 90, 'SpO2_percent': 90
}

print("\nExecuting Test Case 2 (Critical):")
prob, pred = ml_manager.predict("Random Forest", case_2_critical)
res = "Infection" if pred == 1 else "Healthy"
print(f"CASE 2 RESULT: {res} | Probability: {prob:.4f}\n")

