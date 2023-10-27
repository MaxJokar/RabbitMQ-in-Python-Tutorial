import pika







connection_parameters = pika.ConnectionParameters('localhost')
connection = pika.BlockingConnection(connection_parameters)
channel = connection.channel()
# can be without "exchange= " or "exchange_type=" manually, this way ONLY :'x-consistent-hash'
channel.exchange_declare('samplehashing','x-consistent-hash' )

message = 'The routing key is Hashed  from produce.py !'

#  in consumer.py  by choosing the amount of r_K 
# routing_key => for examle:routing_key='1'  OR  routing_key='4' we  we get 3/4 or 1/4 of  a  message 



# Changing  routing_key_to_hash = 'hksdf uu656545hash me!' we can get 1st message 
# routing_key_to_hash = 'hash me!'
routing_key_to_hash = 'HHERhrt1454 m!'

# routing_key_to_hash = '1234'




# routing_key: is what we want to hash on 
channel.basic_publish(exchange='samplehashing', routing_key=routing_key_to_hash, body=message)

print(f'sent message: {message}')

connection.close()

# sent message: The routing key is Hashed  from produce.py !
