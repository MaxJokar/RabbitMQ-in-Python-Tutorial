"""
because of  routing_key =*.europe.* here we can get 
both messages published in producer.py  because the  europe can
have any one word as suffix and prefix  so we can get two messages 

"""
import pika
from pika.exchange_type import ExchangeType

def on_message_received(ch, method, properties, body):
    print(f'Analytics - received new message: {body}')

connection_parameters = pika.ConnectionParameters('localhost')

connection = pika.BlockingConnection(connection_parameters)

channel = connection.channel()
channel.exchange_declare(exchange='topic', exchange_type=ExchangeType.topic)
queue = channel.queue_declare(queue='', exclusive=True)

#  bind me to those ones with r_k which has  europe with one siffix and prefix 
channel.queue_bind(exchange='topic', queue=queue.method.queue, routing_key='*.europe.*')

channel.basic_consume(queue=queue.method.queue, auto_ack=True,
    on_message_callback=on_message_received)

print('Analytics Starting Consuming')

channel.start_consuming()