# -*- coding: utf-8 -*-
import sys
current_working_directory = "E:\python_project\king.car"
sys.path.append(current_working_directory)
import time
from entity.car import *
from utility.img_car_msg_sender import ImgCarMsgSender
from core.rabbitmq import *
from test.entity.car_test import *

#初始化
msg_quene_conf=MsgQueueServiceConfig()
msg_quene_conf.init(host='127.0.0.1',user='guest',pwd='guest')

#构造图片福利对象
img_car=build_img_car()

print img_car

#发送消息
img_car_msg_sender=ImgCarMsgSender()
img_car_msg_sender.publish_msg(img_car)