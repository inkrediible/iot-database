const mongoose = require("mongoose");

const sensorSchema = new mongoose.Schema({
  soil_moisture: Number,
  temperature: Number,
  humidity: Number,
  rain_detected: String,
  water_flow: Number,
  pump_status: String,
  timestamp: {
    type: Date,
    default: () => {
      const istOffset = 5.5 * 60 * 60 * 1000; // IST 
      return new Date(Date.now() + istOffset);
    },
  },
});

const Sensor = mongoose.model("Sensor", sensorSchema, "sensor_data"); // Collection name: "sensor_data"

module.exports = Sensor;
