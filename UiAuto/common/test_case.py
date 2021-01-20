#!/usr/bin/env python

# @Time : 2020/5/6 10:42
# @Author : msy

import unittest
# from common.log import *
import pytest

from common.run_case import *
from ddt import ddt, data, unpack
# import allure
from common.send_email import *
# from common.commethod import MyThread
# import threading
# from multiprocessing import Lock,Process

@ddt
# @pytest.mark.demo
class Test_case(unittest.TestCase):
    case='0'

    def setUp(self):
        # pass
        print("测试用例开始！")
    fc = RunCase().find_case()
    # @allure.description('msy描述')
    # @allure.step('msy步骤')
    # @pytest.mark.flaky(reruns=5)
    # @pytest.mark.run(order=2)
    # @pytest.fixture()
    @data(*fc)
    def test_1(self, args):
        def test_1_1():
            if args != '1' and args != '0':
                print(args)
                print(type(args))
                print(args[11])
                result = RunCase().run_case(args)
                self.assertEqual('1', result) if result != '' else print('用例执行出错！')

            else:
                print('没有用例')
                # result='1'
                # self.assertEqual('1', result)
        test_1_1()

    '''
    parallel 重跑时，可用线程多于用例时有可能会提前跑，导致不准确
    # @unittest.skipUnless(case=='no',u"case为'no',表示重跑用例为0，用例跳过")
    def test_2_rerun1(self):
        # 第一次重跑
        f = RunCase().find_case(rerun='y')
        print('进入用例执行66666')

        # @data(*f)
        for args in f:
            if args !='1' and args!='0':
                print('打打打',args)
                result = RunCase().run_case(args)
                print('第一次重跑8888')
                self.assertEqual('1', result) if result != '' else print('用例执行出错！')
                print('第一次重跑结束')
            elif args == '0':
                print('重跑获取用例出错，没有用例副本文件！')

                self.assertEqual('1', '0')

            else:
                # print(args)
                print('第一次重跑111，没有要重跑用例')
                # self.case='no'
                # result = '1'
                # self.assertEqual('1', result)
        # test_2_1()

    '''
    '''
    # @unittest.skipUnless(status==0,u"状态码为0,表示重跑用例为0，用例跳过")
    def test_3_rerun2(self):
        # 第二次重跑
        ff = RunCase().find_case(rerun='y')
        print('55555')
        # @data(*ff)
        for args in ff:
            if args !='1' and args!='0':
                result = RunCase().run_case(args)
                print('第二次重跑9999')
                self.assertEqual('1', result) if result != '' else print('用例执行出错！')
                print('第二次重跑结束')
            elif args == '0':
                print('重跑获取用例出错，没有用例副本文件！')
                self.assertEqual('1', '0')
            else:
                print('第二次重跑2222，没有要重跑用例')
                # self.status=0
                # result = '1'
                # self.assertEqual('1', result)
    '''
    '''
    def test_4(self):
        filelist = []
        # 把报告加入到列表
        reportfiles = os.listdir(REPORTPATH)
        if len(reportfiles) > 0:
            for f in reportfiles:
                # print(f)
                # 文件和删除目录的方式不一样，所以需要分开操作
                if os.path.isfile(os.path.join(REPORTPATH, f)):
                    filelist.append(os.path.join(REPORTPATH, f))
                else:
                    pass
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
        # 添加到邮件的附件
        send_email(filepath=filelist)

    '''

    # thread[index] = threading.Thread(self.test1, args=(args,))
    # @unittest.skip('跳过用例,不需要清理恢复')    ,#这个不能跳过，跳过会导致所有用例不能执行
    def tearDown(self):
        print("测试用例结束")
        Mylog().my_log().info('测试用例结束')

