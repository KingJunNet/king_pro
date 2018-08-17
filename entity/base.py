# -*- coding: utf-8 -*-
from core.json_plus import JsonConvert

class BaseEntity:
    """
       实体基类
           """
    def __init__(self, id=''):
        self.id = id

    def to_json(self):
       return JsonConvert.serialize_object(self, ['id'])