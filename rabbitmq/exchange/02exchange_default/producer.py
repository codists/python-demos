"""
交换机模式
"""
import pika

# 1.connect to rabbitmq
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
# 2.create exchange
channel.exchange_declare(exchange='logs', exchange_type='fanout')
# 3.insert message into exchange
message = 'in exchange mode'
channel.basic_publish(
    exchange='logs',
    routing_key='',
    body=message
)
#
print('exchange mode: producer start')
connection.close()
