const mongoose = require("mongoose");

const sensorSchema = new mongoose.Schema({
  soil_moisture: Number,
  temperature: Number,
  humidity: Number,
  rain_detected: String,
  water_flow: Number,
  pump_status: String,
  timestamp: { type: Date, default: Date.now },
});

const Sensor = mongoose.model("Sensor", sensorSchema, "sensor_data"); // Collection name: "sensors"

module.exports = Sensor;
