import pika
from pika.exchange_type import ExchangeType

connection_parameters = pika.ConnectionParameters('localhost')

connection = pika.BlockingConnection(connection_parameters)

channel = connection.channel()

# Enables Publish Confitms
channel.confirm_delivery()

# Enables Transactions
channel.tx_select()


channel.exchange_declare(exchange='pubsub', exchange_type=ExchangeType.fanout)

# Creates a durable queue thta survives restarts 
channel.queue_declare("Test", durable=True)



message = 'This message is broadcating'

channel.basic_publish(
    exchange='pubsub', 
    routing_key='', 
    body=message, 
    properties=pika.BasicProperties(headers={'name': 'brian'},
        delivery_mode=1,
        expiration=13434343,
        content_type="application/json"),
    body = message,
    mandatory=True)  # we want to receive a notification of failure

# commit a transaction 
channel.tx_commit()

# rollback a transaction 
channel.tx_rollback()

print(f'sent message: {message}')

connection.close()