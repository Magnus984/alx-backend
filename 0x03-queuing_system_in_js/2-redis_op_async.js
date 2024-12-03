import { createClient, print } from 'redis';
import { promisify } from 'util';

const client = createClient();

client.on('connect', () => {
  console.log('Redis client connected to the server');
});
client.on('error', (err) => {
  console.log('Redis client not connected to the server:', err.toString());
});

const setNewSchool = (schoolName, value) => {
  client.SET(schoolName, value, print);
};

const getAsync = promisify(client.GET).bind(client);

const displaySchoolValue = async (schoolName) => {
  const reply = await getAsync(schoolName);
  console.log(reply);
};

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
