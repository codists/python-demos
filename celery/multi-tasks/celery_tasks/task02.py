import time
import datetime

from .celery import cel


@cel.task
def send_sms(name):
    print(f'{datetime.datetime.now()}： 开始向  {name} 发送短信')
    time.sleep(10)
    print('发送短信完毕')
    return '发送短信完毕'
