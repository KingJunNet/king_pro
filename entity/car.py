# -*- coding: utf-8 -*-
import time
from core.json_plus import JsonConvert
from base import BaseEntity

class Img:
    """
        图片
            """
    def __init__(self,url,description):
        self.url = url
        self.description = description

    def __init__(self,no=0,url='',path='',description=''):
        self.no = no
        self.url = url
        self.path=path
        self.description=description

    def crude(self, url='',description=''):
        self.url = url
        self.description = description

class Car(BaseEntity):
    """
       福利
           """
    def __init__(self, id='', topic='', catalog=0, publish_time=time.time(), catch_time=time.time()):
        BaseEntity.__init__(self,id)
        self.topic = topic
        self.catalog = catalog
        self.publish_time = publish_time
        self.catch_time = catch_time

class ImgCar(Car):
    """
    图片福利
        """

    def __init__(self, id='', topic='', catalog=0, publish_time=time.time(), catch_time=time.time(), num=0, imgs=[]):
        Car.__init__(self,id, topic, catalog, publish_time, catch_time)
        self.num = num
        self.imgs = imgs

    def crude(self,id='', topic='', catalog=0, publish_time=time.time(), catch_time=time.time()):
        self.id=id
        self.topic = topic
        self.catalog = catalog
        self.publish_time = publish_time
        self.catch_time = catch_time

    def add_img(self,img=Img()):
        self.num+=1
        img.no=self.num
        self.imgs.append(img)

    def complete(self,file_path_algorithm_func):
        self.perfect_img_file_path(file_path_algorithm_func)

    def perfect_img_file_path(self,file_path_algorithm_func):
        """
                             补充图片文件路径
                             :return:利润值
                             """
        for img in self.imgs:
            img.path=file_path_algorithm_func(self,img)

    def is_valid(self):
        return True

    def to_json(self):
       img_car_dict= JsonConvert.serialize_object(self, ['id','imgs'])
       imgs_dict=[]
       for img in self.imgs:
           img_dict= JsonConvert.serialize_object(img)
           imgs_dict.append(img_dict)

       img_car_dict['imgs']=imgs_dict

       return img_car_dict

