import pika
import time
import random

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))

channel = connection.channel()

channel.exchange_declare(exchange='temperature', exchange_type='fanout')

for i in range(1,10):
    time.sleep(3)
    message = "Station 2 - " + str(random.randint(0, 40)) + " °C"
    channel.basic_publish(exchange='temperature', routing_key='', body=message)
    print("Published Message")

connection.close()