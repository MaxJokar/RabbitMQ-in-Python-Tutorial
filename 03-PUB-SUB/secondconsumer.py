"""
whenever we  publisha message , it  recives at the same time to the  
queues  , due to  fanout exchange:sends at the same time to any queue 
without any consideration 
"""
import pika

def on_message_received(ch, method, properties, body):
    print(f"second consumer - received new message: {body}")

connection_parameters = pika.ConnectionParameters('localhost')
connection = pika.BlockingConnection(connection_parameters)

channel = connection.channel()

channel.exchange_declare(exchange='pubsub', exchange_type='fanout')

queue = channel.queue_declare(queue='', exclusive=True)

channel.queue_bind(exchange='pubsub', queue=queue.method.queue)

channel.basic_consume(queue=queue.method.queue, auto_ack=True,
    on_message_callback=on_message_received)

print("Starting Consuming")

channel.start_consuming()


# Output:
# Starting Consuming
# first consumer - received new message: b'Hello I want to broadcast this message'
# first consumer - received new message: b'Hello I want to broadcast this message'
# first consumer - received new message: b'Hello I want to broadcast this message'
# first consumer - received new message: b'Hello I want to broadcast this message'