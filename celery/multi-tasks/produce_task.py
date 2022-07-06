from celery_tasks.task01 import send_email

result = send_email.delay('codists')
print(result.id)
