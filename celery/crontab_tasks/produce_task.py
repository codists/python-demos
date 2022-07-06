from datetime import datetime
from datetime import timedelta
from celery_task import send_email

# 方式1
v1 = datetime(2022, 7, 6, 14, 25, 0)
v2 = datetime.utcfromtimestamp(v1.timestamp())
# eta指定任务被执行的时间,要求是UTC时间


# 方式2(周期性执行)
ctime = datetime.now()
# 默认用utc时间
utc_ctime = datetime.utcfromtimestamp(ctime.timestamp())
time_delay = timedelta(seconds=60)
task_time = utc_ctime + time_delay

result = send_email.apply_async(args=('codists',), eta=task_time)
print(result.id)

