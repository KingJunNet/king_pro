# -*- coding: utf-8 -*-
import time
from entity.car import *
from utility.img_car_msg_listener import ImgCarMsgListener
from core.rabbitmq import *

def handle_img_car(img_car=ImgCar()):
    print str(img_car)

#初始化
msg_quene_conf=MsgQueueServiceConfig()
msg_quene_conf.init(host='127.0.0.1',user='guest',pwd='guest')
img_car_msg_listener=ImgCarMsgListener()
img_car_msg_listener.msg_receive_event_handler=lambda img_car:handle_img_car(img_car)
img_car_msg_listener.run()


