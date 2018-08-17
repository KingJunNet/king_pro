# -*- coding: utf-8 -*-
import os
import time
import requests
from bs4 import BeautifulSoup
from core.json_plus import JsonConvert
from core.singleton import singleton
import cfg_item
from entity.car import ImgCar
from core.file_plus import  create_dir
from core.down_file import download_img_file
from core.log import *

@singleton
class ImgFileRule:
    def __init__(self):
        self.__file_root_path =  'E:/pythoncode/static/File/'

    def build_catalog_dir(self,catalog = 0):
        """
                           构造栏目目录
                           :param catalog:  分类
                           :return:主题目录
                        """
        catalog_name= cfg_item.ImgCatalog[catalog]
        dir = self.__file_root_path + catalog_name + '/'
        return dir

    def build_topic_dir(self,catalog = 0, topic = ''):
        """
                           构造主题目录
                           :param catalog:  分类
                           :param topic:  主题
                           :return:主题目录
                        """
        catalog_name= cfg_item.ImgCatalog[catalog]
        dir = self.__file_root_path + str(catalog_name) + '/' + str(topic) + '/'
        return dir

    def build_img_file_name(self,topic='', no=0,extension='jpg'):
        """
                                   构造图片文件名称
                                   :param catalog:  分类
                                   :param topic:  主题
                                   :return:主题目录
                                """
        return topic+'_'+str(no)+'.'+extension

    def build_img_file_relative_path(self, catalog=0, topic='', no=0, extension='jpg'):
        """
                                           构造图片文件相对路径
                                           :param catalog:  分类
                                           :param topic:  主题
                                           :return:主题目录
                                        """
        catalog_name = cfg_item.ImgCatalog[catalog]
        file_path = str(catalog_name) + '/' + str(topic) + '/' + self.build_img_file_name(topic, no, extension)
        return file_path

    def build_img_file_path(self, catalog=0, topic='', no=0, extension='jpg'):
        """
          构造图片文件路径
          :param catalog:  分类
          :param topic:  主题
          :param no:  序号
          :param extension:  主题
          :return:图片文件路径
       """
        return self.__file_root_path + self.build_img_file_relative_path(catalog,topic,no,extension)

    def build_img_file_path(self, mg_file_relative_path=''):
        return self.__file_root_path + mg_file_relative_path

class ImgFileStorager:
    """
                    图片文件存储器
                        """
    def __init__(self, img_car=ImgCar()):
        self.img_car = img_car

    __img_file_rule=ImgFileRule()

    @actionlog('存储图片')
    def excute_store(self):
        """
                                  执行存储
                                  :return:void
                               """
        #创建目录
        self.create_topic_dir()
        #创建文件
        self.create_img_file()

    @actionlog('创建主题目录')
    def create_topic_dir(self):
        """
                           创建主题目录
                           :param bets:  赌注集
                           :return:void
                        """


        topic_dir=self.__img_file_rule.build_topic_dir(catalog=self.img_car.catalog,topic=self.img_car.topic)
        create_dir(topic_dir)

    @actionlog('创建文件')
    def create_img_file(self):
        """
                                  创建图片文件
                                  :param bets:  赌注集
                                  :return:void
                               """
        for img in self.img_car.imgs:
            img_file_path=self.__img_file_rule.build_img_file_path(mg_file_relative_path=img.path)
            download_img_file(img.url,img_file_path)