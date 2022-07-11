"""
交换机模式
"""
import pika

# 1.connect to rabbitmq
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
# 2.create exchange
channel.exchange_declare(exchange='log3', exchange_type='topic')
# 3.insert message into exchange
message = 'usa news: xxxx'
channel.basic_publish(
    exchange='log3',
    routing_key='usa.weather',
    body=message
)
#
print('exchange mode: producer start')
connection.close()
