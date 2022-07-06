# 任务注册
```python

```

# 多任务目录结构
- 启动
    - 用application所在的包名启动
    ```python
    项目目录结构：
    multi-tasks
    ├── celery_tasks
    │   ├── celery.py
    │   ├── __init__.py
    │   ├── __pycache__
    │   ├── task01.py
    │   └── task02.py
    └── README.md
    
    ```

​        启动

```
multi-tasks$ celery -A celery_tasks worker --loglevel=INFO
```



