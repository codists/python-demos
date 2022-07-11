# pika
- 官方文档
https://pika.readthedocs.io/en/stable/
# rabbitmq基本操作
- 官方文档

  https://rabbitmq.com/
- 安装
```shell
$ sudo apt install rabbitmq-server
```
- 启动
```shell
$ sudo rabbitmq-server
```
- 停止
```shell
$ sudo rabbitmqctl stop
```
# exchange(简单模式)
- 生产者

  连接rabbitmq > 创建队列 > 向指定的队列插入数据
- 消费者

   连接rabbitmq > 监听rabbitmq > 确定回调函数
# 参数使用

# 交换机模式
## 发布订阅
## 关键字
## 通配符