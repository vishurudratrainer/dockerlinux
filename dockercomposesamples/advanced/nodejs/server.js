const express = require('express');
const mongoose = require('mongoose');

const app = express();
const PORT = 3000;
const MONGO_URI = process.env.MONGO_URI || 'mongodb://localhost:27017/testdb';

// Connect to MongoDB using the service name defined in docker-compose.yml
mongoose.connect(MONGO_URI)
  .then(() => console.log(' Connected to MongoDB successfully!'))
  .catch(err => console.error(' MongoDB connection error:', err));

app.get('/', (req, res) => {
  res.send('Hello from Node.js running inside Docker Compose connected to MongoDB!');
});

app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});