import time
import datetime

from celery import Celery

# Celry() 如果没有配置broker，那么默认使用rabbitmq，amqp://guest:**@localhost:5672//。如果没有安装rabbitmq，那么就报错
# app1 = Celery()

# Python中使用redis，需要安装redis库
app1 = Celery(backend='redis://localhost')


@app1.task
def send_email(name):
    print(f'{datetime.datetime.now()}： 开始向  {name} 发送邮件')
    time.sleep(10)
    print('发送邮件完毕')
    return 'Hello World'


@app1.task
def send_sms(name):
    print(f'{datetime.datetime.now()}： 开始向  {name} 发送短信')
    time.sleep(10)
    print('发送短信完毕')
    return 'Hello World'
