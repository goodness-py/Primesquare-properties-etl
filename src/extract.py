import requests
import json
import os
from config import API_KEY, BASE_URL

# Step 1: Define the extraction function
def extract_properties(city="San Antonio", state="TX"):
    headers = {
        'accept': 'application/json',
        'x-Api-key': API_KEY,
    }
    params = {
        'city': city,
        'state': state,
    }
    
    print(f"Extracting property data for {city}, {state}")
    response = requests.get(BASE_URL, headers=headers, params=params)
    
    if response.status_code == 200:
        data = response.json()
        print(f"✓ Found {len(data)} properties in {city}")
        return data
    else:
        print(f"✗ Error {response.status_code} - {response.text}")
        return None

# Step 2: I defined the three cities i want to extract data for
cities = [
    {"city": "San Antonio", "state": "TX"},
    {"city": "Austin", "state": "TX"},
    {"city": "Houston", "state": "TX"}
]

# Step 3: Create directory if it doesn't exist
os.makedirs('data/raw', exist_ok=True)

# Step 4: Extract and save each city separately using a loop
for location in cities:
    city = location["city"]
    state = location["state"]
    
    # Extract data
    data = extract_properties(city=city, state=state)
    
    if data:
        # Create filename (replace spaces with underscores)
        file_name = f"data/raw/property_data_{city.replace(' ', '_')}_{state}.json"
        
        # Save to separate file
        with open(file_name, 'w') as f:
            json.dump(data, f, indent=2)
        
        print(f"✓ Saved {len(data)} properties to {file_name}\n")
    else:
        print(f"✗ Failed to extract data for {city}, {state}\n")

print("="*50)
print("Extraction complete! Files created:")
print("  - data/raw/property_data_San_Antonio_TX.json")
print("  - data/raw/property_data_Austin_TX.json")
print("  - data/raw/property_data_Houston_TX.json")