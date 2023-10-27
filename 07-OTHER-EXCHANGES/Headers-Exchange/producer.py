import pika
from pika.exchange_type import ExchangeType




connection_parameters = pika.ConnectionParameters('localhost')
connection = pika.BlockingConnection(connection_parameters)
channel = connection.channel()

channel.exchange_declare('headersexchange', ExchangeType.headers)

message = 'This message from producer.py  will be sent with headers'








#  bind to that queue which includes  the  argument in our header match 
channel.basic_publish(exchange='headersexchange', routing_key='', body=message, 
                    properties=pika.BasicProperties(headers={'name': 'brian'}))

print(f'sent message: {message}')

connection.close()

# sent message: This message from producer.py  will be sent with headers