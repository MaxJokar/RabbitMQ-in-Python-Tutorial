import pika
from pika.exchange_type import ExchangeType

def on_message_received(ch, method, properties, body):
    print(f'received new message: {body}')

connection_parameters = pika.ConnectionParameters('localhost')
connection = pika.BlockingConnection(connection_parameters)
channel = connection.channel()

channel.exchange_declare(exchange='headersexchange', exchange_type=ExchangeType.headers)

channel.queue_declare('letterbox')
# queue = channel.queue_declare(queue='', exclusive=True)

#  changing any to all we can see in producer:received only its own  new message: b'This message will be sent with headers'
# but nothing in consumer  because age is also needed and not just name which is provided in producer
#  solution1: we must add age in producer.py  or delete age here 
bind_args = {
  'x-match': 'all',
  'name': 'brian',
  'age': '21'
}

# argument has a role like  routing_key='user.#' or  routing_key='paymentsonly':routing key is binding key!
channel.queue_bind('letterbox', 'headersexchange', arguments=bind_args)
# channel.queue_bind(exchange='headersexchange', queue=queue.method.queue,arguments=bind_args )

channel.basic_consume(queue='letterbox', auto_ack=True,
    on_message_callback=on_message_received)

print('Starting Consuming')

channel.start_consuming()


# Starting Consuming
# received new message: b'This message from producer.py  will be sent with headers'