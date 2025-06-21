import pymongo
from datetime import datetime
import pytz
import re

# Connect to MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["iot_db"]
collection = db["sensor_data"]

# File to read from
filename = "sensor_log (7).txt"

def parse_line(line):
    # Match line like: | 7/4/2025, 3:31:18 pm | 29.5°C | 40.5% | 63% | No | 0.00 | OFF |
    parts = [p.strip() for p in line.split("|") if p.strip()]
    if len(parts) != 7:
        return None

    try:
        # Parse timestamp as-is without any conversion
        timestamp_str = parts[0].strip()  # Keep the timestamp as-is (string)

        # Convert to datetime object to store in MongoDB
        timestamp = datetime.strptime(timestamp_str, "%m/%d/%Y, %I:%M:%S %p")

        return {
            "timestamp": timestamp,  # Store timestamp directly
            "temperature": float(parts[1].replace("°C", "")),
            "humidity": float(parts[2].replace("%", "")),
            "soil_moisture": int(parts[3].replace("%", "")),
            "rain_detected": parts[4],
            "water_flow": float(parts[5]),
            "pump_status": parts[6]
        }
    except Exception as e:
        print(f"❌ Error parsing line: {line.strip()} - {e}")
        return None

# Read and parse file
entries = []
with open(filename, "r", encoding="utf-8") as file:
    for line in file:
        if re.match(r"^\|", line):  # Only process lines that start with '|'
            data = parse_line(line)
            if data:
                entries.append(data)

# Bulk insert into MongoDB
if entries:
    collection.insert_many(entries)
    print(f"✅ Inserted {len(entries)} entries into MongoDB!")
else:
    print("❌ No valid data found.")

# Fetching and displaying the data (timestamps will be as-is)
for entry in collection.find():  # No limit, fetch all entries
    print(f"Timestamp: {entry['timestamp']}")
    print(entry)
