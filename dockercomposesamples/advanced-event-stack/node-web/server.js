const express = require('express');
const amqp = require('amqplib');

const app = express();
const PORT = process.env.PORT || 3000;
const RABBITMQ_URL = process.env.RABBITMQ_URL || 'amqp://guest:guest@localhost:5672';

async function publishMessage(msg) {
  try {
    const connection = await amqp.connect(RABBITMQ_URL);
    const channel = await connection.createChannel();
    const queue = 'task_queue';
    
    await channel.assertQueue(queue, { durable: true });
    channel.sendToQueue(queue, Buffer.from(msg), { persistent: true });
    
    await channel.close();
    await connection.close();
  } catch (error) {
    console.error('Error publishing to RabbitMQ:', error);
  }
}

app.get('/', async (req, res) => {
  const taskMessage = `Event triggered at ${new Date().toISOString()}`;
  await publishMessage(taskMessage);
  
  res.send(`Request handled by Node container ID: <b>${process.env.HOSTNAME}</b>. Event pushed to RabbitMQ!`);
});

app.listen(PORT, () => {
  console.log(`Web app running on port ${PORT}`);
});