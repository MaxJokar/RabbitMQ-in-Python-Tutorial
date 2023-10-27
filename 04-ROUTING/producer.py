"""
direct exchange binds to its direct queue without any suffix or prefix unlike in topic !
that is the difference between routing and  topic .
the concepts of  Routing  with 2 different consumers which they can get message
based on their routing_key determined ,using the one consumer menationed its name 
or  using the word  both  we can have both consumer simeltaneuosly in RabbitMQ
and direct which is bind to the queue 

in rabbitMQ to smartlys end messages to different consumers in our system 

from producer we have a message which is sent to its relevant queue 

"""
import pika
from pika.exchange_type import ExchangeType

connection_parameters = pika.ConnectionParameters('localhost')
connection = pika.BlockingConnection(connection_parameters)

channel = connection.channel()
channel.exchange_declare(exchange='routing', exchange_type=ExchangeType.direct)

message = 'This message Routing FROM  producer.py'

# binds producer to analyticsonly  using  routing_key 'analyticsonly'
# channel.basic_publish(exchange='routing', routing_key='analyticsonly', body=message)

# we can have two consumers using 'both' word :analyticsconsumer and paymentconsumer(direct)
channel.basic_publish(exchange='routing', routing_key='both', body=message)


print(f'sent message: {message}')

connection.close()


# sent message: This message needs to be routed
# sent message: This message Routing FROM  producer.py
 