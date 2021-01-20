#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/5/6 10:43
# @Author : msy

from config import *
import json

from common.data_operate import *
from common.log import *
from page.order_page import *
from page.merge_charging import *
from page.carpooling import *
from page.receivable import *


class RunCase():
    # rerun：是否重跑用例
    def find_case(self,rerun=None,filepathnext='备份'):

        if os.path.isdir(CASEPATH): # 判断是否是一个目录，传入的是指定的用例目录，如果要修改用例文件，修改config配置的casepath就可以
            self.fc = []   #定义一个列表，保存每个用例后面加入文件名的用例
            dataoperate = DataOperate()
            for f in os.listdir(CASEPATH):  # 遍历用例
                if os.path.isfile(os.path.join(CASEPATH, f)):
                    # l = f.split('.')
                    # print(f, l)
                    # 只能是excel格式的用例,可以用os.path.splittext(f)[1] 获取后缀
                    if f.split('.')[-1] == 'xlsx':
                        # 不复制，先不覆盖
                        self.copyfile = dataoperate.copy_excel(dirpath=CASEPATH, filepath=os.path.join(CASEPATH, f),
                                                               filepathnext=filepathnext, iscopy='nocopy')
                        # PO模式不适用，接口自动化适用
                        # self.mc = BasePage(WEBBROSER)
                        if rerun is None:
                            # 删除测试报告目录的文件
                            dataoperate.delete_file()
                            # REPORTPATH_ALLURE 目录的文件也删除
                            dataoperate.delete_file(dirpath=REPORTPATH_ALLURE)
                            # 用例目录下的文件夹是用例副本，要先删除才能确定不会把之前的用例副本发送到邮箱
                            for j in os.listdir(CASEPATH):
                                if os.path.isdir(os.path.join(CASEPATH, j)):
                                    shutil.rmtree(os.path.join(CASEPATH, j))
                                else:
                                    pass
                            # 目前是复制副本时不走创建副本分支，怀疑是删除与创建间隔时间太短，导致前后不稳定，另外一种可能是创建副本代码不稳定
                            time.sleep(3)
                            # 创建用例副本
                            copyfile = dataoperate.copy_excel(dirpath=CASEPATH, filepath=os.path.join(CASEPATH, f),
                                                              filepathnext=filepathnext)
                            self.copyfile = copyfile
                            self.allcase = dataoperate.get_case(file=os.path.join(CASEPATH, f), rerun=rerun)
                        # 如果是获取重跑的，则去副本里面取，因为结果写在副本
                        else:
                            # 重跑不能删除之前的用例结果，也不能删除测试报告
                            if self.copyfile=='path_not_exits':
                                self.fc = ['0']
                                print('打印用例！', self.fc)
                                return self.fc
                            else:
                                self.allcase = dataoperate.get_case(file=self.copyfile, rerun=rerun)

                        print(self.allcase)
                        # 第一个是1代码没有要执行的用例
                        if self.allcase[0] != '1':
                            for c in self.allcase:
                                # 向每个用例添加文件名,用于写入时定位文件名
                                # c.append(self.f)
                                c.append(self.copyfile)
                                # c.append(self.mc)
                                self.fc.append(c)
                        else:
                            self.fc = ['1']
                else:
                    Mylog().my_log().error('文件类型是：%s,不是用例文件!',f)
        else:
            raise Exception('用例文件不存在')
        print('打印用例！',self.fc)
        # print('打印用例类型！',type(self.fc))
        return self.fc

    # case：用例列表
    def run_case(self,case):
        try:
            # 订单模块
            if case[3] == 'order':
                # case[5]是判断是有参数输入，'/'表示没有
                # 新增订单
                if case[4] == 'add_order':
                    if case[5] == '/':
                        text, rpcustomer_no,rdict = OrderPage().add_order(case=case,row=case[-2])
                    else:
                        # 使用json.loads转换时，None也要用引号，否则转换失败
                        # （除数字类型的不用引号，其他字符要用引号），但是eval不要求括起来
                        param=eval(case[5])
                        text,rpcustomer_no,rdict=OrderPage().add_order(case=case,lg=param['lg'],producttype=param['producttype'],\
                                                                 pcustomer_sales_no =param['pcustomer_sales_no'],\
                                                                 pcustomer_no= param['pcustomer_no'],pweight=param['pweight'],\
                                                                 pvolume=param['pvolume'],pquantity=param['pquantity'],\
                                                                 complete_vehicle_quality=param['complete_vehicle_quality'],\
                                                                 shippingcode=param['shippingcode'],receivingcode=param['receivingcode'],row=case[-2])
                        print(text,rpcustomer_no)
                        # return
                # 编辑订单
                elif case[4] == 'edit_order':
                    # print('进入编辑')
                    text=OrderPage().edit_order(case=case,row=case[-2]) if case[5] == '/' else print(2)
                    print('打印编辑返回结果',text)
                # 删除订单
                elif case[4] == 'del_order':
                    text=OrderPage().del_order(case=case,row=case[-2]) if case[5] == '/' else print(3)
                # 订单上传
                elif case[4] == 'order_upload':
                    if case[5] == '/':
                        resultlist = OrderPage().order_upload(case=case)
                        text = resultlist[0]
                    else:
                        param = eval(case[5])
                        resultlist = OrderPage().order_upload(case=case,copydata=param['copydata'])
                        text = resultlist[0]
                # 订单下载
                elif case[4] == 'order_download':
                    text=OrderPage().order_download(case=case) if case[5] == '/' else print(4)

                elif case[4] == 'import_edit':
                    if case[5] == '/':
                        resultlist=OrderPage().import_edit(case=case,row=case[-2])
                        text = resultlist[0]
                    else:
                        param = eval(case[5])
                        resultlist = OrderPage().import_edit(case=case, copydata=param['copydata'],row=case[-2],datasource=param['datasource'])
                        text = resultlist[0]
                else:
                    print('不是order对象')

            # 合并模块
            elif case[3] == 'merge':
                # case[5]是判断是有参数输入，'/'表示没有
                # 新增合并单
                if case[4] == 'add_merge':
                    if case[5] == '/':
                        text, rpcustomer_no = MergeChargingPage().add_merge(case=case,row=case[-2])
                    else:
                        param = eval(case[5])
                        text, rpcustomer_no = MergeChargingPage().add_merge(case=case,custome_no=param['custome_no'],\
                                                                            producttype=param['producttype'],\
                                                                            shippingcode=param['shippingcode'],\
                                                                            receivingcode=param['receivingcode'],\
                                                                            delorder_flag=param['delorder_flag'],\
                                                                            editorder_flag=param['editorder_flag'],\
                                                                            reconciliation=param['reconciliation'],\
                                                                            more_flag=param['more_flag'],row=case[-2])
                # 审核合并单
                elif case[4] == 'approval_merge':
                    # print('进入编辑')
                    if case[5] == '/':
                        text = MergeChargingPage().approval_merge(case=case,row=case[-2])
                    else:
                        param = eval(case[5])
                        text = MergeChargingPage().approval_merge(case=case,clientorder_margerfeeno=param['clientorder_margerfeeno'],\
                                                                  add_clientorder_margerfeeno=param['add_clientorder_margerfeeno'],\
                                                                  delmerge_flag=param['delmerge_flag'],row=case[-2])
                        print('是否有删除标志',param['delmerge_flag'])
                    # print('打印编辑返回结果',text)
                # 删除合并单
                elif case[4] == 'del_merge':
                    text=MergeChargingPage().del_merge(case=case,row=case[-2]) if case[5] == '/' else print(3)

                else:
                    print('不是merge对象')


            # 拼车模块
            elif case[3] == 'carpoolling':
                # case[5]是判断是有参数输入，'/'表示没有
                # 新增合并单
                if case[4] == 'add_carpoolling':
                    if case[5] == '/':
                        text, rpcustomer_no = CarpoolingPage().add_carpooling(case=case,row=case[-2])
                    else:
                        param = eval(case[5])
                        text, rpcustomer_no = CarpoolingPage().add_carpooling(case=case,customer_no_list=param['customer_no_list'],producttype=param['producttype'],\
                                                                              pick_number=param['pick_number'],pick_pice=param['pick_pice'],\
                                                                              delivery_number=param['delivery_number'],delivery_pice=param['delivery_pice'],\
                                                                              complete_vehicle_quality=param['complete_vehicle_quality'],delorder_flag=param['delorder_flag'],\
                                                                              editorder_flag=param['editorder_flag'],reconciliation=param['reconciliation'],\
                                                                              more_flag=param['more_flag'],row=case[-2])
                # 审核拼车单
                elif case[4] == 'approval_carpoolling':

                    if case[5] == '/':
                        text = CarpoolingPage().approval_carpoolling(case=case,row=case[-2])
                    else:
                        param = eval(case[5])
                        text = CarpoolingPage().approval_carpoolling(case=case,clientorder_carpoollingfeeno=param['clientorder_carpoollingfeeno'],\
                                                                     add_clientorder_carpoollingfeeno=param['add_clientorder_carpoollingfeeno'],\
                                                                     delcarpooling_flag=param['delcarpooling_flag'],row=case[-2])

                # 删除拼车单
                elif case[4] == 'del_carpooling':
                    if case[5] == '/':
                        text = CarpoolingPage().del_carpooling(case=case,row=case[-2])
                    else:
                        param = eval(case[5])
                        text = CarpoolingPage().del_carpooling(case=case,carpooling_no=param['carpooling_no'], add_carpooling_no=param['add_carpooling_no'],row=case[-2])


                # 编辑拼车单
                elif case[4] == 'edit_carpooling':
                    if case[5] == '/':
                        text = CarpoolingPage().edit_carpooling(case=case,row=case[-2])
                    else:
                        param = eval(case[5])
                        text = CarpoolingPage().edit_carpooling(case=case,carpooling_no=param['carpooling_no'], add_carpooling_no=param['add_carpooling_no'],row=case[-2])
                else:
                    print('不是carpoolling对象')
            elif case[3]=='receivalble':
                if case[4] == 'compare_cost':
                    if case[5] == '/':
                        text= Receivalble().compare_cost(case=case,row=case[-2])
                    else:
                        param = eval(case[5])
                        text= Receivalble().compare_cost(case=case,customerno=param['customerno'],merge=param['merge'],carpooling=param['carpooling'],row=case[-2])
                else:
                    print('不是receivalble对象')

            else:
                print('输入的page出错！')
                result = '0'
                return result
            # 由于case[7]用[]及不用[]括起来，读取到的都是str类型，如果没有[]，如eval转换会出错，所以通过[开头区分是否用eval转换数据
            if case[7].startswith('['):
                expectresult = eval(case[7])
            else:
                expectresult = case[7]
            print(len(text),len(expectresult),type(text),type(expectresult),text,expectresult)
            # 判断是否为str,是str，说明只有一个字段要断言
            if isinstance(expectresult,str):
                if isinstance(text,str):
                    # 如果返回的text也是str,则可以进行对比
                    if expectresult in text:
                        # 要返回result,目的是用于断言
                        # case[-2] 取倒数第二个，case[-1]取倒数第一个
                        result = '1'
                    else:
                        result = '0'
                else:
                    print('返回的结果与预期结果对比个数不一致',len(text),len(expectresult),text,expectresult)
                    result = '2'
            elif isinstance(expectresult,list):
                if isinstance(text,list):
                    result = '1'
                    for i,k in zip(expectresult,text):
                        if i in k:
                            result = '0'
                            break
                        else:
                            pass
                else:
                    print('返回的结果与预期结果对比个数不一致')
                    result = '3'
            else:
                print('返回的结果不是列表与不是字符串，对比失败')
                result = '4'
            DataOperate().write_result(case[-2], text, result, case[-1])
            print('回写完成')

        except Exception as e:
            print('运行用例出错啦！',e)
            result='0'
        print(result)
        # 返回result,用于断言
        return result




#方法调试
if __name__ == '__main__':

    runc = RunCase()
    list=runc.find_case()
    # mycase=BasePage(WEBBROSER)
    # mycase.login(URL)
    # runc.run_case(list,mycase)
    # # print(list[1][1])
    # # print(list[1][5])
    # # print('下面获取cookies')
    # cookies=mc.get_cookies(list[1][1],list[1][5])
    # print('打印返回的cookies',(cookies,type(cookies)))
    # for c in list:
    #
    #
    #     result=runc.run_case(c)
    #     print('打印最终返回的结果',result)

    #2020/03/04
    # runc = RunCase()
    # list=runc.find_case()
    # mc=MyCase()
    # print(list[1][1])
    # print(list[1][5])
    # print('下面获取cookies')
    # mc.get_cookies(list[1][1],list[1][5])