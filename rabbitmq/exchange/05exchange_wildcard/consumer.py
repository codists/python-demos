import time

import pika

# 1.连接rabbitmq
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# 2.创建交换机和队列，用队列去绑定交换机
channel.exchange_declare(exchange='log3', exchange_type='topic', )
result = channel.queue_declare('', exclusive=True)
queue_name = result.method.queue
print(queue_name)

channel.queue_bind(
    queue=queue_name,
    exchange='log3',
    routing_key='#.weather'
)


# 3.回调函数
def callback(ch, method, propertices, body):
    print(f'{body} Received')
    time.sleep(5)


# 优先发给空闲的消费者
channel.basic_qos(prefetch_count=1)

# 4.确定监听队列参数
channel.basic_consume(
    queue='hello4',
    auto_ack=True,  # 默认应答
    on_message_callback=callback
)

print('#.weather: ')
# 开始监听
channel.start_consuming()
