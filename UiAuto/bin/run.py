#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/5/6 10:37
# @Author : msy


import sys
import os

#解决命令行运行，包找不到问题，把项目根路径放入到环境变量
# import HtmlTestRunner

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
from config import *
COMMONPATH=os.path.join(BASE_PATH,'common')
# # print(COMMONPATH)
sys.path.append(CASEPATH)
sys.path.append(COMMONPATH)
sys.path.append(LOGPATH)
sys.path.append(REPORTPATH)
sys.path.append(FILE)
# sys.path.append('E:\\software\python3.5.1\\UiAuto\\*')
# sys.path.append('E:\\software\python3.5.1\\UiAuto\\common\\*')
# sys.path.append('E:\\software\python3.5.1\\UiAuto\\common\\general.py')
# sys.path.append('E:\\software\python3.5.1\\UiAuto\\common\\log.py')
# sys.path.append('E:\\software\python3.5.1\\UiAuto\\common\\my_unittest.py')
# sys.path.append('E:\\software\python3.5.1\\UiAuto\\common\\rerun_case.py')
# sys.path.append('E:\\software\python3.5.1\\UiAuto\\common\\rerun_case1.py')
# sys.path.append('E:\\software\python3.5.1\\UiAuto\\common\\run_case.py')
# sys.path.append('E:\\software\python3.5.1\\UiAuto\\common\\send_email.py')
# sys.path.append('E:\\software\python3.5.1\\UiAuto\\page\\order_page.py')
# sys.path.append('E:\\software\\python3.5.1\\Lib\site-packages')
# sys.path.append('E:\\software\\python3.5.1\\Lib\site-packages\\xlrd')
# sys.path.append('E:\\software\\python3.5.1\\Lib\site-packages\\xlwt')
# sys.path.append('E:\\software\\python3.5.1\\Lib\site-packages\\logging')
# sys.path.append('E:\\software\\python3.5.1\\Lib\site-packages\\yaml')
# sys.path.append('E:\\software\\python3.5.1\\Lib\site-packages\\win32com')
# sys.path.append('E:\\software\\python3.5.1\\Lib\site-packages\\requests')
# sys.path.append('E:\\software\\python3.5.1\\Lib\site-packages\\selenium')
# sys.path.append('E:\\software\\python3.5.1\\Lib\site-packages\\win32')
# sys.path.append('E:\\software\\python3.5.1\\Lib\site-packages\\pymysql')
# sys.path.append('E:\\software\\python3.5.1\\Lib\site-packages\\xlutils')
# sys.path.append('E:\\software\\python3.5.1\\Lib\site-packages\\xlwt')
# sys.path.append('E:\\software\python3.5.1\\Scripts')
# sys.path.append('E:\\software\python3.5.1\\Scripts')
import unittest
from BeautifulReport import BeautifulReport
from common.test_case import Test_case
import time
import os
from common.log import *
from common.send_email import *
import sys, os




# BeautifulReport.report
#
# report (
# filename -> 测试报告名称, 如果不指定默认文件名为report.html
# description -> 测试报告用例名称展示
# report_dir='.' -> 报告文件写入路径
# theme='theme_default' -> 报告主题样式 theme_default theme_cyan theme_candy theme_memories
# )




if __name__ == '__main__':
    #   获取当前时间
    # suite = unittest.TestSuite()
    # filepath = []  # 测试报告
    # 不能通过测试套件加多个用例类的方式，因为这样会同时执行或者无规则执行
    # print('开始1')
    # for i in range(1,4):
    '''
    for i in range(1,2):
        nt = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
        # td=time.strftime('%Y/%m/%d', time.localtime(time.time()))
        # 当前时间与字符串拼接
        filename = nt +'-'+str(i)+ '.html'
        Mylog().my_log().warning('开始执行用例')
        suite = unittest.TestSuite()
        if i ==1:
            suite.addTest(unittest.TestLoader().loadTestsFromTestCase(Test_case))
            print('开始2')
            print('哈哈')
        elif i ==2:
            # 不能放在前面，前面导入的会在一开始就执行，一开始执行，会同时读到相同的用例，那就没有重跑的意义
            from common.test_case_rerun1 import Test_rerun1
            suite.addTest(unittest.TestLoader().loadTestsFromTestCase(Test_rerun1))
            print('开始3')
        else :
            from common.test_case_rerun2 import Test_rerun2
            suite.addTest(unittest.TestLoader().loadTestsFromTestCase(Test_rerun2))
            print('开始4')
        # filepath = os.path.join(REPORTPATH, filename)
        result = BeautifulReport(suite)
        result.report(filename=filename, description='测试报告统计', report_dir=REPORTPATH, theme='theme_cyan')
        print('开始5')
    '''
    nt = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
    # td=time.strftime('%Y/%m/%d', time.localtime(time.time()))
    # 当前时间与字符串拼接
    filename = nt  + '.html'
    suite = unittest.TestSuite()
    suite.addTest(unittest.TestLoader().loadTestsFromTestCase(Test_case))
    result = BeautifulReport(suite)
    result.report(filename=filename, description='测试报告统计', report_dir=REPORTPATH, theme='theme_cyan')

    # 发送邮件，发送钉消息，若要发送邮件，启用即可
    # from common.ding import *



    # 把测试用例也打包到邮件
    # 如果是使用多进程pytest -n2跑用例，以上不会输出报告
    # filelist=[]
    # # 把报告加入到列表
    # reportfiles = os.listdir(REPORTPATH)
    # if len(reportfiles) > 0:
    #     for f in reportfiles:
    #         # print(f)
    #         # 文件和删除目录的方式不一样，所以需要分开操作
    #         if os.path.isfile(os.path.join(REPORTPATH, f)):
    #             filelist.append(os.path.join(REPORTPATH, f))
    #         else:
    #             pass
    # else:
    #     print('目录下没有文件')
    #
    # # 把用例结果文件加入到列表
    # casefiles = os.listdir(CASEPATH)
    # if len(casefiles) > 0:
    #     for f in casefiles:
    #         # case目录下的文件夹存放的是在写返回结果的用例，把这个放到邮箱
    #         if os.path.isdir(os.path.join(CASEPATH, f)):
    #             for i in os.listdir(os.path.join(CASEPATH, f)):
    #                 filelist.append(os.path.join(os.path.join(CASEPATH, f),i))
    #         else:
    #             pass
    # else:
    #     print('目录下没有文件')
    # # 添加到邮件的附件
    # send_email(filepath=filelist)


