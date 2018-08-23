# -*- coding: utf-8 -*-
import time

CONST_DEFAULT_TIME_FOMAT = "%Y-%m-%d %H:%M:%S"
# def deco(arg):
#     def _deco(func):
#         def __deco():
#             print("before %s called [%s]." % (func.__name__, arg))
#             func()
#             print("  after %s called [%s]." % (func.__name__, arg))
#         return __deco
#     return _deco
#
# def deco(func):
#     def _deco(*args, **kwargs):
#         print("before %s called." % func.__name__)
#         ret = func(*args, **kwargs)
#         print("  after %s called. result: %s" % (func.__name__, ret))
#         return ret
#     return _deco

def logattribute(message=''):
    def _log(func):
        def __log(*args, **kwargs):
            ret = func(*args, **kwargs)
            ope_time=time.strftime(CONST_DEFAULT_TIME_FOMAT,time.localtime())
            print("  %s | INFO | %s" % (ope_time, message))
            return ret
        return __log
    return _log

def actionlog(action=''):
    def _log(func):
        def __log(*args, **kwargs):
            begin_text="%s | INFO | 开始%s" % (time.strftime(CONST_DEFAULT_TIME_FOMAT, time.localtime()), action)
            print begin_text.decode('UTF-8')
            ret = func(*args, **kwargs)
            end_text="%s | INFO | %s结束" % (time.strftime(CONST_DEFAULT_TIME_FOMAT,time.localtime()), action)
            print end_text.decode('UTF-8')
            return ret
        return __log
    return _log

def log_info(message=''):
    print(("%s | INFO | %s" % (time.strftime(CONST_DEFAULT_TIME_FOMAT, time.localtime()), message)).decode('UTF-8'))