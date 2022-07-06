# python-demos
# celery基本用法
 - 安装
```python
$ pip install Celery
```
 - 启动
   - 方法1
    ```python
    $ celery -A tasks worker
    ```
   - 方法2(dameon)
    ```python
    
    ```
注：tasks为celery application instance所在的模块名。
- 调用任务
   - 以命令行的方式
    ```python
    $ python
    >>> from tasks import add    # close and reopen to get updated 'app'
    >>> result = add.delay(4, 4)
    ```
   - 以模块的方式
    ```python
        from tasks import send_email
        send_email.delay('codists')
    ```
- 停止
```python
Ctrl+C
```
# redis中查看celery存储的值
```shell
$ redis-cli
127.0.0.1:6379> keys *
1) "celery-task-meta-347e0bbe-6071-40f6-876d-6a3c8c5c07d6"

```