import { createClient, print } from 'redis';

const client = createClient();

client.on('error', (err) => {
  console.log('Redis client not connected to the server:', err.toString());
});

const setHash = (hashName, fieldName, fieldValue) => {
  client.hset(hashName, fieldName, fieldValue, print);
};

const getHashAll = (hashName) => {
  client.hgetall(hashName, (_err, reply) => {
    console.log(reply);
  });
};

function run() {
  const hashObject = {
    Portland: 50,
    Seattle: 80,
    'New York': 20,
    Bogota: 20,
    Cali: 40,
    Paris: 2,
  };
  for (const [field, value] of Object.entries(hashObject)) {
    setHash('HolbertonSchools', field, value);
  }
  getHashAll('HolbertonSchools');
}

client.on('connect', () => {
  console.log('Redis client connected to the server');
  run();
});
