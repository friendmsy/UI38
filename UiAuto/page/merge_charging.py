# -*- coding: utf-8 -*-
# @Time    : 2020/6/9 14:17
# @Author  : msy
# @File    : merge_charging.py
# @Software: PyCharm

from common.general import *
from config import *
from common.log import *
import time
from common.data_operate import *
from selenium.webdriver.common.keys import Keys
from page.order_page import OrderPage
from page.reconciliation import Reconciliation

# 合并计费页面类
class MergeChargingPage(BasePage):
    # 系统首页页签
    close_tab = ['xpath', '//*[@id="index_tabs"]/div[1]/div[4]/table/tbody/tr/td[3]/a/span']
    # ----------------------------------菜单
    # 订单管理模块
    order_manage_module = ['xpath', '//td[@title="订单管理"]/child::a[1]']
    # 客户拼车菜单
    customer_merge = ['xpath', '//span[text()="合并计费管理"]/parent::div[starts-with(@id,"_easyui_tree")]']

    # -------------------拼车列表
    listframe = ['xpath', '//iframe[@src="/oss/oms/TBClientOrderMargerFee/list"]']
    # 新增按钮
    add_merge_button = ['xpath', '//form[@id="TBClientOrderMargerFee_form"]/following-sibling::div/div/div/button[1]']
    # 提交
    submit = ['css', 'div.layui-layer-btn.layui-layer-btn- > a.layui-layer-btn0']
    # 查询按钮
    # carno_filter=['xpath','//*[@id="TBClientOrderCarpool_form"]/div/div[3]/div[1]/button']
    select_click = ['css', '#TBClientOrderCarpool_form > div > div:nth-child(3) > div:nth-child(1) > button']
    # 展开更多
    more_filter=['xpath','//*[@id="TBClientOrderMargerFee_queryShowHide"]/a']
    # 列表订单复选框
    merge_check_box = ['css',
                            'body > div.weadmin-body > div > div.layui-table-box > div.layui-table-fixed.layui-table-fixed-l > div.layui-table-body > table > tbody > tr:nth-child(1) > td > div']
    # 列表拼车单号 / DR单号过滤
    clientorder_margerfeeno2 = ['css', '#clientOrderMargerFeeNo']
    # 查询按钮
    select_click = ['css', '#TBClientOrderMargerFee_form > div > div:nth-child(3) > div:nth-child(1) > button']


    # -----------------------删除
    # 删除
    delete_button=['xpath', '//form[@id="TBClientOrderMargerFee_form"]/following-sibling::div/div/div/button[4]']

    # 确定删除
    accept_delete = ['xpath', '//*[starts-with(@id,"layui-layer")]/div[3]/a[1][text()="确定"]']
    # 确认弹窗提示语
    is_delete = ['xpath', '//*[starts-with(@id,"layui-layer")]/div[2]']
    # 删除失败提示语
    delete_fail_tips = ['xpath', '//*[starts-with(@id,"layui-layer")]/div[2][contains(text(),"失败")]']
    # 删除成功提示语
    delete_success_tips = ['xpath', '//*[starts-with(@id,"layui-layer")]/div[text()="删除成功"]']

    # ----------------------审核
    approval_button=['css','#audit']
    # 确定审核
    accept_approval = ['xpath', '//*[starts-with(@id,"layui-layer")]/div[3]/a[1][text()="确定"]']
    # 审核失败提示语
    approval_fail_tips = ['xpath', '//*[starts-with(@id,"layui-layer")]/div[2][contains(text(),"失败")]']
    # 审核成功提示语
    approval_success_tips = ['xpath', '//*[starts-with(@id,"layui-layer")]/div[text()="审核成功"]']


    # ------------------编辑页面
    edit_frame = ['xpath', '//iframe[starts-with(@src,"/oss/oms/TBClientOrderMargerFee/detail")]']
    # 请选择客户
    choose_customer = ['css', '#objForm > div > div:nth-child(1) > div:nth-child(1) > div > div > div > input']
    # 选择具体客户，最好要定位到具体的唯一属性而不是下标，下标是易变的，会使脚本不稳定
    choose_customer_value = ['xpath', '//form[@id="objForm"]/descendant::dd[@lay-value="UATmsy"]']
    # 输入客户单号
    customer_no = ['css', 'textarea#clientOrderNoText']
    # 获取
    load = ['css', '#objForm > div > div:nth-child(3) > button']
    # 点击获取提示语
    load_tips = ['css', '#toast-container > div > div']
    # 获取没有数据结果
    load_result = ['css',
                   '#objForm > div > div:nth-child(5) > div > div > div > div.layui-table-body.layui-table-main > div']
    # 订单全选复选框
    merge_box=['css','#objForm > div > div:nth-child(5) > div > div > div > div.layui-table-fixed.layui-table-fixed-l > div.layui-table-header > table > thead > tr > th:nth-child(1) > div']
    # 合并计费按钮
    margerfee_button= ['css','button#margerFeeButton']
    # 合并计费提示语
    margerfee_button_tips=['css', '#toast-container > div > div']
    # 拼车单号 / DR单号
    clientorder_margerfeeno=['css','#clientOrderMargerFeeNo[placeholder="拼车单号/DR单号"]']
    # 提交失败提示语,成功与失败定位的元素一样
    submit_tips=['css','div.layui-layer-content.layui-layer-padding']


    # 新增合并计费,参数是客户单号
    # custome_no 客户单号，默认不输入，自动仓储订单,要输入只能输入list
    def add_merge(self,lg='t',case=[],custome_no=[],producttype='LD',shippingcode=None,receivingcode= None,\
                  delorder_flag=None,editorder_flag=None,reconciliation=None,more_flag=None,row=None):
            # tm = pcustomer_no = get_customerno()
            tm = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))+"-"+str(row)
            # len(customer_no_list)==0 默认不输入客户单号，由订单新增方法新增整车订单，有需要也可以参数化要输入创建订单的数量
            # 登录
            # self.login(username=case[-4], password=case[-3])
            try:
                if len(custome_no)==0:
                    productlist = ['LD']
                    rcustomer_no_list = []
                    run = OrderPage()
                    no1 = run.add_order(producttype=producttype,shippingcode=shippingcode,receivingcode=receivingcode,row=row,case=case)[1]
                    # 只有创建成功的订单才加入列表
                    if no1 != 'fail':
                        rcustomer_no_list.append(no1)
                    else:
                        print('订单创建失败！不加入列表')
                    for i in productlist:
                        # 当没有传入收货地址码时，不知道为什么用第一次传入的收货地址码，只能设置传入
                        no2 = run.add_order(lg='N', producttype=i,receivingcode='test0702',row=row,case=case)[1]
                        if no2 != 'fail':
                            rcustomer_no_list.append(no2)
                        else:
                            print('订单创建失败！不加入列表')
                    # 合并订单小于两个不合并
                    if len(rcustomer_no_list) <2:
                        clientorder_margerfeeno = 'fail'
                        text = u'输入订单号小于两个，请重新输入！,订单输入个数是：{}'.format(len(rcustomer_no_list))
                        return text, clientorder_margerfeeno
                    else:
                        print(rcustomer_no_list)
                        print(len(rcustomer_no_list))
                    # 退出浏览器
                    run.quit()
                else:
                    # rcustomer_no_list = custome_no.split(',')
                    rcustomer_no_list = custome_no
                    print(rcustomer_no_list)
                # 判断是否要对账
                if reconciliation is not None:
                    # 合并单创建成功情况下才执行删除订单操作
                    try:
                        # 创建账单
                        reconciliation_text=Reconciliation().add_reconciliation(client_order_number=rcustomer_no_list,case=case,row=row)
                        if '创建对账单成功' in reconciliation_text:
                            pass
                        else:
                            print('需要创建对账单，但对账单创建失败')
                            clientorder_margerfeeno = 'fail'
                            return reconciliation_text, clientorder_margerfeeno
                    except Exception as e:
                        reconciliation_text = '创建对账单出错'
                        print('调用对账单出错！', e)
                        clientorder_margerfeeno='fail'
                        return reconciliation_text, clientorder_margerfeeno
                else:
                    print('不需要做对账单')
                if lg == 't':
                    # 登录
                    self.login(username=case[-4], password=case[-3])
                else:
                    print('不需要登录')

                # 登录
                # self.login(username=case[-4], password=case[-3])
                # 关闭所有标签
                self.click(self.close_tab[0], self.close_tab[1])
                self.click(self.close_tab[0], self.close_tab[1])
                self.click(self.close_tab[0], self.close_tab[1])
                # 一级菜单
                self.click(self.order_manage_module[0], self.order_manage_module[1])
                # 进入合并计费菜单
                self.click(self.customer_merge[0], self.customer_merge[1])
                # 进入列表
                self.in_iframe(self.listframe[0], self.listframe[1])
                time.sleep(5)
                # 点击新增按钮
                self.click(self.add_merge_button[0], self.add_merge_button[1])
                # 进入编辑框架
                self.in_iframe(self.edit_frame[0], self.edit_frame[1])
                time.sleep(5)
                # 客户
                self.click(self.choose_customer[0], self.choose_customer[1])
                time.sleep(2)
                # 选择客户
                self.click(self.choose_customer_value[0], self.choose_customer_value[1])
                time.sleep(2)
                # 输入客户单号
                for i in rcustomer_no_list:
                    self.send(self.customer_no[0], self.customer_no[1], i)
                    self.element(self.customer_no[0], self.customer_no[1]).send_keys(Keys.ENTER)
                # 点击获取
                self.click(self.load[0], self.load[1])
                self.scroll()
                # 判断订单有没有对账，是否只有零担或者特殊线路
                try:
                    if self.element(self.load_tips[0], self.load_tips[1], time=5, screenshot='f') != 'fail':
                        text2 = self.element(self.load_tips[0], self.load_tips[1]).text
                        clientorder_margerfeeno = 'fail'
                        print(text2)
                        return text2, clientorder_margerfeeno
                    else:
                        print('订单没有对账且只有零担或者特殊线路')
                except Exception as e:
                    print('出错啦！',e)
                try:
                    # 判断订单是否有效
                    if self.element(self.load_result[0], self.load_result[1], time=5, screenshot='f') != 'fail':
                        text2 = self.element(self.load_result[0], self.load_result[1]).text
                        clientorder_margerfeeno = 'fail'
                        print(text2)
                        return text2, clientorder_margerfeeno
                    else:
                        print('订单有效！')
                except Exception as e:
                    print('出错啦！',e)
                # 选择要合并的订单，全选
                self.click(self.merge_box[0],self.merge_box[1])

                # 点击合并计费按钮
                self.click(self.margerfee_button[0], self.margerfee_button[1])
                try:
                    if self.element(self.margerfee_button_tips[0], self.margerfee_button_tips[1], time=5, screenshot='f') != 'fail':
                        text3 = self.element(self.margerfee_button_tips[0], self.margerfee_button_tips[1]).text
                        clientorder_margerfeeno = 'fail'
                        print(text3)
                        return text3, clientorder_margerfeeno
                    else:
                        print('可以继续合并操作')
                except Exception as e:
                    print('出错啦！',e)
                # 输入合并单号
                self.send(self.clientorder_margerfeeno[0], self.clientorder_margerfeeno[1], tm)
                # 提交
                self.out_iframe()
                self.in_iframe(self.listframe[0],self.listframe[1])
                self.click(self.submit[0],self.submit[1])
                self.in_iframe(self.edit_frame[0], self.edit_frame[1])
                # 通过提交提示语确定是否提交成功
                if self.element(self.submit_tips[0], self.submit_tips[1], time=8,
                                screenshot='f') != 'fail':
                    text = self.element(self.submit_tips[0], self.submit_tips[1], time=8,
                                screenshot='f').text
                    clientorder_margerfeeno = tm
                else:
                    text = u'提交失败，或者捕获不到提示语'
                    clientorder_margerfeeno = 'fail'
                print(text)
                self.out_iframe()
                # self.in_iframe(self.listframe[0], self.listframe[1])
                # time.sleep(5)
                # 退出浏览器
                # self.quit()

            except Exception as e:
                clientorder_margerfeeno='fail'
                print('出错！', e)
                text = u'合并计费出错啦！'

            # delorder_flag 不为 None 时，表示要进入删除订单
            if delorder_flag is not None:
                # 合并单创建成功情况下才执行删除订单操作
                if '创建成功' in text:
                    try:
                        run1=OrderPage()
                        order_text=run1.del_order(pcustomer_no=rcustomer_no_list[0],row=row,case=case)
                    except Exception as e:
                        order_text='合并订单后删除订单出错！'
                        print('合并订单后删除订单出错！',e)

                else:
                    order_text='合并单创建失败，不进行删除订单操作！'
                    print('合并单创建失败，不进行删除订单操作！')
                return order_text,clientorder_margerfeeno
            else:
                print('不需要删除订单操作！')

                # editorder_flag 不为 None 时，表示要进入编辑订单
            if editorder_flag is not None:
                # 合并单创建成功情况下才执行删除订单操作
                if '创建成功' in text:
                    try:
                        # 创建完订单后浏览器会关闭，所以要重新登录
                        run1 = OrderPage()
                        order_text = run1.edit_order(pcustomer_no=rcustomer_no_list[0],row=row,case=case)
                    except Exception as e:
                        order_text = '合并订单后编辑订单出错！'
                        print('合并订单后编辑订单出错！', e)

                else:
                    order_text = '合并单创建失败，不进行编辑订单操作！'
                    print('合并单创建失败，不进行编辑订单操作！')
                return order_text, clientorder_margerfeeno
            else:
                print('不需要编辑订单操作！')

            # more_flag 不为 None 时，表示要再次合并
            if more_flag is not None:
                if '创建成功' in text:
                    text1, carpolling_no = self.add_merge(lg='f',custome_no=rcustomer_no_list,row=row,case=case)
                    if text1 == u'创建成功！':
                        text = u'再次合并创建成功！'
                    else:
                        text = u'再次合并计费失败！' + text1
                else:
                    print('需要再次合并，但第一次合并出错，不进行第二次合并！')

            else:
                print('不需要再次合并计费操作！')

            # 返回提交结果及合并单号
            return text, clientorder_margerfeeno

    # 删除合并计费单
    # clientorder_margerfeeno 合并单号, add_clientorder_margerfeeno 客户订单号'，默认不输入，自动创建订单
    def del_merge(self, lg='f',case=[],clientorder_margerfeeno=None, add_clientorder_margerfeeno=[],row=None):
        # 登录
        # self.login(username=case[-4], password=case[-3])
        # f 默认不输入拼车单号
        try:
            if clientorder_margerfeeno is None:
                text, clientorder_margerfeeno_no1 = self.add_merge(custome_no=add_clientorder_margerfeeno,row=row,case=case)

                if  u'创建成功！' in text:
                    print('输出',u'创建成功！' in text)
                    self.clientorder_margerfeeno_no = clientorder_margerfeeno_no1
                    print('输入的DR号是：{}'.format(self.clientorder_margerfeeno_no))
                else:
                    Mylog().my_log().error('合并失败，请输入要删除的合并单！')
                    self.text = '合并失败，请输入要删除的合并单！'
                    print(self.text)
                    return self.text

            else:
                self.clientorder_margerfeeno_no = clientorder_margerfeeno
            if lg == 't':
                # 登录
                self.login(username=case[-4], password=case[-3])
            else:
                print('不需要登录')

            # 登录
            # self.login(username=case[-4], password=case[-3])
            # 关闭所有标签
            self.click(self.close_tab[0], self.close_tab[1])
            self.click(self.close_tab[0], self.close_tab[1])
            self.click(self.close_tab[0], self.close_tab[1])
            # 一级菜单
            self.click(self.order_manage_module[0], self.order_manage_module[1])
            # 进入拼车菜单
            self.click(self.customer_merge[0], self.customer_merge[1])
            # 进入列表
            self.in_iframe(self.listframe[0], self.listframe[1])
            time.sleep(5)
            # 展开更多条件
            self.click(self.more_filter[0], self.more_filter[1])
            # 输入要过滤的拼车单号
            self.send(self.clientorder_margerfeeno2[0], self.clientorder_margerfeeno2[1], self.clientorder_margerfeeno_no)
            # 点击查询
            self.click(self.select_click[0], self.select_click[1])
            # time.sleep(5)
            # 选中合并计费单
            self.click(self.merge_check_box[0], self.merge_check_box[1])
            # time.sleep(2)
            # 删除按钮
            self.click(self.delete_button[0], self.delete_button[1])
            # time.sleep(13)
            # 确定删除
            self.click(self.accept_delete[0], self.accept_delete[1])

            # 失败与成功的弹窗不同，第一个定位完，弹窗消失，所以第二个也会定位失败,所以不能分开定位
            try:
                self.text = self.element(self.delete_fail_tips[0], self.delete_fail_tips[1], time=6).text
                print(self.text)
            except Exception:
                # 也可以考虑数据查询判断是否删除成功，并且测试删除成功的情况比失败情况少，可以暂时先这么处理
                self.text = u'删除成功'
                print(self.text)
            # 退出浏览器
            # self.quit()

        except Exception:
            self.text = u'删除合并单出错!'
        # self.quit()
        return self.text

    # 审核合并计费单
    # clientorder_margerfeeno  合并单号, add_clientorder_margerfeeno 客户订单号，默认不输入，自动创建订单
    def approval_merge(self,lg='f',case=[], clientorder_margerfeeno=None, add_clientorder_margerfeeno=[],delmerge_flag=None,row=None):
        # f 默认不输入合并单号
        try:
            if clientorder_margerfeeno is None:
                text, clientorder_margerfeeno_no1 = self.add_merge(custome_no=add_clientorder_margerfeeno,row=row,case=case)
                if  u'创建成功！' in text:
                    self.clientorder_margerfeeno_no = clientorder_margerfeeno_no1
                    print('输入的DR号是：{}'.format(self.clientorder_margerfeeno_no))
                else:
                    Mylog().my_log().error('合并失败，请输入要审核的合并单！')
                    self.text = '合并失败，请输入要审核的合并单！'
                    print(self.text)
                    return self.text
                # # 退出浏览器
                # self.quit()
            else:
                self.clientorder_margerfeeno_no = clientorder_margerfeeno
            # 登录
            if lg == 't':
                # 登录
                self.login(username=case[-4], password=case[-3])
            else:
                print('不需要登录')

            # 登录
            # self.login(username=case[-4], password=case[-3])
            # 关闭所有标签
            self.click(self.close_tab[0], self.close_tab[1])
            self.click(self.close_tab[0], self.close_tab[1])
            self.click(self.close_tab[0], self.close_tab[1])
            # 一级菜单
            self.click(self.order_manage_module[0], self.order_manage_module[1])
            # 进入拼车菜单
            self.click(self.customer_merge[0], self.customer_merge[1])
            # 进入列表
            self.in_iframe(self.listframe[0], self.listframe[1])
            time.sleep(5)
            # 展开更多条件
            self.click(self.more_filter[0], self.more_filter[1])
            # 输入要过滤的合并单号
            self.send(self.clientorder_margerfeeno2[0], self.clientorder_margerfeeno2[1], self.clientorder_margerfeeno_no)
            # 点击查询
            self.click(self.select_click[0], self.select_click[1])
            # time.sleep(5)
            # 选中合并计费单
            self.click(self.merge_check_box[0], self.merge_check_box[1])
            # time.sleep(2)
            # 审核按钮
            self.click(self.approval_button[0], self.approval_button[1])
            # time.sleep(13)
            # 确定审核
            self.click(self.accept_approval[0], self.accept_approval[1])

            # 失败与成功的弹窗不同，第一个定位完，弹窗消失，所以第二个也会定位失败,所以不能分开定位
            try:
                self.text = self.element(self.approval_fail_tips[0], self.approval_fail_tips[1], time=6,screenshot='n').text
                print(self.text)
            except Exception:
                # 也可以考虑数据查询判断是否删除成功，并且测试删除成功的情况比失败情况少，可以暂时先这么处理
                self.text = u'审核成功'
                print(self.text)
            # 退出浏览器
            # self.quit()
            self.out_iframe()
        except Exception :
            self.text = u'审核合并单出错!'
        if delmerge_flag is not None:
            # 合并单创建成功情况下才执行删除订单操作
            print('进入删除合并单16')
            if '审核成功' in self.text:
                try:
                    del_text = self.del_merge(clientorder_margerfeeno=self.clientorder_margerfeeno_no,case=case,row=row)
                    # print('进入删除合并单16177',del_text)
                except Exception as e:
                    del_text = '合并审核后删除合并单出错'
                    print('合并审核后删除合并单出错', e)

            else:
                del_text = '合并单审核失败，不进行删除合并单操作'
                print('合并单审核失败，不进行删除合并单操作')
            return del_text
        else:
            print('不需要删除合并单操作！')

        return self.text

if __name__ == '__main__':
    # list='20200629165959,20200629170140'
    run=MergeChargingPage()
    # run.add_merge()
    # run.approval_merge()
    run.del_merge()
    # text, clientorder_margerfeeno_no1 = run.add_merge(custome_no=list)
    # if clientorder_margerfeeno_no1 !='fail':
    #     run.approval_merge(clientorder_margerfeeno=clientorder_margerfeeno_no1)
    # else:
    #     print('请输入要审核的合并单号')
    # run.del_merge(clientorder_margerfeeno='1108680848')
    # run.add_merge(custome_no=list)
    # run.approval_merge(add_clientorder_margerfeeno=list)