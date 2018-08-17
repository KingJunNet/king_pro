# -*- coding: utf-8 -*-
from core.log import *

@actionlog('输出信息')
def output_name(name=''):
    print("你的名字:%s" % (name))

class Person:
    def __init__(self,name=''):
        self.name=name
    @actionlog('输出人员信息')
    def output(self):
        print("%s" % (self.name))

output_name('王世君')
output_name('何茜')
output_name('王锦怡')
person=Person('王世娟')
person.output()
person=Person('王世梅')
person.output()