# -*- coding: utf-8 -*-
from entity.car import ImgCar
from utility.img_file import *
from repository.img_car_repository import *

class ImgCarHandler:
    """
                    图片处理器
                        """

    def __init__(self, img_car=ImgCar()):
        self.img_car = img_car
        self.__img_file_rule = ImgFileRule()
        self.__img_file_storager = ImgFileStorager(self.img_car)
        self.__img_car_repository = ImgCarRepository()
        self.img_file_path_algorithm_func = lambda img_car, img: self.__img_file_rule.build_img_file_relative_path(
        img_car.catalog, img_car.topic, img.no)

    @actionlog('处理图片')
    def handle(self):
        #1.验证图片
        self._validate_img_car()
        #2.图片完整状态
        self.img_car.complete(self.img_file_path_algorithm_func)
        #3.下载存储图片
        self.__img_file_storager.excute_store()
        #4.图片信息入库
        self._add_img_car_to_db()

    @actionlog('验证图片实体')
    def _validate_img_car(self):
        pass

    @actionlog('图片信息入库')
    def _add_img_car_to_db(self):
        self.__img_car_repository.add(self.img_car)



