#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/5/6 10:42
# @Author : msy

import logging
from logging.handlers import RotatingFileHandler
from config import *
import time
import os

# 日志类
class Mylog():
    def __init__(self):
        #通过当前时间作为文件名
        self.tm = time.strftime('%y%m%d', time.localtime(time.time()))
        self.path = self.tm + '.log'
        self.f= os.path.join(LOGPATH, self.path)
        #print(self.f)

    	# try:
        #     os.path.isexists(self.f)
        # except Exception as e:
        #     print('文件不存在')
    # 日志方法
    def my_log(self):
        print(self.f)
        self.logger = logging.getLogger() # 日志实例类
        rthandler = RotatingFileHandler(self.f, mode='a', maxBytes=100 * 1024 * 1024,
                                        backupCount=6)  # 定义一个RomatingFileHandler
        rthandler.setLevel(logging.INFO)  # 测试日志级别
        # formatter = logging.Formatter('%(asctime)s %(mode) 12s-%(levelname)-8s: %(message)s')  # 设置日志输出格式
        formatter = logging.Formatter(
            '%(asctime)s-%(pathname)s-[line:%(lineno)d]-%(levelno)d-%(funcName)s-%(levelname)s-message:%(message)s')  # 设置日志输出格式
        rthandler.setFormatter(formatter)
        # self.logger.addHandler(rthandler)
        # print('打印handle',self.logger.handlers)
        # 如果没有句柄，则添加句柄，解决日志重复输出的问题
        if not self.logger.handlers:
            self.logger.addHandler(rthandler)
        else:
            pass
            # print('不需要重新定义')
        return self.logger