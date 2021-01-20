# # -*- coding: utf-8 -*-
# # @Time    : 2020/7/17 14:05
# # @Author  : msy
# # @File    : test.py
# # @Software: PyCharm
import os
from config import *
import time
import sys
from common.commethod import *
# import pytest
'''
FILE1=os.path.dirname(__file__)
ls=[i for i in os.listdir(FILE1) if os.path.isfile(i)]
print(ls)
ls.sort(key=lambda x:os.path.getmtime(os.path.join(FILE1,x)))
print(ls)
'''

# FILE1=os.path.abspath(__file__)
# print(os.path.basename(__file__))
# print(dir(os.path))
#
# 一般来说os._exit() 用于在线程中退出
# sys.exit() 用于在主线程中退出
# os._exit(2)
# sys.exit()
# max()
# lf=[]
# # print(os.listdir(FILE))
# for i in os.listdir(FILE):
# #     # 列表中有元组时，默认按第一个排序
# #
#     lf.append((time.strftime('%Y%m%d%H%M%S',time.localtime(os.path.getmtime(os.path.join(FILE,i)))),i))
# #     # ll.append(time.strftime('%Y%m%d%H%M%S',time.localtime(os.path.getmtime(os.path.join(FILE,i)))))
# # lf.sort(reverse=True)
# # print(lf[0][1])
# # print(os.path.join(FILE,lf[0][1]))
# # os.path.getmtime() 函数是获取文件修改时间
# #  8         # os.path.getctime() 函数是获取文件创建时间
#  9         dir_list = sorted(dir_list,key=lambda x: os.path.getmtime(os.path.join(file_path, x)))
# lf=sorted(os.listdir(FILE),key= lambda x:os.path.getmtime(os.path.join(FILE,x)),reverse=True)
# print(lf)
# with open(os.path.join(FILE,lf[0]), 'r+',encoding='utf-8') as file1:
#     print('文件名',lf[0])
#     # 全部输出，与文件保持一致
#
#     print('文件内容',file1.read())
#     # 不会自动换行，连换行符也会打印
#     # print('文件内容',file1.read())
#     # print(file1.tell())
#     # print(file1.seek(400))
#     # print(file1.tell())
#     # print('文件内容', file1.read())
#
#
#     # file1.tell(file1.seek())
#     # 一行一行打印，不会打印换行符
#     # for i in file1.readlines():
#     #     print('哈哈')
#     #     print('文件内容:',i)

# import platform
# print(platform.platform())
# print(platform.uname())
# from decimal import *
# # print(Decimal(3.3).compare(Decimal(5.1)))
# # print(Decimal(3.1).quantize(Decimal('1.1100')))
# # print(Decimal(-3.1).copy_abs().quantize(Decimal('1.1100')))
# # print(Decimal(-3.1).quantize(Decimal('1.1100')))
# # print(Decimal(-3.1).copy_sign(12))
# print(Decimal('3.22'))
# print(type(Decimal('3.22')))
# print((Decimal(5.3).max(Decimal(8.3))).quantize(Decimal('1.1100')))
import re
# prog = re.compile('\d{2}')
# print(prog.match('12122sd234sdf').group())
# print(prog.search('sd234sdf').group())
# print(re.match('\D{2}','12122sd234sdf基基'))    # 从开始匹配
# print(re.search(r'[\D{2,6}\d]','基本面sdasdasdasdas234sdf11').group())   #从任一位置匹配
# print(re.split('[2d]','12122sdad夺遥顶替234sdf'))   #分隔，通过正则
# # 替换，要替换的内容，替换后的内容，要处理的字符串，替换长度，没有输入默认就是全部符合的都替换
# su=re.sub('[f]','g','12122sd234sdf')
# print(re.sub('[f]','kk','1dssf1fd234sdf',1))

import io

import io
#文件创建文本流
# f = open('myfile.txt','r',encoding='utf-8')

#内存中的文本流可以使用StringIO对象来创建
# f1 = io.StringIO("some initial text datal")
# print(f1.getvalue()) #读取文本流信息

import sys    # 软件环境
import os
import time
import platform   #硬件环境
# print(sys.argv)
# print(sys.argv[0])
# print(sys.path)
# # print(os.path.abspath(__file__))
# # print(os.path.basename(__file__))
# print(os.path.dirname(__file__))
# print(os.path.dirname(os.path.dirname(__file__)))
# print(sys.version)
# print(sys.platform)
# print(sys.base_prefix)
# print(platform.platform())
# print(platform.version())
# print(platform.machine())
# print(platform.processor())
# sys.exit()   #终止程序，后面的语句不再执行，也不会有报错输出
# print(sys.stdout.write('小马过河'))
# print(sys.stderr.write('小马过河'))
# print()
# print(os.path.split(__file__))
# print(os.path.exists(__file__))
# print(os.path.isfile(__file__))
'''
print(time.strftime('%Y%m%d %H:%M:%S',time.localtime(os.path.getmtime(r'D:\Personal\moshuangyou\Desktop\1206.xlsx'))))
print(time.strftime('%Y%m%d %H:%M:%S',time.localtime(os.path.getatime(r'D:\Personal\moshuangyou\Desktop\1206.xlsx'))))
print(time.strftime('%Y%m%d %H:%M:%S',time.localtime(os.path.getctime(r'D:\Personal\moshuangyou\Desktop\1206.xlsx'))))
print(os.path.ismount(r'D:\Personal\moshuangyou\Desktop\1206.xlsx'))
print(os.path.isabs(r'D:\Personal\moshuangyou\Desktop\1206.xlsx'))
print(os.path.islink(r'D:\Personal\moshuangyou\Desktop\1206.xlsx'))
print(os.path.lexists(r'D:\Personal\moshuangyou\Desktop\1206.xlsx'))
'''
# print(__file__)

# import xlrd
# import xlwt
# import xlutils
# import json
# from xlutils.copy import copy
# import openpyxl   #用openpyxl 模块读取了xls格式的excel,
# 或者读取的是xls文件通过改变后缀变成xlsx格式的文件会报错，所以要另存方式修改

# wb = openpyxl.load_workbook(r'D:\Personal\moshuangyou\Desktop\1206.xlsx')   # 加载表格
# # wb.save(r'D:\Personal\moshuangyou\Desktop\1206.xlsx')
# sh_name = wb.sheetnames  # 获取所有sheet
# sh = wb[sh_name[0]]
# sh.title = "dddd"  # 修改第一个sheet名为dddd
# wb.close()

# rbook=openpyxl.load_workbook(r'D:\Personal\moshuangyou\Desktop\1206.xlsx')
# ws=rbook['test']
# ws.title='new'     #修改表格名
# rbook.save(r'D:\Personal\moshuangyou\Desktop\1206.xlsx')
# rbook.close()
# print('结束')


# '\' 要用r,保持字符原始值，否则：替换为双反斜杠或者替换为正斜杠
# bok=xlrd.open_workbook(r'D:\Personal\moshuangyou\Desktop\1206.xlsx')
# print(bok.sheet_names())  #各表格名称
#
# sheet=bok.sheet_by_index(0)
# print(sheet.cell(1,3))
# print(sheet.get_rows())
# print(sheet.row_values(2))
# print((sheet.cell())
# print(sheet.nrows)
# print(sheet.ncols)
# bok2=copy(bok)
# bok2.add_sheet('test3')  #添加表格
# sheet2=bok2.get_sheet(3)
# # sheet2.write(2,2,'12')
# w=bok2['test']
# w.title='new'
# bok2.save(r'D:\Personal\moshuangyou\Desktop\1206.xlsx')
# print(sheet2.cell(2,2))


# bok2=xlwt.Workbook(r'D:\Personal\moshuangyou\Desktop\1206.xlsx')
# ta=bok2.add_sheet('test')
# bok2.save()
# sheet2=bok.sheet_by_name(('test'))
# sheet2.cell(1,1,'323')


# bok2.save()

'''
# 2020-09-30

import time
print(time.gmtime(0))
print(time.gmtime(time.time()))
print(time.mktime(time.gmtime()))
print(time.time())
print(time.asctime())
print(time.localtime(time.time()))
print(time.localtime())

print(time.clock())
print(time.ctime())
print(time.thread_time())

from datetime import datetime,timedelta
import calendar
print('datatime-----')
print(datetime.now())
print(datetime(1,10,12,13,17,23))
print(datetime.strftime())
print(time.strftime())
print(datetime.now()+timedelta(hours=1,days=1,minutes=3))
print(calendar.isleap(202))
print(calendar.leapdays(2022,2060))
print(calendar.prmonth(2022,6))
print(calendar.month(2022,6))

'''
# print(type('Keys.'+'{}'.format('ENTER')))
# print(os.path.join(BASE_PATH,'yamlconfig.yaml'))
#
# import yaml
# try:
#     with open(os.path.join(BASE_PATH, 'yamlconfig.yml'), 'r',encoding='utf-8') as f:
#         l = [i for i in yaml.load_all(f)]
#         print(l)
#         # print(type(l[0]))
#         print(l[1])
#         print(l[0]['username'])
#         print(l[1]['customer_filtering_value'])
# except Exception as e:
#     print(e)
#
# for i in rangeyield(1,9):
#     print(i)
#
# a = [1,2,3]
# for item in map(lambda x:x*x, a):
#     print(item, end=', ')
# text='创建成功！合并单号：HB202010150013'
# if  '创建成功！' in text:
#     print('真')
# else:
#     print('假')
# from decimal import Decimal
# text='99.0'
# for i in range(1):
#     text1 = Decimal(text).quantize(Decimal("0.0000"))
#     # 转换成功列表
#     text=str(text1)
#     # text.append(text)
#     print('打印text:', text)
#
# import xlwt
# style = xlwt.XFStyle()#格式信息
# font = xlwt.Font()#字体基本设置
# font.name = u'微软雅黑'
# font.color = 'black'
# font.height= 220 #字体大小，220就是11号字体，大概就是11*20得来的吧
# style.font = font
# alignment = xlwt.Alignment() # 设置字体在单元格的位置
# alignment.horz = xlwt.Alignment.HORZ_CENTER #水平方向
# alignment.vert = xlwt.Alignment.VERT_CENTER #竖直方向
# style.alignment = alignment
# border = xlwt.Borders()  #给单元格加框线
# border.left = xlwt.Borders.THIN  #左
# border.top=xlwt.Borders.THIN     #上
# border.right=xlwt.Borders.THIN   #右
# border.bottom=xlwt.Borders.THIN  #下
# border.left_colour = 0x40  #设置框线颜色，0x40是黑色，颜色真的巨多，都晕了
# border.right_colour = 0x40
# border.top_colour = 0x40
# border.bottom_colour = 0x40
# style.borders = border
# #写入sheet
# row=1
# col=1
# value=100
# wb = xlwt.Workbook()
# ws = wb.add_sheet('sheet1')
# ws.write(row,col,value,style)#这样就可以写入自己想要的格式了

# print(sys.path)
# def Singleton(cls):
#     instances = {}

# thread1=threading.Thread(target=run.recivalble_cost,args=('2020063002',))
        # 守护线程是指守护主线程的 ;也就是说守护线程不依赖于终端，但是依赖于系统，与系统“同生共死”;当java虚拟机中没有非守护线程在运行的时候，java虚拟机会关闭。
        # 当所有常规线程运行完毕以后，守护线程不管运行到哪里，虚拟机都会退出运行。所以你的守护线程最好不要写一些会影响程序的业务逻辑。
        # 否则无法预料程序到底 会出现什么问题。
        # thread2.setDaemon(True)
        # thread1.start()

		#  * 主线程向下转时，碰到了t1.join(),t1要申请加入到运行中来，就是要CPU执行权。
		#  * 这时候CPU执行权在主线程手里，主线程就把CPU执行权给放开，陷入冻结状态。
		#  * 活着的只有t1了，只有当t1拿着执行权把这些数据都打印完了，主线程才恢复到运行中来
		#  */
		# //join 方法 确保 t1执行之后 执行t2
		# t1.join();
		# t2.start();

        # thread1.join()

# thread1=MyThread(target=RunCase().run_case,args=(args,))
                # % 执行取模运算，返回除法的余数
                # print(args[11]%3==0)
                # if args[11]%3==0:
                #     thread1=MyThread(target=RunCase().run_case,args=(args,))
                #     # thread1 = threading.Thread(target=RunCase().run_case, args=(args,))
                #     thread1.start()
                #     thread1.join()
                #     result = thread1.get_result()
                #     print('打印',thread1)
                # else:
                #     result = RunCase().run_case(args)

                # result = RunCase().run_case(args)
                # thread1 = MyThread(target=RunCase().run_case, args=(args,))
                # thread1 = threading.Thread(target=RunCase().run_case, args=(args,))
                # Process(target=RunCase().run_case, args=(args,)).start()
                # thread1.start()
                # thread1.join()
                # result = thread1.get_result()
                # print('打印', thread1)


import shutil

# 删除文件夹，把文件夹也删除了
# shutil.rmtree('E:\\software\\tomcat\\apachetomcat9\\webapps\\report')
# 移除文件夹，如果report存在，会报错
# shutil.copytree('E:\\software\\Python3.8.3\\UiAuto\\report','E:\\software\\tomcat\\apachetomcat9\\webapps\\report')
# 删除压缩文件
# os.remove('E:\\software\\Python3.8.3\\UiAuto\\report.zip')
# os.remove('E:\\software\\Python3.8.3\\UiAuto\\笔记 - 副本.txt')

import os
import shutil
import zipfile
from os.path import join, getsize

# # 压缩文件夹
# def zip_file(src_dir):
#     zip_name = src_dir +'.zip'
#     z = zipfile.ZipFile(zip_name,'w',zipfile.ZIP_DEFLATED)
#     for dirpath, dirnames, filenames in os.walk(src_dir):
#         fpath = dirpath.replace(src_dir,'')
#         fpath = fpath and fpath + os.sep or ''
#         for filename in filenames:
#             z.write(os.path.join(dirpath, filename),fpath+filename)
#             # print ('==压缩成功==')
#     z.close()
#
# zip_file('E:\\software\\Python3.8.3\\UiAuto\\report')

# send_email(filepath=['E:\\software\\Python3.8.3\\UiAuto\\report.zip'])
# send_email(filepath=['E:\\software\\Python3.8.3\\UiAuto\\笔记.txt'])

# print(os.path.split(r'E:\software\Python3.8.3\UiAuto\report'))
# from common.general import *
# from config import *
# from common.log import *
# import time
# from common.data_operate import *
# import threading
# # import lock
# # from multiprocessing import Lock,Process
#
# # def order_decorator(args):
# #     pass
# #     新增订单方法已被多处调用，新增一个参数，调用代码也要修改，尝试考虑用装饰器，
# #     但目前了解到装饰器更多适用增加额外功能，修改原方法的逻辑目前不知道如何实现
#
#
#
# # 订单页面类
# class OrderPage(BasePage):
#     # 系统首页页签
#     tab = ['xpath', '//*[@id="index_tabs"]/div[1]/div[3]/ul/li[1]/a/span[1][text()="系统首页"]']
#     # 订单管理模块
#     order_manage_module = ['xpath', '//td[@title="订单管理"]/child::a[1]']
#     # 订单处理
#     order_deal_with = ['xpath', '//span[text()="订单处理_运输"]/parent::div[starts-with(@id,"_easyui_tree")]']
#     def atest(self):
#         self.login()
#         # 关闭所有标签
#         # self.context_choice(self.tab[0], self.tab[1], index=['down', 'down', 'down', 'down'])
#         time.sleep(3)
#         # 一级菜单
#         self.click(self.order_manage_module[0], self.order_manage_module[1])
#         # 二级菜单
#         self.click(self.order_deal_with[0], self.order_deal_with[1])
#         time.sleep(1)

# OrderPage().atest()

# data='{"orderAction":"createOrderUI","id":"","mainOrderNo":"{}","dataSource":"UI","clientId":"04ed6e9405b34862acbf6662b5fdd297","clientCode":"UATmsy","clientName":"UAT测试公司","clientOrderNo":"${clientOrderNo}","clientOrderType":"ys28","totalWeight":"12","totalVolume":"110","totalQty":"140","declaredValue":"","cargoDesc":"","cargoPackage":"","bizType":"1","orderDate":"","planWorkloadDate":"","salesBy":"","salesName":"销售kwkw","belongCompanyCode":"PGL","belongCompanyName":"宝供物流企业集团有限公司","salesChannelCode":"","remark":"","transportMode":"QY","deliveryMethod":"SH","ftlTruckTypeCode":"","twTruckTypeCode":"","startCode":"test0701","startContact":"23","startPhone":"34","startMobile":"2343","startProvince":"110000","startCity":"110100","startCounty":"110101","startAddress":"北京地址09","startClientOrganizationCode":"test0701","endCode":"test0702","endContact":"23123312","endPhone":"12312323","endMobile":"23232323","endProvince":"330000","endCity":"330200","endCounty":"330281","endTown":"","endAddress":"广东省广州广州黄埔区南岗镇云埔工业区宝丰路168号 C D 库","endClientOrganizationCode":"test0702","warehouseBizType":"","shipperId":"","shipperCode":"","shipperName":"","warehouseId":"","warehouseName":"","warehouseAreaId":"","warehouseAreaName":"","asnNo":"","pickUpDriverName":"","pickUpDriverIdCard":"","pickUpPlateNo":"","deliveryDriverName":"","deliveryDriverIdCard":"","deliveryPlateNo":"","transportProductId":"873ac3e336204495a63ced465d9f6e58","transportProductName":"零担干线28","transportProductCode":"CUATMSYTP201910280002","warehouseProductId":"","warehouseProductName":"","warehouseProductCode":"","supplierWarehouseProductId":"","supplierWarehouseProductName":"","supplierWarehouseProductCode":"","warehoueTotalFee":"0.0000","transportTotalFee":"932.5000","supplierWarehoueTotalFee":0,"fixedQty":"","isContractPrice":"Y","isPickUp":"Y","orderPreTemplateId":"","attachmentIds":"","clientOrderId":"","startName":"","endName":"","clientSalesNo":"123120003","clientOrderDetail":[],"tbClientOrderWhInfo":[],"tbClientOrderTpInfo":[{"clientCode":"UATmsy","transportProductCode":"CUATMSYTP201910280002","transportProductName":"零担干线28","feeMainType":"2","feeSubType":"0","priceMethodCode":"WEIGHT","feeName":"附加","priceType":"重量计费","variable_name1":"重泡比:","variable_name2":"单价:","variable1":"33","variable2":"23","totalPrice":"333","variable_name3":"-:","variable3":"-","variable4":"333","jobDesc":"","transportMode":"TY","feeId":"fa78cdaaaa184200b0b2f8eb88329014","feeCode":"CUATMSYTP201910280002000013","transportProductId":"873ac3e336204495a63ced465d9f6e58","contractSignedStatus":"1"},{"clientCode":"UATmsy","transportProductCode":"CUATMSYTP201910280002","transportProductName":"零担干线28","feeMainType":"1","feeSubType":"4","priceMethodCode":"VOLUME","feeName":"零担干线费","priceType":"体积计费","variable_name1":"货量阶梯:","variable_name2":"重泡比:","variable1":"0-120","variable2":"623","totalPrice":"599.5","variable_name3":"单价:","variable3":"5.000000","variable4":"599.5","jobDesc":"","transportMode":"TY","feeId":"56130e46bd0c485993c2d6530f3ef83f","feeCode":"CUATMSYTP201910280002000002","transportProductId":"873ac3e336204495a63ced465d9f6e58","contractSignedStatus":"1"}],"extendFieldLineDetail":[{"clientCustomFieldName":"kwkw","clientCustomFieldValue":"","clientCustomFieldId":"0e2dadc65dbb456882cb5c26c15803dc","clientCode":"UATmsy"}],"tbSupplierOrderWhInfo":[]}'
# print(data)
# print(type(data))
# dd=eval(data)
# print(dd.keys())
# print(dd['orderAction'])
#

# import click
#
# @click.command()
# @click.argument('name')
# @click.option('-c', default=1, help='number of greetings')
# def hello(name, c):
#     for x in range(c):
#         click.echo('Hello %s!' % name)
#
#
#
# from __future__ import print_function
# import gevent
# from gevent import monkey
# monkey.patch_all()
# import time
# import click
# import requests
# from numpy import mean
#
#
# class statistical:
#     pass_number = 0
#     fail_number = 0
#     run_time_list = []
#
#
# def running(url, numbers):
#     for _ in range(numbers):
#         start_time = time.time()
#         r = requests.get(url)
#         if r.status_code == 200:
#             statistical.pass_number = statistical.pass_number + 1
#             print(".", end="")
#         else:
#             statistical.fail_number = statistical.fail_number + 1
#             print("F", end="")
#
#         end_time = time.time()
#         run_time = round(end_time - start_time, 4)
#         statistical.run_time_list.append(run_time)
#
#
# @click.command()
# @click.argument('url')
# @click.option('-u', default=1, help='运行用户的数量，默认 1', type=int)
# @click.option('-q', default=1, help='单个用户请求数，默认 1', type=int)
# def main(url, u, q):
#     print("请求URL: {url}".format(url=url))
#     print("用户数：{}，循环次数: {}".format(u, q))
#     print("============== Running ===================")
#
#     jobs = [gevent.spawn(running, url, q) for _url in range(u)]
#     gevent.wait(jobs)
#
#     print("\n============== Results ===================")
#     print("最大:       {} s".format(str(max(statistical.run_time_list))))
#     print("最小:       {} s".format(str(min(statistical.run_time_list))))
#     print("平均:       {} s".format(str(round(mean(statistical.run_time_list), 4))))
#     print("请求成功", statistical.pass_number)
#     print("请求失败", statistical.fail_number)
#     print("============== end ===================")

# import gevent
# from gevent import monkey
# monkey.patch_all()
# import requests
#
#
# def f(url):
#     print('GET: %s' % url)
#     resp = requests.get(url)
#     data = resp.content.decode('utf-8')
#     print('%d bytes received from %s.' % (len(data), url))
#
#
# gevent.joinall([
#     gevent.spawn(f, 'https://www.python.org/'),
#     gevent.spawn(f, 'https://www.yahoo.com/'),
#     gevent.spawn(f, 'https://github.com/'),
# ])

# import socket
# s=socket.socket()
# print(dir(s))
# host=socket.gethostname()
# port=1024
# print(host)
# s.bind((host,port))
# s.listen(5)
# while True:
#     c,addr=s.accept()
#     print('connect from :',addr)
#     c.send('连接socket')
#     c.close()


# s.connect((host,port))
# s.recv(1024)

# import cgi
# form=cgi.FieldStorage()
# name=form.getvalue('name','world')
# print('sdfsd')
# print('hello,%s!'%name)
# print(""" Content-type:text/html
# <html>
#  <head>
#   <title> Greeting Page</title>
#   </head>
#   <body>
#    <h1>hello,%s!</h1>
#
#    <form action='simple3.cgi'>
#    Change name <input type='text' name='name'/>
#    <input type='submit' />
#    </form>
#   </body>
# </html>
# """ % name)
#
# print('</p>')

from asyncore import dispatcher
import asyncore,socket

class ChatServer(dispatcher):
    def handle_accept(self):
        conn,addr=self.accept()
        print('连接',addr[0])
s=ChatServer()
s.create_socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(('',5005))
s.listen(5)
asyncore.loop()