import { createQueue } from 'kue';

const queue = createQueue();

const job = queue.create('push_notification_code', {
  phoneNumber: '0541279486',
  message: 'Hey there',
});
job.on('enqueue', () => {
  console.log(`Notification job created: ${job.id}`);
}).on('complete', () => {
  console.log('Notification job completed');
}).on('failed attempt', () => {
  console.log('Notification job failed');
});
job.save();
