"""
因为任务是异步执行的，无法直接获取结果，所以结果要从result backend获取——本模块用于获取任务执行的结果
"""
from celery.result import AsyncResult
from tasks import app1

async_result = AsyncResult(id="347e0bbe-6071-40f6-876d-6a3c8c5c07d6", app=app1)
if async_result.successful():
    result = async_result.get()
    print('成功')
elif async_result.failed():
    print('失败')
elif async_result.status == 'START':
    print('开始')
elif async_result.status == 'PENDING':
    print('执行中')
elif async_result.status == 'RETRY':
    print('重试')