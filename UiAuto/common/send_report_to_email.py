# -*- coding: utf-8 -*-
# @Time    : 2020/11/13 15:31
# @Author  : msy
# @File    : test_sendreport.py
# @Software: PyCharm


import os
import sys
# import unittest
# import pytest
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
from config import *
from common.send_email import *
from common.data_operate import *
COMMONPATH=os.path.join(BASE_PATH,'common')
sys.path.append(COMMONPATH)

def send():
    try:
        filelist = []

        reportfiles = os.listdir(REPORTPATH)
        if len(reportfiles) > 0:
            for f in reportfiles:
                # print(f)
                # 判断为文件
                if os.path.isfile(os.path.join(REPORTPATH, f)):
                    # 判断为不是html格式文件则跳过
                    if os.path.basename(os.path.join(REPORTPATH, f)).split('.')[1] != 'html':
                        # print(os.path.basename(os.path.join(REPORTPATH, f)).split('.')[1])
                        pass
                        # print('文件不html格式，不处理')
                    # 否则是html格式文件
                    else:
                        # 判断html格式文件的名称是index，则是allure报告 ，需要压缩文件
                        if os.path.basename(os.path.join(REPORTPATH, f)).split('.')[0] == 'index':
                            filelist.append(DataOperate().zip_file(REPORTPATH))
                        # 判断html格式文件的名称不是index，则可能是beautiful或pytest-html报告 ，则直接把路径加入列表
                        else:
                            filelist.append(os.path.join(REPORTPATH, f))

                else:
                    pass
                    # print('不是文件，不处理')
        else:
            print('目录下没有文件')

        # 把用例结果文件加入到列表
        casefiles = os.listdir(CASEPATH)
        if len(casefiles) > 0:
            for f in casefiles:
                # case目录下的文件夹存放的是在写返回结果的用例，把这个放到邮箱
                if os.path.isdir(os.path.join(CASEPATH, f)):
                    for i in os.listdir(os.path.join(CASEPATH, f)):
                        filelist.append(os.path.join(os.path.join(CASEPATH, f), i))
                else:
                    pass
        else:
            print('目录下没有文件')

        # print('打印发送邮件的文件',filelist)
        # 添加到邮件的附件
        send_email(filepath=filelist)
    except Exception as e:
        print(e)

    return filelist

# print(send())



