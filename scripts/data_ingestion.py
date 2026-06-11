from pathlib import Path
import pandas as pd
"""
Data Ingestion Module.

Loads raw mutual fund datasets and performs
basic validation checks.
"""
DATA_PATH = Path("../data/raw")

csv_files = list(DATA_PATH.glob("*.csv"))

print(f"Total CSV Files Found: {len(csv_files)}")

for file in csv_files:
    print("\n" + "="*80)
    print(f"FILE: {file.name}")

    try:
        df = pd.read_csv(file)

        print("\nShape:")
        print(df.shape)

        print("\nColumns:")
        print(df.columns.tolist())

        print("\nData Types:")
        print(df.dtypes)

        print("\nFirst 5 Rows:")
        print(df.head())

        print("\nMissing Values:")
        print(df.isnull().sum())

        print("\nDuplicate Rows:")
        print(df.duplicated().sum())

    except Exception as e:
        print(f"Error reading {file.name}: {e}")