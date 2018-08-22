# -*- coding: utf-8 -*-
from pymongo import MongoClient
from core.singleton import singleton
import pika

@singleton
class MsgQueueServiceConfig:
    def __init__(self):
        self.host = ''
        self.user = ''
        self.pwd = ''

    def init(self,host,user,pwd):
        self.host = host
        self.user = user
        self.pwd = pwd

    def init_from_config_file(self,config_file_path):
        pass

def create_connection(host,user,pwd):
    user_pwd = pika.PlainCredentials(user, pwd)
    connection = pika.BlockingConnection(pika.ConnectionParameters(host, credentials=user_pwd))  # 创建连接

    return connection


def create_channel(host, user, pwd):
    connection= create_connection(host,user,pwd)
    channel = connection.channel()

    return channel




