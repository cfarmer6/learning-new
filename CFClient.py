import pika
import sys
import json
import urllib.request

website = "https://jsonplaceholder.typicode.com/todos/1"

with urllib.request.urlopen(website) as url:
    msg = json.dumps(url.read().decode())

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='task_queue', durable = True)

channel.basic_publish(
    exchange='',
    routing_key='task_queue', 
    body=msg,
    properties = pika.BasicProperties(
        delivery_mode = 2,
    ))
print(json.loads(msg))
connection.close()
