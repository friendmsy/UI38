# -*- coding: utf-8 -*-
# @Time    : 2020/10/9 16:53
# @Author  : msy
# @File    : commethod.py
# @Software: PyCharm
import  time

# yield 是生成器，占用内存比列表小，内存只保留调用到的，前面的不保留
# 订单EXCEL批量修改订单号
# n边界是不取的，但m 的边界会取

# m：开始,n：结束,k：步长
def rangeyield(m,n,k=1):
    for i in range(m,n,k):
        yield i
# 从开始，m ：结束，能取到下限，不能取到上限
def rangeyield2(m):
    for i in range(m):
        yield i

# sequese:序列
def beyield(sequese):
    for i in sequese:
        yield i

import threading
# class MyThread(threading.Thread):
#     """重写多线程，使其能够返回值"""
#     def __init__(self, target=None, args=()):
#         super(MyThread, self).__init__()
#         self.func = target
#         self.args = args
#
#
#     def run(self):
#         self.result = self.func(*self.args)
#         # return self.result
#
#
#     def get_result(self):
#         try:
#             self.result = self.func(*self.args)
#             return self.result  # 如果子线程不使用join方法，此处可能会报没有self.result的错误
#         except Exception:
#             return None

def set_func(func):
    # num=[0]
    num=0
    def call_func():
        # 使用列表则不需要使用nonlocal ,　使用列表的id不会变，使用int 列表id(地址)会变，
        # 另外，只有第一次运行会跑到外部变量中，后面再运行函数不执行外部变量的赋值；
        # 通过使用int外部变量打开的id看出，内部函数对外部函数操作后，变量会改变地址，
        # 后面执行时使用的是上一次操作变量后保存的地址；这就达到了统计函数运行次数的
        # 目的（要配合装饰品使用，不然直接调用也达不到效果）
#        global a#在这里会报错，因为global定义的是全局变量
# 　　　　nonlocal a#在这里使用nonlocal是对上一级的修改
# 　　　　a+=1#不能对全局变量进行修改
        nonlocal num
        # customerno=func()
        # 统计函数执行次数
        # num[0]+=1
        num+=1
        # 订单号+执行次数，解决多线程多进程订单号重复问题  --后续，用pytest -n2 运行用例仍有问题，
        # 仍会重复，但是代码调试是不重复的
        # customerno=str(int(func())+num[0])
        customerno=str(int(func())+num)
        return customerno
    return call_func

@set_func
def get_customerno():
    pcustomer_no = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
    return pcustomer_no





from multiprocessing import Lock,Process
# 进程
# get_customerno()
# get_customerno()
# get_customerno()
# P1=Process(target=get_customerno())
# P2=Process(target=get_customerno())
# P3=Process(target=get_customerno())

# 线程
# P1=threading.Thread(target=get_customerno())
# P2=threading.Thread(target=get_customerno())
# P3=threading.Thread(target=get_customerno())
# P1.start()
# P2.start()
# P3.start()
# print(get_customerno())

# def set_func1():
#     num=[0]
#     # print("id",id(num))
#     # print("id",num)
#     def call_func():
#         # customerno=func()
#         pcustomer_no = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
#         # 统计函数执行次数
#         num[0]+=1
#         print('执行次数',num[0])
#         # 订单号+执行次数，解决多线程多进程订单号重复问题
#         customerno=str(int(pcustomer_no)+num[0])
#         print(customerno)
#         return customerno
#     return call_func

# s1=set_func1()
# s2=set_func1()
# s3=set_func1()
# # s1()
# # s2()
# # s3()
# P1=Process(target=s1())
# P2=Process(target=s2())
# P3=Process(target=s3())


# def f1():
#     print("in  f1..")
#     num=111
#     def f2():
#         nonlocal num
#         num=222
#         print(num)
#     f2()
#     print(num)
# f1()
# f1()
# f1()