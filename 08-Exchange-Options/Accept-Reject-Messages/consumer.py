import pika
from pika.exchange_type import ExchangeType

#  we wanna decide if we wanna acknowledge or reject
def on_message_received(ch, method, properties, body):
    # for every 5th message we acknowledge that message
    if (method.delivery_tag % 5 == 0):
        # every message will be acknowledge straight a way 
        # ch.basic_ack(delivery_tag=method.delivery_tag, multiple=True)
        ch.basic_nack(delivery_tag=method.delivery_tag, requeue=False, multiple=True)

    #ch.basic_reject(delivery_tag=method.delivery_tag, requeue=False)

    print(f'Received new message: {method.delivery_tag}')

connection_parameters = pika.ConnectionParameters('localhost')
connection = pika.BlockingConnection(connection_parameters)
channel = connection.channel()

channel.exchange_declare(
    exchange='acceptrejectexchange', 
    exchange_type=ExchangeType.fanout)

channel.queue_declare(queue='letterbox')
channel.queue_bind('letterbox', 'acceptrejectexchange')

channel.basic_consume(queue='letterbox', on_message_callback=on_message_received)

print('Starting Consuming')

channel.start_consuming()