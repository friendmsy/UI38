# -*- coding: utf-8 -*-
# @Time    : 2020/5/20 9:55
# @Author  : msy
# @File    : carpooling.py
# @Software: PyCharm

from common.general import *
from config import *
from common.log import *
import time
from common.data_operate import *
from selenium.webdriver.common.keys import Keys
from page.order_page import OrderPage
from page.reconciliation import Reconciliation

# 拼车页面类
class CarpoolingPage(BasePage):

    # 系统首页页签
    close_tab = ['xpath', '//*[@id="index_tabs"]/div[1]/div[4]/table/tbody/tr/td[3]/a/span']
    # ----------------------------------菜单
    # 订单管理模块
    order_manage_module = ['xpath', '//td[@title="订单管理"]/child::a[1]']
    # 客户拼车菜单
    customer_carpooling = ['xpath', '//span[text()="客户拼车"]/parent::div[starts-with(@id,"_easyui_tree")]']

    # -------------------拼车列表
    listframe = ['xpath', '//iframe[@src="/oss/oms/TBClientOrderCarpool/list"]']
    # 新增按钮
    add_carpooling_button = ['css', 'button#create']
    # 提交
    submit = ['css', 'div.layui-layer-btn.layui-layer-btn- > a.layui-layer-btn0']
    # 拼车单号查询
    carpoolNo=['css','#carpoolNo']
    # 查询按钮
    # carno_filter=['xpath','//*[@id="TBClientOrderCarpool_form"]/div/div[3]/div[1]/button']
    select_click = ['css', '#TBClientOrderCarpool_form > div > div:nth-child(3) > div:nth-child(1) > button']
    # 列表订单复选框
    carpooling_check_box = ['css',
                       'body > div.weadmin-body > div > div.layui-table-box > div.layui-table-fixed.layui-table-fixed-l > \
                       div.layui-table-body > table > tbody > tr > td > div > div > i']
    list_carpooling_no = ['xpath','/html/body/div[2]/div/div[2]/div[2]/table/tbody/tr[1]/td[3]/div[text()="20200607110752"]']

    # ----------------------审核
    approval_button = ['css', '#audit']
    # 确定审核
    accept_approval = ['xpath', '//*[starts-with(@id,"layui-layer")]/div[3]/a[1][text()="确定"]']
    # 审核失败提示语
    approval_fail_tips = ['xpath', '//*[starts-with(@id,"layui-layer")]/div[2][contains(text(),"失败")]']
    # 审核成功提示语
    approval_success_tips = ['xpath', '//*[starts-with(@id,"layui-layer")]/div[text()="审核成功"]']

    #-------------------- 删除
    # 删除按钮
    delete_button = ['css', '#remove']
    # 确定删除
    accept_delete = ['xpath', '//*[starts-with(@id,"layui-layer")]/div[3]/a[1][text()="确定"]']
    # 确认弹窗提示语
    is_delete = ['xpath', '//*[starts-with(@id,"layui-layer")]/div[2]']
    # 删除失败提示语
    delete_fail_tips = ['xpath', '//*[starts-with(@id,"layui-layer")]/div[2][contains(text(),"失败")]']
    # 删除成功提示语
    delete_success_tips = ['xpath', '//*[starts-with(@id,"layui-layer")]/div[text()="删除成功！"]']

    # ------------------------编辑
    # 编辑按钮
    # 编辑
    update = ['css', '#update']
    # 拼车总费用
    totalfee=['xpath','//*[@id="carpoolTotalFee"]']


    # -------------------新增页面
    # 编辑页面列表
    edit_frame = ['xpath', '//iframe[starts-with(@src,"/oss/oms/TBClientOrderCarpool/detail")]']
    # 请选择客户
    choose_customer=['css','#objForm > div > div:nth-child(1) > div:nth-child(1) > div > div > div > input']
    # 选择具体客户
    choose_customer_value=['xpath', '//form[@id="objForm"]/descendant::dd[@lay-value="UATmsy"]']
    # 输入客户单号
    customer_no=['css','textarea#clientOrderNoText']
    # 是否运作
    is_operate=['css','#objForm > div > div:nth-child(2) > button:nth-child(2)']
    # # 是否运作结果提示
    # operate_tips=['css','#toast-container > div > div']
    # close_operate_tips=['css','#toast-container > div > button']
    # 获取
    load=['css','#objForm > div > div:nth-child(2) > button']
    # 点击获取提示语
    load_tips=['css','#toast-container > div > div']
    # 获取没有数据结果
    load_result=['css','#objForm > div > div:nth-child(4) > div > div > div > div.layui-table-body.layui-table-main > div']
    # 提货点数
    pick_number=['css','input#pickUpPoint']
    # 提货点单价
    pick_pice=['css','input#pickUpPointPrice']
    # 送货点数
    delivery_number = ['css', 'input#deliveryPoint']
    # 送货点单价
    delivery_pice = ['css', 'input#deliveryPointPrice']
    # 产品下拉框
    product=['css','#objForm > div > div:nth-child(6) > div:nth-child(1) > div:nth-child(2) > div > div > input']
    # 选择第整车0401产品
    product_value=['xpath','//*[@id="objForm"]/div/div[6]/div[1]/div[1]/div/dl/dd[@lay-value="CUATMSYTP202001060001"]']
    # 始发线路
    line_start_choose=['css','#objForm > div > div:nth-child(6) > div:nth-child(1) > div:nth-child(4) > div > div > input']
    line_start_value=['css','#objForm > div > div:nth-child(6) > div:nth-child(1) > div:nth-child(4) > div > dl > dd:nth-child(2)']
    # 到达线路
    line_end_choose=['css','#objForm > div > div:nth-child(6) > div:nth-child(1) > div:nth-child(6) > div > div > input']
    line_end_value=['css','#objForm > div > div:nth-child(6) > div:nth-child(1) > div:nth-child(6) > div > dl > dd:nth-child(2)']
    # 拼车单号
    carpooling_no=['css','#objForm > div > div:nth-child(6) > div:nth-child(1) > div:nth-child(8)>input']
    # 新增车型
    choose_cartype_button=['css','#objForm > div > div:nth-child(6) > div:nth-child(2) > button']
    chosse_cartype=['xpath','//*[starts-with(@id,"eleven")]/th[3]/div/div/input']
    chosse_cartype_value=['xpath','//*[starts-with(@id,"eleven")]/th[3]/div/dl/dd[2]']
    # 数量
    car_number=['xpath','//*[starts-with(@id,"fixedQty")]']
    submit=['xpath','//*[starts-with(@id,"layui-layer")]/div/a[text()="提交"]']
    submit_tips=['xpath','//*[starts-with(@id,"layui-layer")]/div[2]']
    price=['xpath','//*[@id="eleven_0"]/th[6]']
    # 更新提交结果
    submit_tips2=['xpath','//*[starts-with(@id,"layui-layer")]/div[contains(text(),"！")]']

    # 新增拼车
    # customer_no_list  客户订单号（列表）, pick_number 提货点数, pick_pice 提货单价,
    # delivery_number 送货点数, delivery_pice送货单价, carpolling_num 拼车单号
    def add_carpooling(self,lg='t',case=[],customer_no_list=[],producttype='ZC',pick_number='1',pick_pice='1',delivery_number='1',delivery_pice='1',\
                       complete_vehicle_quality='1',delorder_flag=None,editorder_flag=None,reconciliation=None,more_flag=None,row=None):
        # tm=get_customerno()
        tm=time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))+"-"+str(row)
        # len(customer_no_list)==0 默认不输入客户单号，由订单新增方法新增整车订单，有需要也可以参数化要输入创建订单的数量
        try:
            if len(customer_no_list)==0:
                productlist=['ZC']
                rcustomer_no_list = []
                run = OrderPage()
                no1=run.add_order(producttype=producttype,row=row,case=case)[1]
                # 只有创建成功的订单才加入列表
                if no1!='fail':
                    rcustomer_no_list.append(no1)
                else:
                    print('订单创建失败！不加入列表')
                for i in productlist:
                    no2=run.add_order(lg='N',producttype=i,row=row,case=case)[1]
                    if no2 != 'fail':
                        rcustomer_no_list.append(no2)
                    else:
                        print('订单创建失败！不加入列表')
                # 小于两个不拼车
                if len(rcustomer_no_list)<2:
                    carpolling_no = 'fail'
                    text=u'输入订单号小于两个，请重新输入！,订单输入个数是：{}'.format(len(rcustomer_no_list))
                    return text,carpolling_no
                else:
                    print(rcustomer_no_list)
                    print(len(rcustomer_no_list))
            else:
                rcustomer_no_list=customer_no_list
                print(rcustomer_no_list)
                print(type(rcustomer_no_list))

            # 判断是否要对账
            if reconciliation is not None:
                # 合并单创建成功情况下才执行删除订单操作
                try:
                    # 创建账单
                    reconciliation_text = Reconciliation().add_reconciliation(client_order_number=rcustomer_no_list,case=case)
                    if '创建对账单成功' in reconciliation_text:
                        pass
                    else:
                        print('需要创建对账单，但对账单创建失败')
                        carpolling_no = 'fail'
                        return reconciliation_text, carpolling_no
                except Exception as e:
                    reconciliation_text = '创建对账单出错'
                    print('调用对账单出错！', e)
                    carpolling_no = 'fail'
                    return reconciliation_text, carpolling_no
            else:
                print('不需要做对账单')

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
            self.click(self.customer_carpooling[0], self.customer_carpooling[1])
            # 进入列表
            self.in_iframe(self.listframe[0], self.listframe[1])
            time.sleep(5)
            # 点击新增按钮
            self.click(self.add_carpooling_button[0], self.add_carpooling_button[1])
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
            # # 查询是否运运作按钮
            # self.click(self.is_operate[0],self.is_operate[1])
            # # 判断获取后有弹窗
            # if self.element(self.operate_tips[0],self.operate_tips[1],screenshot='n')!='fail':
            #     print('点击获取后有弹窗')
            #     text1=self.element(self.operate_tips[0], self.operate_tips[1], screenshot='n').text
            #     carpolling_no = 'fail'
            #     return text1, carpolling_no
            # else:
            #     pass
            #
            # self.click(self.close_operate_tips[0],self.close_operate_tips[1])
            # 目的是防止后面获取太快，仍时定位到上面的提示语
            # time.sleep(3)
            # 点击获取
            self.click(self.load[0], self.load[1])
            self.scroll()
            # 判断是否仓+运或者是否存在不同产品
            try:

                if self.element(self.load_tips[0], self.load_tips[1],time=5,screenshot='f')!= 'fail':
                    # print('点击获取出现弹窗')
                    text2 = self.element(self.load_tips[0], self.load_tips[1]).text
                    carpolling_no = 'fail'
                    print(text2)
                    return text2,carpolling_no
                else:
                    pass
            except Exception as e:
                print('出错啦！',e)
            try:
                # 判断订单是否有效
                if self.element(self.load_result[0], self.load_result[1],time=5,screenshot='f')!= 'fail':
                    text2 = self.element(self.load_result[0], self.load_result[1]).text
                    carpolling_no = 'fail'
                    print(text2)
                    return text2,carpolling_no
                else:
                    print('订单有效！')
            except Exception as e:
                print('出错啦！',e)
            # 提货、送货点数及单价
            self.send(self.pick_number[0],self.pick_number[1],pick_number)
            self.send(self.pick_pice[0],self.pick_pice[1],pick_pice)
            self.send(self.delivery_number[0], self.delivery_number[1],delivery_number)
            self.send(self.delivery_pice[0], self.delivery_pice[1],delivery_pice)
            # 选择产品
            self.click(self.product[0], self.product[1])
            self.click(self.product_value[0], self.product_value[1])
            # 选择线路
            self.click(self.line_start_choose[0],self.line_start_choose[1])
            self.click(self.line_start_value[0],self.line_start_value[1])
            self.click(self.line_end_choose[0], self.line_end_choose[1])
            self.click(self.line_end_value[0], self.line_end_value[1])
            # 拼车单号
            self.send(self.carpooling_no[0],self.carpooling_no[1],tm)
            # 添加车型
            self.click(self.choose_cartype_button[0],self.choose_cartype_button[1])
            self.scroll()
            # 判断是否是整车或者铁水
            try:
                if self.element(self.load_tips[0], self.load_tips[1],time=5,screenshot='f')!= 'fail':
                    text3 = self.element(self.load_tips[0], self.load_tips[1]).text
                    carpolling_no = 'fail'
                    print(text3)
                    return text3,carpolling_no
                else:
                    print('订单产品是整车或者铁水，产品也有效')
            except Exception as e:
                print('出错啦！',e)
            # 车型选择
            self.click(self.chosse_cartype[0],self.chosse_cartype[1])
            self.click(self.chosse_cartype_value[0],self.chosse_cartype_value[1])
            time.sleep(2)
            # 车型数量
            self.send(self.car_number[0], self.car_number[1],complete_vehicle_quality)
            # 点击单价，让费用重算
            self.click(self.price[0],self.price[1])
            # 切换到列表框架
            self.out_iframe()
            self.in_iframe(self.listframe[0],self.listframe[1])
            # 提交
            self.click(self.submit[0],self.submit[1])
            # 进入编辑框架
            self.in_iframe(self.edit_frame[0], self.edit_frame[1])
            time.sleep(5)
            try:

                if self.element(self.load_tips[0], self.load_tips[1],time=5,screenshot='f')!= 'fail':
                    # print('点击提交出现弹窗1')
                    text2 = self.element(self.load_tips[0], self.load_tips[1]).text
                    carpolling_no = 'fail'
                    print(text2)
                    return text2,carpolling_no
                else:
                    pass
            except Exception as e:
                print('出错啦！',e)

            # 提交失败弹窗
            try:

                if self.element(self.submit_tips[0], self.submit_tips[1], time=5, screenshot='f') != 'fail':
                    # print('点击提交出现弹窗2')
                    text2 = self.element(self.submit_tips[0], self.submit_tips[1]).text
                    carpolling_no = 'fail'
                    print(text2)
                    return text2, carpolling_no
                else:
                    pass
            except Exception as e:
                print('出错啦！', e)
                # 切换到列表框架
            self.out_iframe()
            self.in_iframe(self.listframe[0], self.listframe[1])
            time.sleep(2)
            # 保存提示语消失太快，难以捕捉，刚进入编辑列表，提示框就消失了，
            # 只能提交操作后刷新列表，查看第一条是否是刚才新增的
            # 点击查询
            self.click(self.select_click[0], self.select_click[1])
            self.list_carpooling_no[1]='/html/body/div[2]/div/div[2]/div[2]/table/tbody/tr[1]/td[3]/div[text()="{}"]'.format(tm)
            # 通过列表第一条是否是刚才新增那条判断是否保存成功
            if self.element(self.list_carpooling_no[0],self.list_carpooling_no[1],time=8,screenshot='f')!='fail':
                text =u'创建成功！'
                carpolling_no = tm
            else:
                text = u'提交失败或查询出错！'
                carpolling_no = 'fail'
            print(text)
            self.out_iframe()
        except Exception as e:
            print('出错！',e)
            text=u'拼车出错啦！'

        # delorder_flag 不为 None 时，表示要进入删除订单
        if delorder_flag is not None:
            # 拼车单创建成功情况下才执行删除订单操作
            if '创建成功' in text:
                try:
                    run1 = OrderPage()
                    order_text = run1.del_order(pcustomer_no=rcustomer_no_list[0],case=case,row=row)
                except Exception as e:
                    order_text = '拼车后删除订单出错！'
                    print('拼车后删除订单出错！', e)

            else:
                order_text = '拼车创建失败，不进行删除订单操作！'
                print('拼车创建失败，不进行删除订单操作！')
            return order_text, carpolling_no
        else:
            print('不需要删除订单操作！')

        # editorder_flag 不为 None 时，表示要进入编辑订单
        if editorder_flag is not None:
            # 拼车创建成功情况下才执行删除订单操作
            if '创建成功' in text:
                try:
                    run1 = OrderPage()
                    order_text = run1.edit_order(pcustomer_no=rcustomer_no_list[0],case=case,row=row)
                except Exception as e:
                    order_text = '拼车后编辑订单出错！'
                    print('拼车后编辑订单出错！', e)

            else:
                order_text = '拼车创建失败，不进行编辑订单操作！'
                print('拼车创建失败，不进行编辑订单操作！')
            return order_text, carpolling_no
        else:
            print('不需要编辑订单操作！')

        # more_flag 不为 None 时，表示要再次拼车
        if  more_flag is not None:
            if '创建成功' in text :
                print('再次拼车输入的单号',rcustomer_no_list)
                text1, carpolling_no = self.add_carpooling(lg='f',customer_no_list=rcustomer_no_list,row=row,case=case)
                # print('测试')
                if text1 == u'创建成功！':
                    text = u'再次拼车创建成功！'
                else:
                    text = u'再次拼车创建失败！' + text1
                return text, carpolling_no
            else:
                print('需要再次拼车，但第一次拼车出错，不进行第二次拼车！')
        else:
            print('不需要再次做拼车操作！')

        return text,carpolling_no

    # 删除拼车
    # carpooling_no  拼车单号, add_carpooling_no  客户单号，默认不需要输入，自动做订单及删除
    def del_carpooling(self,lg='f',case=[],carpooling_no='f',add_carpooling_no=[],row=None):
        # f 默认不输入拼车单号
        try:
            if carpooling_no == 'f':
                text,carpooling_no1 = self.add_carpooling(customer_no_list=add_carpooling_no,row=row,case=case)

                # self.carpooling_no = carpooling_no1

                if text == u'创建成功！':
                    self.carpooling_no = carpooling_no1
                    print('输入的拼车号是：{}'.format(self.carpooling_no))
                else:
                    Mylog().my_log().error('拼车失败，请输入要删除的拼车单！')
                    self.text = '拼车失败，请输入要删除的拼车单！'
                    print(self.text)
                    return self.text
            else:
                self.carpooling_no=carpooling_no
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
            self.click(self.customer_carpooling[0], self.customer_carpooling[1])
            # 进入列表
            self.in_iframe(self.listframe[0], self.listframe[1])
            time.sleep(5)
            # 输入要过滤的拼车单号
            self.send(self.carpoolNo[0],self.carpoolNo[1],self.carpooling_no)
            # 点击查询
            self.click(self.select_click[0], self.select_click[1])
            # time.sleep(5)
            # 选中拼车单
            self.click(self.carpooling_check_box[0], self.carpooling_check_box[1])
            # time.sleep(2)
            # 删除按钮
            self.click(self.delete_button[0], self.delete_button[1])
            # time.sleep(13)
            # 确定删除
            self.click(self.accept_delete[0], self.accept_delete[1])

            # 失败与成功的弹窗不同，第一个定位完，弹窗消失，所以第二个也会定位失败,所以不能分开定位
            try:
                if  self.element(self.delete_fail_tips[0], self.delete_fail_tips[1],time=6) !='fail':
                    self.text = self.element(self.delete_fail_tips[0], self.delete_fail_tips[1], time=6).text
                    print(self.text)
                else:
                    self.text = u'拼车单删除成功'
                    print(self.text)

            except Exception as e:
                # 也可以考虑数据查询判断是否删除成功，并且测试删除成功的情况比失败情况少，可以暂时先这么处理
                print('删除拼车返回结果定位出错!',e)
            self.out_iframe()
        except Exception:
            self.text=u'删除拼车出错!'
        # self.quit()
        return self.text

    # 编辑拼车
    # carpooling_no 拼车单号, add_carpooling_no 客户单号，默认不需要输入，自动做订单及删除
    def edit_carpooling(self,lg='f',case=[], carpooling_no='f', add_carpooling_no=[],row=None):
        # f 默认不输入拼车单号
        try:
            if carpooling_no == 'f':
                text, carpooling_no1 = self.add_carpooling(customer_no_list=add_carpooling_no,row=row,case=case)

                self.carpooling_no = carpooling_no1

                if text == u'创建成功！':
                    self.carpooling_no = carpooling_no1
                    print('输入的客户单号是：'.format(self.carpooling_no))
                    # time.sleep(2)
                else:
                    Mylog().my_log().error('拼车失败，请输入要删除的拼车单！')
                    self.text = '拼车失败，请输入要删除的拼车单！'
                    print(self.text)
                    return self.text
            else:
                self.carpooling_no = carpooling_no
            # 登录
            if lg == 't':
                # 登录
                self.login(username=case[-4], password=case[-3])
            else:
                print('不需要登录')
            # # 登录
            # self.login(username=case[-4], password=case[-3])
            # 关闭所有标签
            self.click(self.close_tab[0], self.close_tab[1])
            self.click(self.close_tab[0], self.close_tab[1])
            self.click(self.close_tab[0], self.close_tab[1])
            # 一级菜单
            self.click(self.order_manage_module[0], self.order_manage_module[1])
            # 进入拼车菜单
            self.click(self.customer_carpooling[0], self.customer_carpooling[1])
            # 进入列表
            self.in_iframe(self.listframe[0], self.listframe[1])
            time.sleep(5)

            # 输入要过滤的拼车单号
            self.send(self.carpoolNo[0], self.carpoolNo[1], self.carpooling_no)

            # 点击查询
            self.click(self.select_click[0], self.select_click[1])
            # time.sleep(5)
            # 选中拼车单
            self.click(self.carpooling_check_box[0], self.carpooling_check_box[1])
            # 点击编辑按钮
            self.click(self.update[0], self.update[1])
            self.scroll()
            self.scroll()
            # 循环判断金额不为0才点击提交，否则直接进入提交，有些信息没有加载完，会报错，总共等待20*3 秒
            for i in range(1,7):
                try:
                    if self.element(self.totalfee[0], self.totalfee[1], time=2, screenshot='f') == 'fail':
                        continue
                    elif self.element(self.totalfee[0],self.totalfee[1],time=3,screenshot='f').text =='0':
                        continue
                    else:
                        print(self.element(self.totalfee[0], self.totalfee[1], time=3, screenshot='f').text)
                        break
                except Exception as e:
                    print("出错了")
                    Mylog().my_log().error('出错了',e)
            # 点击提交
            self.click(self.submit[0],self.submit[1])
            # 提交结果，用于断言
            self.in_iframe(self.edit_frame[0], self.edit_frame[1])
            # 定位提示语
            try:
                text = self.element(self.submit_tips2[0], self.submit_tips2[1], time=8, screenshot='f').text
                print(text)
            except Exception as e:
                text = u'没有定位到提示语'
                Mylog().my_log().error('没有定位到提示语')
                print(text)
            self.out_iframe()
            # self.in_iframe(self.listframe[0], self.listframe[1])
            # time.sleep(5)
        except Exception as e:
            Mylog().my_log().error('编辑失败！',e)
            print('编辑失败！')
            text=u'编辑失败！'
        return text


    # 审核拼车
    # clientorder_margerfeeno  合并单号, add_clientorder_margerfeeno 客户订单号，默认不输入，自动创建订单
    def approval_carpoolling(self, lg='f',case=[],clientorder_carpoollingfeeno=None, add_clientorder_carpoollingfeeno=[],delcarpooling_flag=None,row=None):

        # f 默认不输入拼车单号
        try:
            if clientorder_carpoollingfeeno is None:
                text, clientorder_carpoollingfeeno_no1 = self.add_carpooling(customer_no_list=add_clientorder_carpoollingfeeno,row=row,case=case)
                print(1111)
                if  u'创建成功！' in text:
                    self.clientorder_carpoollingfeeno_no = clientorder_carpoollingfeeno_no1
                    print('输入的拼车单号是：{}'.format(self.clientorder_carpoollingfeeno_no))
                else:
                    Mylog().my_log().error('合并失败，请输入要审核的拼车单号！')
                    self.text = '合并失败，请输入要审核的拼车单号！'
                    print(self.text)
                    return self.text
                # # 退出浏览器
                # self.quit()
            else:
                self.clientorder_carpoollingfeeno_no = clientorder_carpoollingfeeno
            # # 登录
            if lg == 't':
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
            self.click(self.customer_carpooling[0], self.customer_carpooling[1])
            # 进入列表
            self.in_iframe(self.listframe[0], self.listframe[1])
            time.sleep(5)

            # 输入要过滤的合并单号
            self.send(self.carpoolNo[0], self.carpoolNo[1], self.clientorder_carpoollingfeeno_no)
            # 点击查询
            self.click(self.select_click[0], self.select_click[1])
            time.sleep(3)
            # 选中合并计费单
            self.click(self.carpooling_check_box[0], self.carpooling_check_box[1])
            # time.sleep(2)
            # 审核按钮
            self.click(self.approval_button[0], self.approval_button[1])
            # time.sleep(13)
            # 确定审核
            self.click(self.accept_approval[0], self.accept_approval[1])

            # 失败与成功的弹窗不同，第一个定位完，弹窗消失，所以第二个也会定位失败,所以不能分开定位
            try:
                if self.element(self.approval_fail_tips[0], self.approval_fail_tips[1], time=6,screenshot='n')!='fail':
                    self.text = self.element(self.approval_fail_tips[0], self.approval_fail_tips[1], time=6,
                                             screenshot='n').text
                    print(self.text)
                else:
                    self.text = u'审核成功'
                    print(self.text)
            except Exception:
                # 也可以考虑数据查询判断是否删除成功，并且测试删除成功的情况比失败情况少，可以暂时先这么处理
                print('拼车审核出错啦')
            # 退出浏览器
            # self.quit()
            self.out_iframe()
        except Exception :
            self.text = u'审核拼车单出错!'

        if delcarpooling_flag is not None:
            # 合并单创建成功情况下才执行删除订单操作
            if '审核成功' in self.text:
                try:
                    del_text = self.del_carpooling(carpooling_no=self.clientorder_carpoollingfeeno_no,row=row,case=case)
                except Exception as e:
                    del_text = '拼车审核后删除拼车单出错'
                    print('拼车审核后删除拼车单出错', e)

            else:
                del_text = '拼车单审核失败，不进行删除拼车单操作'
                print('拼车单审核失败，不进行删除拼车单操作')
            return del_text
        else:
            print('不需要删除拼车单操作！')


        return self.text



if __name__ == '__main__':
    run=CarpoolingPage()
    # 测试产品没有审核
    # list='20200604102739'
    # 测试是否是否非铁水或者 整车
    list = '20200607103426,20200607103608'
    # list='2020060410, 202006041026,202006041027'
    # run.add_carpooling()
    run.del_carpooling(carpooling_no='20200607103426')
    # run.edit_carpooling(carpooling_no='20200608155310')