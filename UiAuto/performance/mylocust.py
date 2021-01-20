# -*- coding: utf-8 -*-
# @Time    : 2020/12/11 10:41
# @Author  : msy
# @File    : locust.py
# @Software: PyCharm

import time
# from common.api_general import *
from common.data_operate import *
from page.api_transport_job_ticket import *
from locust import HttpUser,TaskSet,task,between,events
import queue
# from locust import User,TaskSet,task,between
# from locust import HttpLocust,TaskSet,task,between
# from page.api_transport_job_ticket import *

# 用于定义测试业务
class QuickstartUser(TaskSet):
    # count=0
    # environment.runner.quit()
    # @task()
    # 装饰该方法为一个任务。1、2
    # 表示一个Locust实例被挑选执行的权重，数值越大，执行频率越高
    # http: // localhost: 8089 /

    # @task(1)
    # def ui_login(self):
    #     BasePage.login()
    def on_start(self):
        # 如果长时间运行，同一用户只会运行一次，不会因为用户循环运行也多次执行
        print('每一个用户初始化')
    def test1(self):
        print('test1')
    def test2(self):
        print('test2')

    # 没有task 装饰的方法不会当作一个行为，不会被直接运行，但可以被调用
    # @task(1)
    # def test3(self):
    #     print('test3')

    # @task(1)
    def test_api_login(self):
        # r = self.client.get('/login/ajaxDoLogin',data={"username": "sybmsy", "password": "12345678", "captchaCode": "8888"},catch_response = True)
        with self.client.post('/login/ajaxDoLogin',data={"username": "sybmsy", "password": "12345678", "captchaCode": "8888"},catch_response=True) as r:
            print(r.content.decode('utf-8'))
            content = eval(r.content.decode('utf-8'))
            # 对200状态进行断言
            if r.status_code == 200:
                if '登录成功' in content['msg']:
                    r.success()
                    pass
                else:
                    r.failure("Got wrong response")
            else:
                pass

    @task(1)
    # 定义行为
    def transport_job(self):
        try:
            # 取数
            subno = self.user.q.get()
            # 取出来后又推进行，达到循环的目的
            self.user.q.put(subno)
            tm, dit = TransportJobTicket().operate_job(list=subno,nojob='nojob')
            # 不用with方式似乎有问题
            with self.client.post(
                    '/api/service?method=pgl.erp.api.oms.jobOrderTp.add&appCode=pgl-erp-oss-oms&companyCode=PGLKY&timestamp={}&version=1.0&sign=M2f8gkzZEzMKPgq&departCode=PGLKY03'.format( tm),json=dit, catch_response=True) as r:
                print(r.content.decode('utf-8'))
                content = eval(r.content.decode('utf-8'))
                if r.status_code == 200:
                    if '创建成功' in content['msg']:
                        r.success()
                        pass
                    else:
                        r.failure("Got wrong response")
                else:
                    pass
        except Exception as e:
            print(e)
    def on_stop(self):
        print('每一个用户结束')

# 模拟用户
class WebsiteUser(HttpUser):
# class WebsiteUser(HttpLocust):
#     名称一定是tasks，否则找不到任务！！！！！
    tasks=[QuickstartUser]
    host='https://uaterp.pgl-world.com.cn'
    q=queue.Queue(maxsize=0)
    # _task_queue=queue.Queue(maxsize=0)
    data=DataOperate().excel_operat(filepath=os.path.join(FILE,'subno.xlsx'))
    print(data)
    for i in data:
        q.put(i)
        # _task_queue.put(i)
    # self.q=Queue.queue(maxsize=0)
    # min_time=2000
    # max_time=5000
    # wait_time = between(1, 3)

if __name__ == "__main__":
    # os.system("locust -f E:\\software\\Python3.8.3\\UiAuto\\performance\\mylocust.py")
    os.system("locust -f E:\\software\\Python3.8.3\\UiAuto\\performance\\mylocust.py --headless -u2 -r1 -t15")
    # locust - f ** **.py - -csv = onetest - -host = http: // 0.0 .0.0: 0000 --no-web -c10 -r10 -t2
    # （PS：-f # 指定运行的py文件的名字，--csv  生成报告的名字，--host  测试的http服务的ip和port，headless不用web启动，
    # -u 设置虚拟用户数， -r 设置每秒启动虚拟用户数， -t 设置运行时间，如果不设置no web模式，启动后要在浏览器打开http://localhost:8089/，
    # 即可输入虚拟用户数和每秒启动虚拟用户数，并有可视化的界面结果查看）
    # wait_time属性
    # 用户wait_time方法是一种可选功能，用于使模拟用户在任务执行之间等待指定的时间。
    # 内置了三个等待时间功能：
    # constant
    # 在固定的时间内
    # between
    # 在最大值和最小值之间的随机时间
    # constant_pacing
    # 自适应时间，以确保任务每X秒（最多）运行一次
    # import os
    # locust - f
    # E:\software\Python3.8.3\UiAuto\performance\locust.py - -host = https://uaterp.pgl-world.com.cn
    # os.system("locust -f E:\\software\\Python3.8.3\\UiAuto\\performance\\mylocust.py --host=https://uaterp.pgl-world.com.cn")
    print(DataOperate().excel_operat(filepath=os.path.join(FILE,'subno.xlsx'),col=[1,3],row=[1,3]))


