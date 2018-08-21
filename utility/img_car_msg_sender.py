# -*- coding: utf-8 -*-
import pika
from entity.car import ImgCar
from utility.img_file import *
from repository.img_car_repository import *

def img_car_msg_sender():
    username = 'guest'  # 指定远程rabbitmq的用户名密码
    pwd = 'guest'
    user_pwd = pika.PlainCredentials(username, pwd)
    s_conn = pika.BlockingConnection(pika.ConnectionParameters('127.0.0.1', credentials=user_pwd))  # 创建连接
    chan = s_conn.channel()  # 在连接上创建一个频道
    chan.queue_declare(queue='hello')  # 声明一个队列，生产者和消费者都要声明一个相同的队列，用来防止万一某一方挂了，另一方能正常运行
    chan.basic_publish(exchange='', routing_key = 'hello', body = 'test 4')  # 生产者要发送的消息
    print("[生产者] send 'hello world")
    s_conn.close()  # 当生产者发送完消息后，可选择关闭连接

img_car_msg_sender()

