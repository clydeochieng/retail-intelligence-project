import pandas as pd
import json

print("🚀 Project is running!")

# Load CSV
df = pd.read_csv("retail_pricing_demand_100k.csv")
print("\nCSV loaded successfully")
print(df.head())

# Load JSON
with open("retail_project_config.json") as f:
    config = json.load(f)

print("\nJSON loaded successfully")
print(config)