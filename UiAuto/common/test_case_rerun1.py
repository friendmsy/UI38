#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/5/6 10:42
# @Author : msy

import unittest
# from common.log import *
import pytest
import flaky
from common.run_case import *
from ddt import ddt, data, unpack


@ddt
# @pytest.mark.demo
class Test_rerun1(unittest.TestCase):

    def setUp(self):
        # pass
        print("测试用例开始！")
        # Mylog().my_log().info('测试用例开始')
        # print(self.fc)
    # 第一次重跑
    f = RunCase().find_case(rerun='y')
    print('进入用例执行')
    # @pytest.mark.run(order=2)
    @data(*f)
    def test_2(self,args):
        if args != '1':
            result = RunCase().run_case(args)
            self.assertEqual('1', result) if result != '' else print('用例执行出错！')
        else:
            # print(args)
            print('第一次重跑111，没有要重跑用例')
            # result = '1'
            # self.assertEqual('1', result)



    # @unittest.skip('跳过用例,不需要清理恢复')
    def tearDown(self):
        print("测试用例结束")
        Mylog().my_log().info('测试用例结束')
