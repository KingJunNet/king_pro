# -*- coding: utf-8 -*-
from core.mongo_plus import *
from core.singleton import singleton
from entity.base import BaseEntity
from entity.car import ImgCar
from pymongo import MongoClient
from bson.objectid import ObjectId
from core.json_plus import JsonConvert
import json

def _img_car_doc_2_entity(img_doc):
    """return value of object for pickling.
           needed explicitly because __slots__() defined.
           """
    img_urls=[]
    if img_doc.has_key('img_urls'):
        img_urls=img_doc['img_urls']
    img=ImgCar(str(img_doc['_id']) ,img_doc['title'],img_doc['catalog'],img_doc['num'],img_urls,img_doc['publish_time'],img_doc['catch_time'])
    return img

def _img_car_entity_2_json(img_car=ImgCar()):
    """
        图片实体转换为json对象
        :param img_car:  图片实体
        :return:图片集合
        """
    # img_car_json={
    #     "title" : img_car.title,
    #     "catchTime" : img_car.catch_time,
    #     "publishTime" : img_car.publish_time,
    #     "catalog" : img_car.catalog,
    #     "num" : img_car.num,
    #     "imgUrls" : img_car.img_urls
    # }

    img_car_json=json.dumps(img_car)
    print img_car_json

    return img_car_json

class BaseRepository:
    """
        基础仓储
        """
    def __init__(self):
        self.mongo_session=MongoSession()
        pass

    def add(self,entity= BaseEntity()):
        entity_json = entity.to_json()
        result = self.get_collection().insert_one(entity_json)
        id = str(result.inserted_id)

    def get_collection(self):
        pass

class ImgCarRepository(BaseRepository):
    def __init__(self):
        BaseRepository.__init__(self)

    def get_collection(self):
        return self.mongo_session.db.ImgCar

class ImgCarRepositoryB(BaseRepository):
    def __init__(self):
        self.__mongo_client = MongoClient('mongodb://localhost:50000')
        self.__db = self.__mongo_client.OldDriverDB
        pass

    def get_img_cars(self, from_time,to_time):
        """
        获取指定ID的图片
        :param id:  tuple of (short opt, long opt), e.g: ('-f', '--format')
        :return:图片集合
        """
        img_cars = []

        img_cursor =self.__db.ImgCar.find({"catch_time": {"$gt": from_time, "$lt": to_time}},{"img_urls":0})
        for img_doc in img_cursor:
            img_car=_img_car_doc_2_entity(img_doc)
            img_cars.append(img_car)

        return img_cars

    def get_imgs(self, id=''):
        """
        获取指定ID的图片
        :param id:  tuple of (short opt, long opt), e.g: ('-f', '--format')
        :return:图片集合
        """
        imgs = []

        img_cursor =self.__db.ImgCar.find({"_id" : ObjectId(id)})
        for img_doc in img_cursor:
            print(img_doc['_id'])
            for img in img_doc['img_urls']:
                imgs.append(img)

        return imgs

    def add_img_car(self,img_car=ImgCar()):
        """
                获取指定ID的图片
                :param id:  tuple of (short opt, long opt), e.g: ('-f', '--format')
                :return:图片集合
                """
        id=''

        img_car_json=JsonConvert.serialize_object(img_car,['id'])
        img_car_json2=img_car.to_json()
        result = self.__db.ImgCar.insert_one(img_car_json)
        result = self.__db[''].insert_one(img_car_json)
        id=str(result.inserted_id)

        return id