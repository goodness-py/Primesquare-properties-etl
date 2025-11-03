import json
import pandas as pd
import os

# Load data from JSON files
cities = ["San_Antonio", "Austin", "Houston"]
all_properties = []

for city in cities:
    file_path = f"data/raw/property_data_{city}_TX.json"
    
    with open(file_path, "r") as f:
        data = json.load(f)
    
    for prop in data:
        prop['source_city'] = city
        all_properties.append(prop)
    
    print(f"Loaded {len(data)} properties from {city}")

# Normalize and clean
df = pd.json_normalize(all_properties)

# Keep only important columns
columns_to_keep = [
    'id', 'formattedAddress', 'city', 'state', 'zipCode', 
    'latitude', 'longitude', 'propertyType', 'bedrooms', 
    'bathrooms', 'squareFootage', 'lotSize', 'yearBuilt', 'source_city'
]

df_clean = df[[col for col in columns_to_keep if col in df.columns]].copy()

# Rename columns
df_clean.columns = df_clean.columns.str.replace('formattedAddress', 'formatted_address')
df_clean.columns = df_clean.columns.str.replace('zipCode', 'zip_code')
df_clean.columns = df_clean.columns.str.replace('propertyType', 'property_type')
df_clean.columns = df_clean.columns.str.replace('squareFootage', 'square_footage')
df_clean.columns = df_clean.columns.str.replace('lotSize', 'lot_size')
df_clean.columns = df_clean.columns.str.replace('yearBuilt', 'year_built')

# Save
os.makedirs('data/transformed', exist_ok=True)
df_clean.to_csv('data/transformed/all_properties_cleaned.csv', index=False)
print(f"Saved {len(df_clean)} properties to CSV")