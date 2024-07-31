// 0-redis_client.js

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
