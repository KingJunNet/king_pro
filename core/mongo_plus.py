# -*- coding: utf-8 -*-
from pymongo import MongoClient

from core.singleton import singleton


@singleton
class MongoServiceConfig:
    def __init__(self):
        self.ip = ''
        self.port = 0
        self.db_name = ''
        self.user = ''
        self.pwd = ''

    def init(self,ip='',port=0,db_name='',user='',pwd=''):
        self.ip = ip
        self.port = port
        self.db_name = db_name
        self.user = user
        self.pwd = pwd

    def init_from_config_file(self,config_file_path):
        pass


class MongoSession:
    """
            MongoDB会话对象
            """
    # def __init__(self):
    #     mongo_service_config=MongoServiceConfig()
    #     self._init_db(mongo_service_config.ip,mongo_service_config.port,mongo_service_config.db_name)

    def __init__(self,ip='', port=0, db_name=''):
        if ip=='' and port==0 and db_name=='':
            mongo_service_config = MongoServiceConfig()
            self._init_db(mongo_service_config.ip, mongo_service_config.port, mongo_service_config.db_name)
        else:
            self._init_db(ip,port,db_name)

    def _init_db(self,ip, port, db_name):
        self.ip=ip
        self.port=port
        self.db_name=db_name
        self.connect_str='mongodb://%s:%d'%(ip,port)
        self.mongo_client = MongoClient(self.connect_str)
        self.db = self.mongo_client[db_name]