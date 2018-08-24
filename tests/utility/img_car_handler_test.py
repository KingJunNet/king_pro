# -*- coding: utf-8 -*-
import time
from core.file_plus import create_dir
from entity.car import *
from core.mongo_plus import *
from utility.cfg_item import ImgCatalog
from utility.img_file import *


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

#初始化
create_catalog_dir()
from utility.img_car_handler import ImgCarHandler, ImgFileRule

mongo_conf=MongoServiceConfig()
mongo_conf.init(ip='localhost',port=50000,db_name='OldDriverDB',user='',pwd='')

#构造图片福利
img_car=ImgCar()
img_car.crude(topic='港媒：歼20跻身世界最先进喷气式战机 可媲美F-22', catalog=1, publish_time=time.time(), catch_time=time.time())
img1=Img()
img1.crude("https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1534330777385&di=8964941d79e54f50dd9c6e4d98ac60c4&imgtype=0&src=http%3A%2F%2Fn.sinaimg.cn%2Fsinacn19%2F266%2Fw640h426%2F20180515%2F87a4-hapkuvm3684064.jpg")
img2=Img()
img2.crude("https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1534330776990&di=e8c53a8af0f68b8059662f19010e9632&imgtype=0&src=http%3A%2F%2Fimg9.itiexue.net%2F2150%2F21502461.jpg")
img3=Img()
img3.crude("https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1534330777390&di=8cf6b983eddd9647e93f374fabd22e6f&imgtype=0&src=http%3A%2F%2F05.imgmini.eastday.com%2Fmobile%2F20171130%2F20171129_b7878026d7a51dc98fce24404c854ea9_mwpm_05501609.jpg")
img4=Img()
img4.crude("https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1534330777390&di=9336e2b0e72f9d6f38f891c45d3c3931&imgtype=0&src=http%3A%2F%2F01.imgmini.eastday.com%2Fmobile%2F20170707%2F20170707010832_397dc7df28461ca39fb9150d0cdc47ae_2.jpeg")
img5=Img()
img5.crude("https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1534330777389&di=2f35a3e47fb787fa53d994fe7915d393&imgtype=0&src=http%3A%2F%2F01.imgmini.eastday.com%2Fmobile%2F20171017%2F1d9c2db83ffd9d7221f9220647e57514.jpeg")
img_car.add_img(img1)
img_car.add_img(img2)
img_car.add_img(img3)
img_car.add_img(img4)
img_car.add_img(img5)

img_car_handler= ImgCarHandler(img_car)
img_car_handler.handle()

print '结束'