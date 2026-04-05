import kagglehub
import pandas as pd
import os

print("Downloading MIMIC-IV Sepsis Dataset...")
path = kagglehub.dataset_download("sinanshereef/mimic-iv-style-icu-dataset-for-sepsis-prediction")
print("Downloaded to:", path)

csv_files = [f for f in os.listdir(path) if f.endswith('.csv')]
if csv_files:
    # Most likely one CSV file
    file_path = os.path.join(path, csv_files[0])
    df = pd.read_csv(file_path)
    print("Columns:", df.columns.tolist())
    print("Head:\n", df.head(2))
else:
    print("No CSV found in the downloaded dataset folder.")
