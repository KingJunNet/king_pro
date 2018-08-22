# -*- coding: utf-8 -*-
import pika
import core.rabbitmq
from core.rabbitmq import MsgQueueServiceConfig
from entity.car import ImgCar
from utility.img_file import *
from repository.img_car_repository import *

class ImgCarMsgSender:
    """
                    图片福利消息发送器
                        """
    def __init__(self):
        self.__msg_queue_service_config = MsgQueueServiceConfig()
        self.__queue_name='img_car'

    def publish_msg(self,img_car=ImgCar()):
        img_car_msg=str(img_car)
        #建立通道
        channel=core.rabbitmq.create_channel(self.__msg_queue_service_config.host,self.__msg_queue_service_config.user,self.__msg_queue_service_config.pwd)
        #申明队列
        channel.queue_declare(queue=self.__queue_name)
        #f发布消息
        channel.basic_publish(exchange='', routing_key=self.__queue_name, body=img_car_msg)
        #关闭连接
        channel.connection.close()
        log_info('发布图片福利消息:%s' % (img_car_msg))

queue_name='img_car'
def img_car_msg_sender():
    username = 'guest'  # 指定远程rabbitmq的用户名密码
    pwd = 'guest'
    user_pwd = pika.PlainCredentials(username, pwd)
    s_conn = pika.BlockingConnection(pika.ConnectionParameters('127.0.0.1', credentials=user_pwd))  # 创建连接
    chan = s_conn.channel()
    chan.queue_declare(queue=queue_name)  # 声明一个队列，生产者和消费者都要声明一个相同的队列，用来防止万一某一方挂了，另一方能正常运行
    chan.basic_publish(exchange='', routing_key = queue_name, body = 'test 5')  # 生产者要发送的消息
    print("[生产者] send 'hello world")
    s_conn.close()  # 当生产者发送完消息后，可选择关闭连接

#img_car_msg_sender()

