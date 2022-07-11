import pika

# 1. connect to rabbitmq
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
# 2.创建交换机
channel.exchange_declare(
    exchange='logs',
    exchange_type='fanout'
)
# 3.创建队列
result = channel.queue_declare('', exclusive=True)
queue_name = result.method.queue
print(queue_name)
# 4.将交换机和队列进行绑定
channel.queue_bind(queue=queue_name, exchange='logs')


# 5.创建回调函数
def callback(ch,method, properties, body):
    print(f'message is: {body}')


# 6.监听队列
channel.basic_consume(
    queue=queue_name,
    auto_ack=True,
    on_message_callback=callback
)
channel.start_consuming()
