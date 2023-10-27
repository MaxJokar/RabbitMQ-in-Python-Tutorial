#  METHOD 1

import pika
def on_message_received(ch, method, properties, body):
    print(f'received new message: {body}')

connection_parameters = pika.ConnectionParameters('localhost')
connection = pika.BlockingConnection(connection_parameters)
channel = connection.channel()

channel.exchange_bind('secondexchange', 'firstexchange',routing_key='RED')

# channel.exchange_declare(exchange='secondexchange', exchange_type='fanout')
channel.exchange_declare('secondexchange','fanout')
channel.queue_declare(queue='letterbox')
channel.queue_bind('letterbox', 'secondexchange', routing_key='')


channel.basic_consume(queue='letterbox', auto_ack=True,
    on_message_callback=on_message_received)

print('Starting Consuming')

channel.start_consuming()




# METHOD 2

# import pika
# def on_message_received(ch, method, properties, body):
#     print(f'received new message: {body}')

# connection_parameters = pika.ConnectionParameters('localhost')
# connection = pika.BlockingConnection(connection_parameters)
# channel = connection.channel()

# # channel.exchange_declare(exchange='secondexchange', exchange_type='fanout')
# channel.exchange_declare('secondexchange','fanout')
# channel.queue_declare(queue='letterbox')
# channel.queue_bind('letterbox', 'secondexchange', routing_key='')


# channel.basic_consume(queue='letterbox', auto_ack=True,
#     on_message_callback=on_message_received)

# print('Starting Consuming')


# channel.start_consuming()





# Starting Consuming
# received new message: b'This message has gone through multiple exchanges to consumer,from producer.py'

#  METHOD 3

# import pika
# def on_message_received(ch, method, properties, body):
#     print(f'received new message: {body}')

# connection_parameters = pika.ConnectionParameters('localhost')
# connection = pika.BlockingConnection(connection_parameters)
# channel = connection.channel()

# channel.exchange_declare(exchange='secondexchange', exchange_type='fanout')
# channel.queue_declare(queue='letterbox')
# channel.queue_bind('letterbox', 'secondexchange')

# channel.basic_consume(queue='letterbox', auto_ack=True,
#     on_message_callback=on_message_received)

# print('Starting Consuming')

# channel.start_consuming()