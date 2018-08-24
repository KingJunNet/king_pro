# -*- coding: utf-8 -*-
import time
from core.log import log_info
from entity.car import *
from utility.img_car_handler import ImgCarHandler
from utility.img_car_msg_listener import ImgCarMsgListener
from utility.global_start import global_start

#处理图片
def handle_img_car(img_car=ImgCar()):
    img_car_handler = ImgCarHandler(img_car)
    img_car_handler.handle()

#初始化
global_start()

#启动监听器
img_car_msg_listener=ImgCarMsgListener()
img_car_msg_listener.msg_receive_event_handler=lambda img_car:handle_img_car(img_car)
img_car_msg_listener.run()







