import os
import time
import pika

rabbitmq_url = os.environ.get('RABBITMQ_URL', 'amqp://guest:guest@localhost:5672')

def callback(ch, method, properties, body):
    print(f" [x] Received event: {body.decode()}")
    time.sleep(1) # Simulate background processing delay
    print(" [x] Task processed and acknowledged successfully!")
    ch.basic_ack(delivery_tag=method.delivery_tag)

def main():
    print(f"Connecting to RabbitMQ broker at {rabbitmq_url}...")
    while True:
        try:
            params = pika.URLParameters(rabbitmq_url)
            connection = pika.BlockingConnection(params)
            channel = connection.channel()
            
            channel.queue_declare(queue='task_queue', durable=True)
            channel.basic_qos(prefetch_count=1)
            channel.basic_consume(queue='task_queue', on_message_callback=callback)
            
            print(' [*] Waiting for messages. To exit press CTRL+C')
            channel.start_consuming()
        except Exception as e:
            print(f"Connection failed ({e}), retrying in 5 seconds...")
            time.sleep(5)

if __name__ == '__main__':
    main()