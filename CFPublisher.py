import pika
import sys
import json
import urllib.request

website = "https://jsonplaceholder.typicode.com/todos/2"

with urllib.request.urlopen(website) as url:
    msg = json.dumps(url.read().decode())

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='logs', exchange_type='fanout')

channel.basic_publish(
    exchange='logs', 
    routing_key='',
    body=msg
    )
print(json.loads(msg))
connection.close()
