import pika

#  create a connection to  running locally running rbMQ
connection_parameters = pika.ConnectionParameters('localhost')
connection = pika.BlockingConnection(connection_parameters)
#  we interact with channels and not directly to connections(many dif channels  ) 
channel = connection.channel()
# to see how we can use above to send a mess onto the broker following
channel.queue_declare(queue='letterbox')



message = "Hello this is my first message from producer.py"

channel.basic_publish(exchange='', routing_key='letterbox', body=message)

print(f"sent message: {message}")

connection.close()