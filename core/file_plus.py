# -*- coding: utf-8 -*-
import os

def create_dir(dir):
    """
                       创建目录
                       :param dir:  目录地址
                       :return:void
                    """
    # dir=dir.encode("GBK")
    dir = dir.decode('utf-8', 'ignore').encode('gbk')
    if not os.path.exists(dir):
        os.mkdir(dir)