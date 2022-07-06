from celery.result import AsyncResult
from celery_tasks.celery import cel

async_result = AsyncResult(id='3765fa47-c723-4a0a-bee6-89321c20c05c', app=cel)

if async_result.successful():
    print('成功')
elif async_result.failed():
    print('失败')

elif async_result.status == 'START':
    print('开始')
elif async_result.status == 'PENDING':
    print('执行中')
elif async_result.status == 'RETRY':
    print('重试')

