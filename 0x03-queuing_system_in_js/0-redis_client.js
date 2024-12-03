import { createClient } from 'redis';

const client = createClient();

(async () => {
  await client.connect();
})();

client.on('ready', () => {
  console.log('Redis client connected to the server');
});
client.on('error', (err) => {
  console.log('Redis client not connected to the server: ', err);
});
