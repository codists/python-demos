"""
查看消息队列中的任务:
1.redis基本操作：
1.1 type celery(查看celery类型)
1.2 list查询：LRANGE key start stop
"""
from redis import Redis

r = Redis(host='localhost', port=6379, db=1)

# 手动删除任务队列中的任务
# r.delete('celery')

for i in r.lrange('celery', 0, -1):
    print(i)
