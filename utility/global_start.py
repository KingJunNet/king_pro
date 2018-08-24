# -*- coding: utf-8 -*-
import time
from core.file_plus import create_dir
from core.mongo_plus import MongoServiceConfig
from core.rabbitmq import MsgQueueServiceConfig
from utility.cfg_item import ImgCatalog
from utility.img_file import ImgFileRule

def create_catalog_dir():
    """
                           创建栏目目录
                           :param dir:  目录地址
                           :return:void
                        """
    for catalog_name in ImgCatalog.keys():
        img_file_rule=ImgFileRule()
        catalog_dir = img_file_rule.build_catalog_dir(catalog=catalog_name)
        create_dir(catalog_dir)


def global_start():
    """
              初始化
              :param catalog:  分类
              :return:void
           """
    # 创建栏目目录
    create_catalog_dir()

    # 加载mongo数据库配置
    mongo_conf = MongoServiceConfig()
    mongo_conf.init(ip='localhost', port=50000, db_name='OldDriverDB', user='', pwd='')

    # 加载消息队列服务配置
    msg_quene_conf = MsgQueueServiceConfig()
    msg_quene_conf.init(host='127.0.0.1', user='guest', pwd='guest')

