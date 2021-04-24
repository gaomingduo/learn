# encoding=utf-8
# @time   :2020/5/11 10:54
# @Author :liulaing.song
# @Email  :1056703204@qq.com
# @File   :ParseConfig.py
# @explain:读取配置文件

from configparser import ConfigParser
from config.VarConfig import *
import time


class ParseConfig(object):

    # 构造函数
    def __init__(self):
        self.cf = ConfigParser()
        self.cf.read(configPath, 'utf-8-sig')

    # 获取配置文件中的值
    def getValue(self, sectionName, optionName):
        time.sleep(1)
        value = self.cf.get(sectionName, optionName)
        return value
