#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/5/6 10:58
# @Author : msy

import os
import sys
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)


BASE_PATH=os.path.dirname(os.path.abspath(__file__))    #配置文件父目录
print(BASE_PATH)
#print(BASE_PATH)
LOGPATH=os.path.join(BASE_PATH,'log')   #日志父目录
#print(LOGPATH)
CASEPATH=os.path.join(BASE_PATH,'case')   #用例父目录
REPORTPATH=os.path.join(BASE_PATH,'report')   #测试报告父目录
REPORTPATH_ALLURE=os.path.join(BASE_PATH,'report-allure')   #测试报告父目录
TESTER='msy'   #测试执行人
FILE=os.path.join(BASE_PATH,'file')
SCREEN_SHOT=os.path.join(FILE,'screenshot')
#浏览器，chrome 谷歌  ie IE  firefox，火狐
WEBBROSER='chrome'
# WEBBROSER='firefox'
#测试网站
# URL='http://10.10.1.110:8080/'
URL='https://uaterp.pgl-world.com.cn'
# 登录账号
USENAME='sybmsy'
# 登录密码
PASSWORD='12345678'
# 数据库服务
HOST='10.10.1.131'
# 数据库账号
USER='saadmin'
# 端口
PORT=3306
# 数据库账号密码
DBPASSWORD='erpmysql2019'
# 登录数据
DATABASE='pgl_erp_oss_uat'
# 数据库类型
DATATYPE='mysql'

# YAML=os.path.join(BASE_PATH,'yamlconfig')