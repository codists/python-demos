import time
import datetime

from .celery import cel


@cel.task
def send_email(name):
    print(f'{datetime.datetime.now()}： 开始向  {name} 发送邮件')
    time.sleep(10)
    print('发送邮件完毕')
    return f'{name}, 发送邮件完毕'
