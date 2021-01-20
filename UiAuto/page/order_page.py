#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/5/6 17:00
# @Author : msy

from common.general import *
from config import *
from common.log import *
import time
from common.data_operate import *
import threading
from page_element.order_page_element import *
# import lock
# from multiprocessing import Lock,Process

# def order_decorator(args):
#     pass
#     新增订单方法已被多处调用，新增一个参数，调用代码也要修改，尝试考虑用装饰器，
#     但目前了解到装饰器更多适用增加额外功能，修改原方法的逻辑目前不知道如何实现

# class OrderPageObject():
#     pass

# 订单页面类
class OrderPage(OrderPageE):
    # COUNT = 1
    # globals(COUT=0)
    # 创建锁对象
    # process_lock=Lock()
    # lock=threading.Lock()
    lock=threading.RLock()
    # 订单保存结果弹窗
    submit_elastic_frame=['xpath',"//span[@class='layui-layer-setwin']/parent::div//div[@class='layui-layer-content layui-layer-padding']"]
    # 发货地址码
    newshippingcode='#tpModule > div:nth-child(3) > div.layui-col-md2.myWidth-16 > div > dl > dd[lay-value="{}"]'
    shippingcode='#tpModule > div:nth-child(3) > div.layui-col-md2.myWidth-16 > div > dl > dd[lay-value="test0701"]'
    # 收货地址码
    newreceivingcode='#tpModule > div:nth-child(5) > div.layui-col-md2.myWidth-16 > div > dl > dd[lay-value="{}"]'
    receivingcode='#tpModule > div:nth-child(5) > div.layui-col-md2.myWidth-16 > div > dl > dd[lay-value="test0702"]'
    # 产品
    newchoose_product_ld2='#layui-tab-content01 > div.layui-tab-item.layui-show > div:nth-child(1) > div.layui-col-md2 > div > dl >dd[lay-value="{}"]'


    # 新增订单，客户订单号默认是取程序跑的时间，允许跑的时候输入
    # lg = 'T' 默认要登录   producttype   产品类型 , pcustomer_sales_no 销售单号,
    # pcustomer_no  客户订单号，默认传入时间, pweight  总重量, pvolume 总体积, pquantity  总件数,
    # complete_vehicle_quality  整车/铁水数量，默认是1; row参数是为了解决多进程导致订单号重复的问题
    def add_order(self,case=[],lg='T',producttype='LD',pcustomer_sales_no ='123120003',pcustomer_no= None,pweight='12',pvolume='110',\
                  pquantity='140',complete_vehicle_quality='1',shippingcode=None,receivingcode=None,row=None,*args,**kwargs):

        rdict=[]
        self.lock.acquire()
        if pcustomer_no is None:
            print(pcustomer_no)
            print(lg)
            pcustomer_no = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))+"-"+str(row)
            # pcustomer_no = get_customerno()
            time.sleep(2)
            print('关注',pcustomer_no )
            self.lock.release()
            # self.process_lock.acquire()
        else:
            print('有输入单号')
            # rpcustomer_no=pcustomer_no
        try:
            # 目的是判断是否要登录
            if lg.upper()=='T':
                # 登录
                self.login(username=case[-4],password=case[-3])
            else:
                # print('不用登录！')
                print(pcustomer_no)
                print(lg)

            # 关闭所有标签
            self.click_close_tab()
            self.click_close_tab()
            self.click_close_tab()
            # 一级菜单
            self.click_order_manage_module()
            # time.sleep(2)
            # 二级菜单
            self.click_order_deal_with()
            # time.sleep(2)
            # 进入列表
            self.frame_listframe()
            time.sleep(2)
            # 点击新增
            self.click_add()
            # 进入编辑页面框架
            self.frame_editframe()
            # 进入直接点击，下拉是没有值的，这也是界面上确存的一个小BUG，所以暂时先强制等待5秒
            time.sleep(4)
            # self.implicitlty_wait(20)
            # 点击客户下拉框
            self.click_delivery_customer()
            time.sleep(1)
            # 选择客户
            self.click_customer()
            time.sleep(1)
            # 输入客户单号
            self.clear_customer_no()
            self.send_customer_no(send=pcustomer_no)
            # 订单类型下拉框
            self.click_customer_type()
            # 选择订单类型
            self.click_customtype()
            # 输入销售单号
            self.send_customer_sales_no(send=pcustomer_sales_no)
            # 输入重量
            self.send_weight(send=pweight)
            # 输入体积
            self.send_volume(send=pvolume)
            # 输入件数
            self.send_quantity(send=pquantity)
            # 业务类型下拉
            self.click_business_type()
            time.sleep(1)
            # 选择业务类型
            self.click_bustype()
            # 滚动页面
            self.scroll_shipping_type()
            # 运输方式下拉
            self.click_shipping_type()
            # 选择运输方式
            self.click_shipping_type_value()
            # 提货上门
            self.click_pickup()
            # 提货方式下拉
            self.click_pickup_type()
            # 选择提货方式
            self.click_picktype()

            # 发货地址码下拉
            self.click_shipping_address_code()
            # 选择发货地址码
            newshippingcode= self.newshippingcode.format(shippingcode) if shippingcode is not None else self.shippingcode
            time.sleep(3)
            self.click_shippingcode(param=newshippingcode)
            # self.click(self.shippingcode[0], self.shippingcode[1])
            # 目的是加载过快，选项没有出来
            time.sleep(3)
            # 收货地址码下拉
            self.click_receiving_address_code()
            # 选择收货地址码
            newreceivingcode=self.newreceivingcode.format(receivingcode)if receivingcode is not None else self.receivingcode
            # print('输出收货地址',self.receivingcode[1])
            time.sleep(2)
            self.click_receivingcode(param=newreceivingcode)
            time.sleep(2)
            # 滚动到产品选择
            self.scroll_product()
            # 进入产品选择
            self.click_product()
            # 产品下拉
            self.click_prductlist()
            time.sleep(1)
            if producttype.upper()=='KD':
                # 选择快递产品
                self.click_choose_product()
            elif producttype.upper()=='ZC':
                # 选择整车产品
                self.click_choose_product_zc()
                self.send_complete_vehicle_quality(send=complete_vehicle_quality)
                # 点击一下单价，目的是让费用重算
                self.click_unit_price()

            elif producttype.upper()=='TS':
                # 选择铁水产品
                self.click_choose_product_ts()
                self.send_complete_vehicle_quality(send=complete_vehicle_quality)
                # 点击一下单价，目的是让费用重算
                self.click_unit_price()

            elif producttype.upper()=='LD':
                # 选择零担产品
                self.click_choose_product_ld()
            elif producttype.upper()=='LDTH':
                # 选择零担提货产品
                self.click_choose_product_ld_th()
            elif producttype.upper()=='LDSH':
                # 选择零担提送货产品
                self.click_choose_product_ld_sh()
            elif producttype.upper()=='LD_0529':
                # 选择零担0529
                self.click_choose_product_ld_0529()
            elif producttype.upper()=='ZC_0421':
                # 选择整车0421
                self.click_choose_product_zc_0421()
                self.send_complete_vehicle_quality(send=complete_vehicle_quality)
                # 点击一下单价，目的是让费用重算
                self.click_unit_price()
            # 输入产品id,id共性都是有TP（应该是运输的意思），没有考虑整车铁水等选择产品后还有其他操作的情况，这是方便添加零担产品的
            elif 'TP' in producttype.upper():
                newchoose_product_ld2=self.newchoose_product_ld2.format(
                    producttype)
                self.click_choose_product_ld2(param=newchoose_product_ld2)

            else:
                self.text1 = u'产品输入有问题'
                self.out_iframe()
                rpcustomer_no = 'fail'
                return self.text1,rpcustomer_no,rdict
            try:
                # 再写一个列表金额与查看页面金额对比的方法，该方法调用之前写的查看页面金额的方法，输入一个参数，默认是不对比金额
                # 定位计算出来的费用
                element = self.element_totalfee()
                for i in range(20):
                    if self.element(element[0], element[1], time=8).text == '0':
                        time.sleep(1)
                        continue
                    else:
                        rdict['transport_total_fee'] = self.element(element[0], element[1], time=3).text
                        break
            except Exception as e:
                print(e)
            time.sleep(2)
            # 退出框架
            self.out_iframe()
            # 进入列表框架
            self.frame_listframe()
            # print('进入框架哈哈')
            time.sleep(5)
            # 点击提交
            self.click_submit()
            # time.sleep(2)
            # print('点击提交！')
            # 运行脚本发现有时候已经点击了提交，但是系统没有反应，需要进行第二次点击，
            # 降低失败的概率,不要截图，截图会占用时间，导致后面提交返回的结果定位不到!
            try:
                element=self.element_submit()
                # print(element[0],element[1])
                if self.element(element[0],element[1],time=1)!='fail':
                    self.click_submit()
                    print('第二次点击提交！')
                else:
                   text2='没有定位到结果弹窗'

            except Exception as e:
                print('结果弹窗定位出错！！！！！',e)

            # 进入编辑页面框架
            self.frame_editframe()
            # self.scroll()
            # 获取提交订单弹框提示语，可用于断言
            try:
                element=self.element_submit_elastic_frame()
                if self.element(element[0],element[1])!='fail':
                   text2 = self.element(element[0],element[1]).text
                else:
                   text2='没有定位到结果弹窗'

            except Exception as e:
                print('结果弹窗定位出错！！！！！',e)
            rpcustomer_no = pcustomer_no if text2==u'新增订单成功' else 'fail'
            print('订单号:{},返回结果：{}'.format(rpcustomer_no,text2))
            self.out_iframe()
        except Exception as e:
           Mylog().my_log().error('订单新增出错，原因如下：'.format(e))
           text2= u'订单创建出错！'
           rpcustomer_no='fail'
           print(pcustomer_no)
           # print(lg)
        # self.quit()
        print(text2,rpcustomer_no)
        return text2,rpcustomer_no,rdict

    # 删除订单不输入客户订单号，默认是先跑一遍创建订单方法，删除新建的订单；
    # 删除成功与失败要分开定位，t表示要定位删除成功的，其他则是定位删除失败的（成功与失败元素不相同）
    # 订单删除
    # pcustomer_no 客户订单号，默认是时间
    def del_order(self,lg='f',case=[],pcustomer_no=None,row=None):
        try:
            if pcustomer_no is None:
                text,rpcustomer_no,rdict = self.add_order(row=row,case=case)
                self.pcustomer_no=rpcustomer_no
                # 关闭新增的页签
                # self.click(self.tab[0], self.tab[1])
                if text == u'新增订单成功':
                    time.sleep(3)
                    # 点击查询
                    # self.click(self.select_click[0], self.select_click[1])
                    # print('执行查询')
                    time.sleep(3)
                    print('输入的客户单号是：{}'.format(self.pcustomer_no))
                    time.sleep(2)
                else:
                    Mylog().my_log().error('创建订单失败，请输入要删除的订单号')
                    print('创建订单失败，请输入要删除的订单号')
                    self.text = '创建订单失败，请输入要删除的订单号'
                    return self.text
            else:
                self.pcustomer_no = pcustomer_no
            if lg == 't':
                # 登录
                self.login(username=case[-4], password=case[-3])
            else:
                print('不需要登录')

            # 关闭所有标签
            self.click_close_tab()
            self.click_close_tab()
            self.click_close_tab()
            # 一级菜单
            self.click_order_manage_module()
            # 二级菜单
            self.click_order_deal_with()
            time.sleep(1)
            # 进入列表
            self.frame_listframe()
            time.sleep(3)
            # 列表查询，客户过滤下拉
            self.click_customer_filtering()
            time.sleep(2)
            # 列表查询，选择要过滤的客户
            with open(os.path.join(BASE_PATH, 'yamlconfig.yml'), mode='r',encoding='utf-8') as f:
                # load_all 读取多个文档
                l = [i for i in yaml.load_all(f)]
            customer_filtering_value = ['xpath','//*[@id="TBClientOrder_queryTable"]/tbody/tr[1]/td[1]/div/div/dl/dd[text()="{}"]'.format(l[1]['customer_filtering_value'])]
            self.click_customer_filtering_value(customer_filtering_value[0],customer_filtering_value[1])
            time.sleep(2)
            # 列表查询，客户订单号过滤
            self.send_customer_no_filtering_input(send=self.pcustomer_no)
            # 点击查询
            self.click_select_click()
            # 列表订单复选框
            self.click_order_check_box()
            # 删除按钮
            self.click_delete_button()
            # 确定删除
            self.click_accept_delete()
            try:
                element=self.element_delete_fail_tips()
                # 定位删除失败的提示语，若定位不到证明成功,这么处理的原因是成功与失败的提示框元素一样，但是弹出的时间不一样，所以无法准确定位
                if self.element(element[0],element[1])!='fail':
                    self.text = self.element(element[0],element[1]).text
                    print(self.text)
                else:
                    # 也可以考虑查询数据库判断是否删除成功，并且测试删除成功的情况比失败情况少，可以暂时先这么处理
                    self.text = u'删除成功'
                    print(self.text)

            except Exception as e:
                print('定位出错啦',e)

            self.out_iframe()
        except Exception:
            Mylog().my_log().error('删除订单出错!')
            self.text=u'删除订单出错!'
        # self.quit()
        return self.text

    # 编辑，不输入客户订单号，默认是先跑一遍创建订单方法，编辑新建的订单
    # pcustomer_no 客户订单号，默认时间, pweight 总重量, pvolume 重体积, pquantity 总件数，有默认值
    def edit_order(self,lg='f',case=[],pcustomer_no=None,pweight=None,pvolume=None,pquantity=None,row=None):
        try:
            if pcustomer_no is None:
                text, rpcustomer_no,rdict = self.add_order(row=row,case=case)
                self.pcustomer_no = rpcustomer_no
                # 关闭新增的页签
                # self.click(self.tab[0],self.tab[1])
                if text == u'新增订单成功':
                    time.sleep(3)
                    # # 点击查询
                    # self.click(self.select_click[0], self.select_click[1])
                    # print('执行查询')
                    time.sleep(3)
                    print('输入的客户单号是：{}'.format(self.pcustomer_no))
                    time.sleep(2)
                else:
                    Mylog().my_log().error('创建订单失败，请输入要编辑的订单号')
                    print('创建订单失败，请输入要编辑的订单号')
                    self.text1 = u'创建订单失败，请输入要编辑的订单号'
                    return self.text1
            else:
                self.pcustomer_no = pcustomer_no
            if lg == 't':
                # 登录
                self.login(username=case[-4], password=case[-3])
            else:
                print('不需要登录')
            # 关闭所有标签
            self.click_close_tab()
            self.click_close_tab()
            self.click_close_tab()
            # 一级菜单
            self.click_order_manage_module()
            # 二级菜单
            self.click_order_deal_with()
            time.sleep(1)
            # 进入列表
            self.frame_listframe()
            time.sleep(3)
            # 列表查询，客户过滤下拉
            self.click_customer_filtering()
            time.sleep(2)
            # 列表查询，选择要过滤的客户
            self.click_customer_filtering_value()
            time.sleep(2)
            # 列表查询，客户订单号过滤
            self.send_customer_no_filtering_input(send=self.pcustomer_no)
            # 点击查询
            self.click_select_click()
            # 列表订单复选框
            self.click_order_check_box()
            time.sleep(2)
            # 编辑按钮
            self.click_update()
            try:
                element=self.element_update_fail()
                # 判断是否出现失败弹框
                if self.element(element[0],element[1])!='fail':
                    self.text1 = self.element(element[0],element[1]).text
                    self.out_iframe()
                    return self.text1
                else:
                    pass

            except Exception as e:
                print('定位出错啦',e)

            # 循环判断金额不为0才点击提交，否则直接进入提交，有些信息没有加载完，会报错。这是页面设计有问题
            for i in range(1, 10):
                try:
                    element = self.element_totalfee()
                    # 没有定位到总金额元素，继续循环
                    if self.element(element[0], element[1],time=2) == 'fail':
                        continue
                    # 定位到总金额元素，但是费用为0，这种情况下提交会有问题，继续循环
                    elif self.element(element[0], element[1],time=3).text == '0':
                        continue
                    # 定位到总金额元素，费用不为0则跳出循环
                    else:
                        text=self.element(element[0], element[1],time=3).text
                        print(text)
                        break
                except Exception as e:
                    print("出错了")
                    Mylog().my_log().error('出错了', e)

            # 重量体积件数有输入值，则是要修改这部分内容，否则直接进入提交，若线路与产品需要修改，参照以下内容加代码逻辑
            if pweight is not None or pvolume is not None or pquantity is not None:
                self.frame_editframe()
                time.sleep(5)
                if pweight is not None:
                    self.clear_weight()
                    # 输入重量
                    self.send_weight(param=pweight)
                    time.sleep(2)
                else:
                    print('重量没有改变！')
                if pvolume is not None:
                    # 输入体积
                    self.clear_volume()
                    # 输入件数
                    self.send_volume(param=pvolume)
                    time.sleep(2)
                else:
                    print('体积没有改变！')

                if pquantity is not None:
                    self.clear_quantity()
                    self.send_quantity(param=pquantity)
                    time.sleep(2)
                else:
                    print('件数没有改变！')
                # 滚动到产品栏
                self.scroll_to_terminal_product()
                time.sleep(2)
                # 进入产品选择
                self.click_product()
                # 产品下拉
                self.click_prductlist()
                # 选择快递产品
                self.click_choose_product()
                time.sleep(5)
                # 退出框架
                self.out_iframe()
                # 进入列表框架
                self.frame_listframe()
                time.sleep(5)
            else:
                print('重量体积件数没有修改！')

            # 点击提交
            self.click_submit()
            # 进入编辑页面框架
            self.frame_editframe()
            # self.scroll()
            # 获取提交订单弹框提示语，可用于断言
            try:
                element = self.element_submit_elastic_frame()
                # 获取提交订单弹框提示语，可用于断言
                if self.element(element[0], element[1]) != 'fail':
                    self.text1 = self.element(element[0], element[1]).text
                    # return self.text1
                else:
                    self.text1 = '没有定位到提交结果弹窗'

            except Exception as e:
                print('定位出错啦', e)
            # 退出框架
            self.out_iframe()
            # 进入列表框架
            # self.in_iframe(self.listframe[0], self.listframe[1])
            # time.sleep(3)
        except Exception as e:
            Mylog().my_log().error('编辑订单出错：{}'.format(e))
            print('编辑订单出错：{}'.format(e))
            self.text1 = 'f'
        self.quit()
        return self.text1

    # 过滤，客户通过位置选择，默认是第二个客户，uat客户
    # pcustomer_no 客户订单号  lg  是否要登录，默认要登录, customer 要过滤的客户，默认是UAT客户
    def filter(self,case=[],pcustomer_no=None,lg='t',customer='584.00',row=None):
        try:
            # 登录
            if lg=='t':
                self.login(username=case[-4],password=case[-3])

            else:
                print('不需要登录！')
            # 关闭所有标签
            self.click_close_tab()
            self.click_close_tab()
            self.click_close_tab()
            # 一级菜单
            self.click_order_manage_module()
            # 二级菜单
            self.click_order_deal_with()
            time.sleep(1)
            # 进入列表
            self.frame_listframe()
            time.sleep(3)
            # 列表查询，客户过滤下拉
            self.click_customer_filtering()
            time.sleep(2)
            # 列表查询，选择要过滤的客户
            value='#TBClientOrder_queryTable > tbody > tr:nth-child(1) > td:nth-child(1) > div > div > dl > dd[lay-value="{}"]'.format(customer)
            print(value)
            customer_filtering_value_new=['css',value]
            self.click_customer_filtering_value(customer_filtering_value_new[0], customer_filtering_value_new[1])
            time.sleep(2)
            # 列表查询，客户订单号过滤
            self.clear_customer_no_filtering_input()
            time.sleep(1)
            self.send_customer_no_filtering_input(param=pcustomer_no)
            # time.sleep(5)
            # 点击查询
            self.click_select_click()
            time.sleep(5)     #要暂停下，等待列表数据加载出来
            # 被查询子单调用，不能退出框架
            # self.out_iframe()
        except Exception as e:
            Mylog().my_log().error('过滤出错！',e)

    # 查询子订单号，应用场景是做作业单要用到订单子订单号
    # pcustomer_no 客户订单号 ，lg  是否要登录，默认是登录, customer  客户默认是uat客户

    def filter_subno(self,case=[],pcustomer_no=None, lg='t', customer='UATmsy',row=None):
        try:
            self.filter(lg=lg,pcustomer_no=pcustomer_no,case=case,customer=customer,row=row)
            # 选中订单
            self.click_order_check_box()
            # 点击子订单按钮
            self.click_sub_order_button()
            time.sleep(3)
            self.scroll()
            # 进入子订单列表
            self.frame_sub_order_frame()

            try:
                element = self.element_sub_order()
                # 获取子订单号，text
                if self.element(element[0], element[1]) != 'fail':
                    text = self.element(element[0], element[1]).text
                    # return self.text1
                else:
                    text='定位不到元素'
            except Exception as e:
                print('定位出错啦', e)
            # 退出子订单列表
            self.out_iframe()
            # self.in_iframe(self.listframe[0], self.listframe[1])
        except Exception as e:
            Mylog().my_log().error('过滤子订单失败！',e)
            text=u'过滤子订单失败！'
            print(text)
        print(text)
        return text


    # 上传订单
    # filepath 路径，有默认值；选择附件上传后，在上传过程中修改excel订单，
    # 不会影响上传，应该是在提交步就读取了所有内容，所以后面的修改不会影响
    def order_upload(self,case=[],copydata=None):
        resultlist=[]
        # 参数化订单号：
        with open(os.path.join(BASE_PATH, 'yamlconfig.yml'), 'r', encoding='utf-8') as f:
            filepath = [i for i in yaml.load_all(f)][1]['filepath']
            # 对订单号进行参数化并获取订单行数，目的是导入的完成时间会因为订单数量不同，时间不同，所以等待时间要乘行号这个系数
            self.lock.acquire()
            row,filepath2 = DataOperate().order_upload(filepath, copydata=copydata)
            self.lock.release()
            print('23')
            if row==1:
                text = u'失败，订单行数为0，无法导入'
                print(text)
                resultlist.append(text)
                resultlist.append(filepath2)
                return resultlist
            else:
                pass
            # print('订单导入打印返回的行数',row)
        try:
            # 登录
            self.login(username=case[-4], password=case[-3])
            # 关闭所有标签
            self.click_close_tab()
            self.click_close_tab()
            self.click_close_tab()
            # 一级菜单
            self.click_order_manage_module()
            # 二级菜单
            self.click_order_deal_with()
            time.sleep(1)
            # 进入列表
            self.frame_listframe()
            time.sleep(3)

            # 点击上传按钮
            # print('点击上传前')
            self.click_upload1()
            # print('点击上传')
            # 点击确实要上传文件
            self.click_update_determine()
            # 进入文件弹窗列表
            self.frame_file_iframe()
            # 添加文件
            self.click_add_file()
            # 选择文件
            # 由于selenuim 不能定位系统上传窗口，要借助AutoIt工具去定位，文件也要参数化
            # print('导入的地址',filepath)
            os.system(r"E:\software\python3.8.3\UiAuto\file\upload.exe %s"%filepath2)
            # time.sleep(3)
            self.click_add_file_submit()
            time.sleep(3)
            # 退出框架
            self.out_iframe()
            # 进入列表框架
            self.frame_listframe()
            # 提交附件
            self.click_submit_file()
            # 进入导入进程窗口列表
            time.sleep(2)
            self.frame_import_frame()
            # 导入结果提示语
            try:
                element = self.element_import_result_button()
                result=self.element(method=element[0], param=element[1], time=row*7,screenshot='n')
                if result!='fail':
                    # 失败原因有两种方式 ，一种是界面输出，另外一种是下载文件
                    if result.text!='导入成功':
                        # 下载文件查看失败原因
                        element2 = self.element_import_fail_download()
                        fail_download= self.element(method=element2[0], param=element2[1], screenshot='n')
                        if fail_download !='fail':
                            # 下载错误
                            self.click_import_fail_download()
                            time.sleep(3)
                            # 按最新修改时间降序排序，取第一个（最新的是上面下载的文件）
                            # os.path.getmtime() 函数是获取文件最后修改时间
                            # os.path.getctime() 函数是获取文件最后创建时间
                            lf = sorted(os.listdir(FILE), key=lambda x: os.path.getmtime(os.path.join(FILE, x)),
                                        reverse=True)
                            # 第一个是最新的
                            with open(os.path.join(FILE, lf[0]), 'r+', encoding='utf-8') as f:
                                # print('文件名', lf[0])
                                text = f.read()
                                # 全部输出，与文件保持一致
                                print('导入报错信息', text)
                                # 写入到日志中
                                Mylog().my_log().error(text)

                        else:
                            element3 = self.element_import_fail_reason()
                            # 定位界面的错误原因
                            text=self.element(element3[0],element3[1]).text
                    else:
                        # 结果不是失败
                        text = result.text
                    # 退出框架
                    self.out_iframe()
                    # 进入列表框架
                    self.frame_listframe()
                    # 关闭弹窗
                    self.click_import_hide(time=3)
                else:
                    text=u'没有定位到导入进程窗口！'
            except Exception:
                text = u'订单导入失败，但下载错误内容出错！'
            resultlist.append(text)
            resultlist.append(filepath)
        except Exception as e:
            Mylog().my_log().error('上传失败！',e)
            text=u'上传出错！'
            resultlist.append(text)
            resultlist.append(filepath2)
        # self.quit()
        return resultlist

    # 订单下载 LG 是判断是否要登录，filter_lg, 判断是否要登录  customer都是客户，filepath 是文件路径，有默认值
    # 20201012 应该再加一个逻辑，导出的文件记录数应该与界面的一致
    def order_download(self,case=[],lg='T',pcustomer_no='',filter_lg='f',customer='584.00',filepath=FILE):

        try:
            # 登录
            self.login(username=case[-4], password=case[-3])
            self.filter(case=case, lg=filter_lg, pcustomer_no=pcustomer_no, customer=customer)
            # time.sleep(5)
            # 点击导出按钮
            self.click_outport()
            # 进入点击下载框架
            # self.in_iframe(self.outport_frame[0],self.outport_frame[1])
            # 这么做的目的是没有进入框架时就不再执行后面语句，因为设置等待的时间太久，但是不这么设置，
            # 前面出错好像也不往后执行了
            if self.frame_outport_frame()=='2':
                text =u'导出出错啦！'
                return text
            else:
                # print('进入导出下载框架')
                # 通过定位此提示语，来确定是否下载完成，因为就算没有下载完成，代码仍能点击下载按钮,等待10分钟
                self.click_file_download_end(time1=600)
                # print('已经生成文件！')
                re_dirnum = len(
                    [lists for lists in os.listdir(filepath) if os.path.isdir((os.path.join(filepath, lists)))])
                re_firenum = len(
                    [lists for lists in os.listdir(filepath) if os.path.isfile((os.path.join(filepath, lists)))])
                print(re_firenum,re_dirnum)
                # 点击下载按钮
                self.click_outport_load()
                print('下载完成！')
                # 需要等待一下，否则太快，前后目录及文件会找到一样多
                time.sleep(5)
                #判断是否下载到文件,通过目录文件个数前后对比
                dirnum=len([lists for lists in os.listdir(filepath) if os.path.isdir((os.path.join(filepath,lists)))])
                firenum=len([lists for lists in os.listdir(filepath) if os.path.isfile((os.path.join(filepath,lists)))])
                print(firenum, dirnum)

                if re_dirnum!=dirnum or re_firenum!=firenum:
                    print('文件下载到指定目录')
                    text=u'导出成功'
                else:
                    print('文件没有下载到指定目录或者下载失败')
                # 退出框架
                self.out_iframe()
                # 进入列表
                self.frame_listframe()
                time.sleep(3)
                # 关闭下载弹窗
                self.click_export_close()

        except Exception :
            print('导出出错!')
            text=u'导出出错！'
        self.quit()
        return text

    # copydata,复制的行数，如果是none，则手工新增订单，否则导入订单
    def import_edit(self,case=[],copydata=None,lg='f',row=None,datasource=None,*args,**kwargs):
        resultlist=[]
        # 默认是ui，则界面新增订单及导入修改此订单
        pcustomer_no_list=[]
        with open(os.path.join(BASE_PATH, 'yamlconfig.yml'), 'r', encoding='utf-8') as f:
            yamlfile=[i for i in yaml.load_all(f)]
            # 订单导入路径
            # filepath = yamlfile[1]['filepath']
            # 修改导入路径
            import_edit_filepath = yamlfile[1]['edit_import_filepath']
            # 对订单号进行参数化并获取订单行数，目的是导入的完成时间会因为订单数量不同，时间不同，所以等待时间要乘行号这个系数
        try:
            if datasource is None:
                text, rpcustomer_no, rdict = self.add_order(row=row, case=case)
                # text, rpcustomer_no=u'新增订单成功','202101180001'
                # 关闭新增的页签
                if text == u'新增订单成功':
                    time.sleep(3)
                    print('输入的客户单号是：{}'.format(rpcustomer_no))
                    time.sleep(2)
                    pcustomer_no_list.append(rpcustomer_no)
                else:
                    Mylog().my_log().error('创建订单失败，请输入要编辑的订单号')
                    print('创建订单失败，请输入要编辑的订单号')
                    text1 = u'创建订单失败，请输入要编辑的订单号'
                    resultlist.append(text1)
                    resultlist.append('None')
                    return resultlist

            # 不是ui，先导入订单，再对此部分订单进行修改导入
            else:
                resultlist = self.order_upload(case=case,copydata=copydata)
                lg='t'
                if  '导入成功' in resultlist[0]:
                    print('上传订单成功')
                # 先读取上传成功的订单的客户单号并存入pcustomer_no_list，然后回写到修改模板中进行上传
                # 打开文件并读取客户单号
                    pcustomer_no = DataOperate().excel_operat(row=[1], col=[3, 4],filepath=resultlist[1])
                    print(pcustomer_no)
                    # 由float变成字符串
                    for i in pcustomer_no:
                        # 每个i都是list，所以要取出来
                        pcustomer_no_list.append(int((i[0])))

                else:
                    text1 = u'订单导入失败，无法导入修改'
                    resultlist.append(text1)
                    resultlist.append('None')
                    return resultlist

            # 复制修改导入模板的数据
            r,newfilepath=DataOperate().order_upload(filepath=import_edit_filepath, copydata=len(pcustomer_no_list),isparam='n')
            # 写入修改模板
            DataOperate().write_excel(row=[1], col=[2], valuelist=pcustomer_no_list,filepath=newfilepath)
            if lg == 't':
                # 登录
                self.login(username=case[-4], password=case[-3])
            else:
                print('不需要登录')
            # 关闭所有标签
            self.click_close_tab()
            self.click_close_tab()
            # 一级菜单
            self.click_order_manage_module()
            # 二级菜单
            self.click_order_deal_with()
            time.sleep(1)
            # 进入列表
            self.frame_listframe()
            time.sleep(3)

            # 点击修改上传按钮
            # print('点击修改上传前')
            self.click_import_edit_button()
            # print('点击上传')
            # 点击确实要上传文件
            self.click_update_determine()
            # 进入文件弹窗列表
            self.frame_file_iframe()
            # 添加文件
            self.click_add_file()
            # 选择文件
            # 由于selenuim 不能定位系统上传窗口，要借助AutoIt工具去定位，文件也要参数化
            # print('导入的地址',filepath)
            os.system(r"E:\software\python3.8.3\UiAuto\file\upload.exe %s" % newfilepath)
            # time.sleep(3)
            self.click_add_file_submit()
            time.sleep(3)
            # 退出框架
            self.out_iframe()
            # 进入列表框架
            self.frame_listframe()
            # 提交附件
            self.click_submit_file()
            # 进入导入进程窗口列表
            time.sleep(2)
            self.frame_import_frame()
            # 导入结果提示语
            try:
                element = self.element_import_result_button()
                result = self.element(method=element[0], param=element[1], time=row * 7, screenshot='n')
                if result != 'fail':
                    # 失败原因有两种方式 ，一种是界面输出，另外一种是下载文件
                    if result.text != '导入成功':
                        # 下载文件查看失败原因
                        element2 = self.element_import_fail_download()
                        fail_download = self.element(method=element2[0], param=element2[1], screenshot='n')
                        if fail_download != 'fail':
                            # 下载错误
                            self.click_import_fail_download()
                            time.sleep(3)
                            # 按最新修改时间降序排序，取第一个（最新的是上面下载的文件）
                            # os.path.getmtime() 函数是获取文件最后修改时间
                            # os.path.getctime() 函数是获取文件最后创建时间
                            lf = sorted(os.listdir(FILE), key=lambda x: os.path.getmtime(os.path.join(FILE, x)),
                                        reverse=True)
                            # 第一个是最新的
                            with open(os.path.join(FILE, lf[0]), 'r+', encoding='utf-8') as f:
                                # print('文件名', lf[0])
                                text1 = f.read()
                                # 全部输出，与文件保持一致
                                print('导入报错信息', text1)
                                # 写入到日志中
                                Mylog().my_log().error(text1)

                        else:
                            element3 = self.element_import_fail_reason()
                            # 定位界面的错误原因
                            text1 = self.element(element3[0], element3[1]).text
                    else:
                        # 结果不是失败
                        text1 = result.text
                    # 退出框架
                    self.out_iframe()
                    # 进入列表框架
                    self.frame_listframe()
                    # 关闭弹窗
                    self.click_import_hide(time=3)
                else:
                    text1 = u'没有定位到导入进程窗口！'
                # 导入成功后，对比金额，后续看情况优化
                if '导入成功' in text1:
                    pass
                else:
                    pass
            except Exception as e:
                print(e)
                text1 = '定位返回结果失败！'
        except Exception as e:
            print(e)
            text1='订单修改导入出错'
        resultlist.append(text1)
        resultlist.append('None')
        return resultlist

'''
            # 关闭所有标签
            self.click_close_tab()
            self.click_close_tab()
            self.click_close_tab()
            # 一级菜单
            self.click_order_manage_module()
            # 二级菜单
            self.click_order_deal_with()
            time.sleep(1)
            # 进入列表
            self.frame_listframe()
            time.sleep(3)
            # 直接拷贝订单上传部分的代码
        except Exception as e :
            print(e)
'''

if __name__ == '__main__':
    OrderPage().atest()


    # run1=OrderPage()
    # run2=OrderPage()
    # run1.order_upload()
    # run2=OrderPage()
    # run.edit_order()
    # run.order_download()
    # run.del_order(pcustomer_no='2020092726')
    # run.add_order(pcustomer_no='000999333',receivingcode='999977-8')
    # run1=OrderPage()
    # run2=OrderPage()
    # run3 = OrderPage()
    # run.del_order(pcustomer_no='202005291049481')
    # print(run.add_order())
    # list=['ZC_0529','ZC_0529','LD_0529','LD_0529']
    # for i in list:
    #     run.add_order(LG='N',producttype=i)
    # run.edit_order(pcustomer_no='20200609103553')
    # run.filter_subno(pcustomer_no='60111107126')
    # for i in range(5):
    #
    #     run.add_order()
    # run.order_upload(filepath=r'E:\software\python3.5.1\UiAuto\file\登康.xlsx')
    # run.order_upload(filepath=r'E:\software\python3.5.1\UiAuto\file\import0710.xlsx')
    # run.order_upload(filepath=r'E:\software\python3.5.1\UiAuto\file\nandan.xlsx')
    # run.order_upload(filepath=r'E:\software\python3.5.1\UiAuto\file\importmnls.xlsx')

    # run.order_download(customer='3')
    # run.filter(pcustomer_no='25150815',customer='5')
    # print(7*10)
    # thread1=threading.Thread(target=run1.add_order)
    # thread2=threading.Thread(target=run2.add_order)
    #
    # # thread2=threading.Thread(target=run2.order_download,args=('T','8.882165282E9',))
    # # run2.order_download()
    # # thread3=threading.Thread(target=run3.order_upload,args=(r'E:\software\python3.5.1\UiAuto\file\import0525.xlsx',))
    # #
    # thread1.start()
    # thread2.start()
    # thread3.start()
    # thread1.join()
    # thread2.join()
    # thread3.join()

    # run.order_download()