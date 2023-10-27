"""
competing consumers (work queue)
prefetch value:gives only one message when worker is busy 

"""
import pika
import time
import random

def on_message_received(ch, method, properties, body):
    processing_time = random.randint(1, 6)
    print(f'received: "{body}", will take {processing_time}SECOND to process')
    time.sleep(processing_time)
    ch.basic_ack(delivery_tag=method.delivery_tag)
    print(f'finished processing and acknowledged message')

# connect and  create a channel, declare queue
connection_parameters = pika.ConnectionParameters('localhost')
connection = pika.BlockingConnection(connection_parameters)
channel = connection.channel()
channel.queue_declare(queue='letterbox')
#  give only one message when  worker is busy 
#  broker waits until a consumer  finish processing prev before sending another
channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue='letterbox', on_message_callback=on_message_received)

print('Starting Consuming')

channel.start_consuming()