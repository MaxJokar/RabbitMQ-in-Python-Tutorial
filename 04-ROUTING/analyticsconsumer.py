"""
routing_key='*.europe.*'  is the keyword for the routing the messages 
here we can only get one word as prefix and europe then one word as suffix  after the europe word 

"""
import pika
from pika.exchange_type import ExchangeType

def on_message_received(ch, method, properties, body):
    print(f'Analytics - received new message: {body}')

connection_parameters = pika.ConnectionParameters('localhost')
connection = pika.BlockingConnection(connection_parameters)

channel = connection.channel()
channel.exchange_declare(exchange='routing', exchange_type=ExchangeType.direct)
# channel.exchange_declare(exchange='mytopicexchange', exchange_type=ExchangeType.topic)

queue = channel.queue_declare(queue='', exclusive=True)


#  from routing to mytopicexchange
# channel.queue_bind(exchange='mytopicexchange', queue=queue.method.queue, routing_key='*.europe.*')

#  both analyticscunsumer and paymentconsumer should take the message /when we have only two files
channel.queue_bind(exchange='routing', queue=queue.method.queue, routing_key='analyticsonly')
#  we can have both analyticsonnly and paymentconsumer as well 
channel.queue_bind(exchange='routing', queue=queue.method.queue, routing_key='both')

channel.basic_consume(queue=queue.method.queue, auto_ack=True,
    on_message_callback=on_message_received)


print('Analytics Starting Consuming')

channel.start_consuming()

# Analytics Starting Consuming
# Analytics - received new message: b'This message Routing FROM  producer.py'












