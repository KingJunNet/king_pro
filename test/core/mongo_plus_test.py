# -*- coding: utf-8 -*-
from core.mongo_plus import *

mongo_conf1=MongoServiceConfig()
mongo_conf2=MongoServiceConfig()
mongo_conf1.init("a",1,'aa','aaa','aaaa')
print '%s-%d-%s-%s-%s-'%(mongo_conf1.ip,mongo_conf1.port,mongo_conf1.db_name,mongo_conf1.user,mongo_conf1.pwd)
print '%s-%d-%s-%s-%s-'%(mongo_conf2.ip,mongo_conf2.port,mongo_conf2.db_name,mongo_conf2.user,mongo_conf2.pwd)

mongo_conf2.init("b",2,'bb','bbb','bbbb')
print '%s-%d-%s-%s-%s-'%(mongo_conf1.ip,mongo_conf1.port,mongo_conf1.db_name,mongo_conf1.user,mongo_conf1.pwd)
print '%s-%d-%s-%s-%s-'%(mongo_conf2.ip,mongo_conf2.port,mongo_conf2.db_name,mongo_conf2.user,mongo_conf2.pwd)