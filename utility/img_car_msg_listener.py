# -*- coding: utf-8 -*-
import pika
import sys
current_working_directory = "E:\python_project\king.car"
sys.path.append(current_working_directory)
from entity.car import ImgCar
from core.rabbitmq import MsgQueueServiceConfig
import core.rabbitmq
from core.log import *
from tests.entity.car_test import build_img_car

class ImgCarMsgListener:
    """
                    图片福利消息监听器
                        """
    def __init__(self):
        self.__msg_queue_service_config = MsgQueueServiceConfig()
        self.__queue_name='img_car'
        self.msg_receive_event_handler=None

    def run(self):
        log_info("启动图片消息监听器")
        #建立通道
        channel=core.rabbitmq.create_channel(self.__msg_queue_service_config.host,self.__msg_queue_service_config.user,self.__msg_queue_service_config.pwd)
        #申明队列
        channel.queue_declare(queue=self.__queue_name)
        def callback(ch, method, properties, body):
            self.on_msg_receive(ch, method, properties, body)
        channel.basic_consume(callback, queue=self.__queue_name,  no_ack=True)
        log_info("正在监听消息...")
        channel.start_consuming()

    def on_msg_receive(self,channel, method, properties, body):
        #记录日志
        log_info("=======================================================" )
        log_info("收到消息:%s"%(body))
        #字符串转换为对象
        img_car=ImgCar.deserialize(body)
        self.msg_receive_event_handler(img_car)

def img_car_msg_listenerd():
    username = 'guest'  # 指定远程rabbitmq的用户名密码
    pwd = 'guest'
    user_pwd = pika.PlainCredentials(username, pwd)
    s_conn = pika.BlockingConnection(pika.ConnectionParameters('127.0.0.1', credentials=user_pwd))  # 创建连接
    chan = s_conn.channel()  # 在连接上创建一个频道
    chan.queue_declare(queue='hello')  # 声明一个队列，生产者和消费者都要声明一个相同的队列，用来防止万一某一方挂了，另一方能正常运行
    def callback(ch, method, properties, body):  # 定义一个回调函数，用来接收生产者发送的消息
        print u'收到消息:%s'%(body)
    chan.basic_consume(callback,  # 调用回调函数，从队列里取消息
                       queue='hello',  # 指定取消息的队列名
                       no_ack=True)  # 取完一条消息后，不给生产者发送确认消息，默认是False的，即  默认给rabbitmq发送一个收到消息的确认，一般默认即可
    print('[消费者] waiting for msg .')
    chan.start_consuming()  # 开始循环取消息

# img_car=build_img_car()
# print 'king%s'%(img_car.num)
# img_car_msg_listenerd()


