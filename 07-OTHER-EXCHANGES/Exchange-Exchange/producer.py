"""
we bind two exchanges together via direct then fanout 
"""

# METHOD 1


import pika



connection_parameters = pika.ConnectionParameters('localhost')
connection = pika.BlockingConnection(connection_parameters)
channel = connection.channel()

channel.exchange_declare(exchange='firstexchange', exchange_type='direct')
channel.exchange_declare(exchange='secondexchange', exchange_type='fanout')
channel.exchange_bind('secondexchange', 'firstexchange')

message = "YYYY This message has gone through multiple exchanges to consumer,from producer.py"

# direct usually needs a  specific routing_key address to bind to but here,....
# channel.basic_publish(exchange='firstexchange', routing_key='', body=message)
# channel.basic_publish(exchange='firstexchange', routing_key='green', body=message)

# channel.basic_publish(exchange='secondexchange', routing_key='', body=message)
channel.basic_publish(exchange='firstexchange', routing_key='green', body=message)

print(f"sent message: {message}")

connection.close()








# METHOD 2
# import pika



# connection_parameters = pika.ConnectionParameters('localhost')
# connection = pika.BlockingConnection(connection_parameters)
# channel = connection.channel()

# channel.exchange_declare(exchange='firstexchange', exchange_type='direct')
# channel.exchange_declare(exchange='secondexchange', exchange_type='fanout')
# channel.exchange_bind('secondexchange', 'firstexchange',routing_key='green')

# message = "This message has gone through multiple exchanges to consumer,from producer.py"

# # direct usually needs a  specific routing_key address to bind to but here,....
# # channel.basic_publish(exchange='firstexchange', routing_key='', body=message)
# # channel.basic_publish(exchange='firstexchange', routing_key='green', body=message)

# channel.basic_publish(exchange='secondexchange', routing_key='', body=message)

# print(f"sent message: {message}")

# connection.close()

# sent message: This message has gone through multiple exchanges to consumer,from producer.py





# METHOD 3


# import pika



# connection_parameters = pika.ConnectionParameters('localhost')
# connection = pika.BlockingConnection(connection_parameters)
# channel = connection.channel()

# channel.exchange_declare(exchange='firstexchange', exchange_type='direct')
# channel.exchange_declare(exchange='secondexchange', exchange_type='fanout')
# channel.exchange_bind('secondexchange', 'firstexchange')

# message = "This message has gone through multiple exchanges to consumer,from producer.py"

# # direct usually needs a  specific routing_key address to bind to but here,....
# channel.basic_publish(exchange='firstexchange', routing_key='', body=message)

# print(f"sent message: {message}")

# connection.close()