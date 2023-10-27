"""
messages that have the routing_key of  paymentsonly will be sent to this queue here
and consumed by the consumer service 
"""
import pika
from pika.exchange_type import ExchangeType

def on_message_received(ch, method, properties, body):
    print(f'Payments - received new message: {body}')

connection_parameters = pika.ConnectionParameters('localhost')
connection = pika.BlockingConnection(connection_parameters)
channel = connection.channel()
# channel.exchange_declare(exchange='routing', exchange_type=ExchangeType.direct)
channel.exchange_declare(exchange='mytopicexchange', exchange_type=ExchangeType.direct)

queue = channel.queue_declare(queue='', exclusive=True) # connection closes,queue deleted
#  add a binding key between queue and exchange:
# only mess have routing key  of paymentsonly  will be sent to this queue here 
channel.queue_bind(exchange='mytopicexchange', queue=queue.method.queue, routing_key='paymentsOnly')
channel.queue_bind(exchange='routing', queue=queue.method.queue, routing_key='both')
# the basic consum method 
channel.basic_consume(queue=queue.method.queue, auto_ack=True,
    on_message_callback=on_message_received)

print('Payments Starting Consuming')

channel.start_consuming() 


# PS C:\mydrive\DjangoProjects2023\rabitMQ\04-ROUTING> python producer.py
# sent message: a european user paid for something
# sent message: a european business order for  something
# PS C:\mydrive\DjangoProjects2023\rabitMQ\04-ROUTING> 

# Payments Starting Consuming
# Payments - received new message: b'a european user paid for something'