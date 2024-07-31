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

// Custom callback function to print the result of hset
function printResult(err, reply) {
  if (err) {
    console.error(`Error: ${err}`);
  } else {
    console.log(`Reply: ${reply}`);
  }
}

// Function to create and store a hash
function storeHash() {
  client.hset('HolbertonSchools', 'Portland', 50, printResult);
  client.hset('HolbertonSchools', 'Seattle', 80, printResult);
  client.hset('HolbertonSchools', 'New York', 20, printResult);
  client.hset('HolbertonSchools', 'Bogota', 20, printResult);
  client.hset('HolbertonSchools', 'Cali', 40, printResult);
  client.hset('HolbertonSchools', 'Paris', 2, printResult);
}

// Function to display the hash
function displayHash() {
  client.hgetall('HolbertonSchools', (err, object) => {
    if (err) {
      console.error(`Error fetching data: ${err}`);
    } else {
      console.log(object);
    }
  });
}

// Execute the functions
storeHash();
displayHash();
