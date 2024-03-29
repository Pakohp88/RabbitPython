import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='temperature', exchange_type='fanout')

result = channel.queue_declare(queue='', exclusive=True)
queue_name = result.method.queue

channel.queue_bind(exchange='temperature', queue=queue_name)

print(' [*] Waiting for messages. To exit pres CTRL+C')

def callback(ch, method, properties, body):
    print("     [Station USA] Received %r" % body.decode('utf-8'))

channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)

channel.start_consuming()