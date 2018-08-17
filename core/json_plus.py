# -*- coding: utf-8 -*-
import file_plus
class JsonConvert:
    """
           Json转换器
           """
    def __init__(self):
        pass

    @staticmethod
    def serialize_object(obj,ignore_fields=[]):
        '''把Object对象转换成Dict对象'''
        dict = {}
        dict.update(obj.__dict__)
        for field in ignore_fields:
            del dict[field]

        return dict