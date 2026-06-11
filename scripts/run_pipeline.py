"""
Master Execution Script

Runs data ingestion and ETL pipeline.
"""

import subprocess

print("Running Data Ingestion...")
subprocess.run(
    ["python", "scripts/data_ingestion.py"]
)

print("Running ETL Pipeline...")
subprocess.run(
    ["python", "scripts/etl_pipeline.py"]
)

print("\nPipeline Completed Successfully")
print("Run recommender.py separately if required.")