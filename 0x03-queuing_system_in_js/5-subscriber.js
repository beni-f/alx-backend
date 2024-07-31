import { createClient } from 'redis';

// Create a Redis client
const client = createClient();

// Handle connection success
client.on('connect', () => {
  console.log('Redis client connected to the server');
});

// Handle connection errors
client.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err.message}`);
});

// Subscribe to the channel
client.subscribe('holberton school channel');

// Handle incoming messages
client.on('message', (channel, message) => {
  console.log(`Received message: ${message}`);
  if (message === 'KILL_SERVER') {
    client.unsubscribe('holberton school channel');
    client.quit();
  }
});
