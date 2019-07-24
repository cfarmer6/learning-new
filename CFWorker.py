import pika
import json
import string
import time

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='task_queue', durable=True)

print("waiting")

def callback(ch, method, properties, body):
    print(json.loads(body))
    ch.basic_ack(delivery_tag=method.delivery_tag)

channel.basic_qos(prefetch_count=2)
channel.basic_consume(
    queue='task_queue', on_message_callback=callback)

channel.start_consuming()
