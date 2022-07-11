import pika

# 1.连接rabbitmq
connection = pika.BlockingConnection(pika.ConnectionParameters('127.0.0.1'))
channel = connection.channel()

# 2.创建队列(需为队列指定名称)
channel.queue_declare(queue='hello4')

# 3.向队列插入数据
channel.basic_publish(
    exchange='',  # 简单模式
    routing_key='hello4',  # 指定队列
    body='Hello World'  # 指定数据
)

print('in producer.py')
