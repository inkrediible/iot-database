const connectDB = require("./db");
const { saveSensorData, getAllSensorData, getLatestSensorData } = require("./sensorservice");

const runTests = async () => {
  await connectDB(); // Connect to MongoDB

  // Dummy data for testing
  const testData = {
    soil_moisture: 100,
    temperature: 45,
    humidity: 79,
    rain_detected: "YES",
    water_flow: 7.5,
    pump_status: "ON",
  };

  // Save test data
  await saveSensorData(testData);

  // Fetch all data
  const allData = await getAllSensorData();
  console.log("📌 All Sensor Data:", allData);

  // Fetch latest data
  const latestData = await getLatestSensorData();
  console.log("📌 Latest Sensor Data:", latestData);
};

runTests();

