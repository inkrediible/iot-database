const Sensor = require("./sensormodel");

// Save sensor data
const saveSensorData = async (data) => {
  try {
    const sensorEntry = new Sensor(data);
    await sensorEntry.save();
    console.log("✅ Sensor Data Saved");
  } catch (error) {
    console.error("❌ Error Saving Sensor Data:", error);
  }
};

// Get all sensor data
const getAllSensorData = async () => {
  try {
    const data = await Sensor.find().sort({ timestamp: -1 }); // Latest first
    return data;
  } catch (error) {
    console.error("❌ Error Fetching Data:", error);
  }
};

// Get the latest sensor data
const getLatestSensorData = async () => {
  try {
    const latestData = await Sensor.findOne().sort({ timestamp: -1 }); // Get the most recent entry
    return latestData;
  } catch (error) {
    console.error("❌ Error Fetching Latest Data:", error);
  }
};

module.exports = { saveSensorData, getAllSensorData, getLatestSensorData };
