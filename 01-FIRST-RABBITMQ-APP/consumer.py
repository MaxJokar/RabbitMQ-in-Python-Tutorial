import pika

def on_message_received(ch, method, properties, body):
    print(f"received new message: {body}")

# the same connection and channel  
connection_parameters = pika.ConnectionParameters('localhost')
connection = pika.BlockingConnection(connection_parameters)

channel = connection.channel()

channel.queue_declare(queue='letterbox')
# To consume the queue , call back : when it receives the  mess do something
channel.basic_consume(queue='letterbox', auto_ack=True,
    on_message_callback=on_message_received)

print("Starting Consuming")

channel.start_consuming()