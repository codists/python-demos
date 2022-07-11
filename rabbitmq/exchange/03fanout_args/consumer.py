import time

import pika

# 1.连接rabbitmq
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
# 2.监听队列（如果队列不存在就创建）
channel.queue_declare(queue='hello4')


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

print('consumer in 5s, wait for message, press Ctrl-C to exit')
# 开始监听
channel.start_consuming()
