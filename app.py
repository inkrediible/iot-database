from flask import Flask, jsonify #this file is only checking if website is taking test data 
from flask_cors import CORS
from pymongo import MongoClient
from bson import ObjectId
from datetime import datetime
import pytz

app = Flask(__name__)
CORS(app)

# MongoDB connection
client = MongoClient("mongodb://localhost:27017/")  # Update if on different port
db = client["iot_db"]  # Replace with your DB name
collection = db["sensor_data"]  # Replace with your collection name

# timestamp to ist yay
def convert(doc):
    ist = pytz.timezone('Asia/Kolkata')
    return {
        "id": str(doc["_id"]),
        "soil_moisture": doc["soil_moisture"],
        "temperature": doc["temperature"],
        "humidity": doc["humidity"],
        "rain_detected": doc["rain_detected"],
        "water_flow": doc["water_flow"],
        "pump_status": doc["pump_status"],
        "timestamp": doc["timestamp"].astimezone(ist).isoformat()
    }

@app.route("/api/all", methods=["GET"])
def get_all_data():
    data = list(collection.find().sort("timestamp", -1).limit(50))  # Get last 50 entries
    return jsonify([convert(doc) for doc in data])

if __name__ == "__main__":
    app.run(debug=True)
