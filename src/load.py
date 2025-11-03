import pandas as pd
from sqlalchemy import create_engine, text
from dotenv import load_dotenv
import os

load_dotenv()

# Get database credentials
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")

# Load CSV
df = pd.read_csv("data/transformed/all_properties_cleaned.csv")
print(f"Loaded {len(df)} properties from CSV")

# Connect to database
engine = create_engine(f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@127.0.0.1:5432/{DB_NAME}")

# Load to database
df.to_sql('properties', engine, if_exists='replace', index=False)
print(f"Loaded {len(df)} properties to database")

# Verify
with engine.connect() as conn:
    result = conn.execute(text("SELECT COUNT(*) FROM properties"))
    count = result.fetchone()[0]
    print(f"Verified: {count} rows in database")