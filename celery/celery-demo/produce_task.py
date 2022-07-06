"""
本模块用于calling task
"""
from tasks import send_email

result = send_email.delay('codists')
print(result.id)
