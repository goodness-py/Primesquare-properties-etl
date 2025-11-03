import os

print("Starting ETL Pipeline...")

print("\n[1/3] Extracting data...")
os.system("python src/extract.py")

print("\n[2/3] Transforming data...")
os.system("python src/transform.py")

print("\n[3/3] Loading to database...")
os.system("python src/load.py")

print("\nETL Pipeline Complete!")
