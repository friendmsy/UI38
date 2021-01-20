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
# import lock
# from multiprocessing import Lock,Process

# def order_decorator(args):
#     pass
#     新增订单方法已被多处调用，新增一个参数，调用代码也要修改，尝试考虑用装饰器，
#     但目前了解到装饰器更多适用增加额外功能，修改原方法的逻辑目前不知道如何实现

# class OrderPageObject():
#     pass

# 订单页面类
class OrderPage(BasePage):
    # COUNT = 1
    # globals(COUT=0)
    # 创建锁对象
    # process_lock=Lock()
    # lock=threading.Lock()
    lock=threading.RLock()

    #----------------------------------菜单
    # 订单管理模块
    order_manage_module = ['xpath', '//td[@title="订单管理"]/child::a[1]']
    # 订单处理
    order_deal_with = ['xpath', '//span[text()="订单处理_运输"]/parent::div[starts-with(@id,"_easyui_tree")]']

    # ---------------------------------订单管理列表
    # 菜单列表iframe
    listframe = ['xpath', '//iframe[@src="/oss/oms/TBClientOrder/todoList"]']

    # 系统首页页签
    close_tab=['xpath','//*[@id="index_tabs"]/div[1]/div[4]/table/tbody/tr/td[3]/a/span']
    # 提交按钮列表
    # listframe2 = ['xpath', '//iframe[@src="/oss/oms/TBClientOrderCarpool/list"]']
    # 新增
    add = ['xpath', '//*[@id="create"]']
    # 子单按钮
    sub_order_button = ['css','#queryInner']

    # 编辑
    update = ['css','#myUpdate']
    update_fail=['xpath','//*[starts-with(@id,"layui-layer")]//following-sibling::div[@class="layui-layer-content layui-layer-padding"]']
    # 上传按钮
    upload1 = ['css','button#importTp:nth-child(8)']
    # 导入成功提示语
    upload_success =['xpath','//div[text()="导入成功"]']
    # 导入失败定位下载按钮提示语
    upload_fail=['css','div.layui-layer-content.layui-layer-padding > a>span']
    # 导入失败下载
    upload_fail_load=['css','div.layui-layer-content.layui-layer-padding > a']
    # 列表查询，客户过滤下拉
    customer_filtering = ['css','#TBClientOrder_queryTable > tbody > tr:nth-child(1) > td:nth-child(1) > div > div > div > input']

    # 列表查询，选择要过滤的客户(执行删除时，过滤客户不稳定，有时会执行到下一个客户，但定位时确实是定位到uat客户)
    customer_filtering_value = ['css','#TBClientOrder_queryTable > tbody > tr:nth-child(1) > td:nth-child(1) > div > div > dl > dd[lay-value="UATmsy"]']
    # 列表查询，客户订单号过滤
    customer_no_filtering_input = ['css','#myClientOrderNo']
    # 点击查询
    select_click = ['css','#TBClientOrder_form > div > div:nth-child(3) > div:nth-child(1) > button']
    # 列表订单复选框
    order_check_box = ['css','body > div.weadmin-body > div > div.layui-table-box > div.layui-table-fixed.layui-table-fixed-l > div.layui-table-body > table > tbody > tr > td > div > div > i']

   # --------------------------------删除

    # 删除按钮
    delete_button = ['css','#remove']
    #确定删除
    accept_delete = ['xpath','//*[starts-with(@id,"layui-layer")]/div[3]/a[1][text()="确定"]']
    # 确认弹窗提示语
    is_delete=['xpath','//*[starts-with(@id,"layui-layer")]/div[2]']
    #删除失败提示语
    delete_fail_tips = ['xpath','//*[starts-with(@id,"layui-layer")]/div[2][contains(text(),"失败")]']
    #删除成功提示语
    delete_success_tips = ['xpath','//*[starts-with(@id,"layui-layer")]/div[text()="删除成功！"]']

    # -----------------------------------------导入
    update_determine = ['xpath','//*[starts-with(@id,"layui-layer")]/div[3]/a[1]']
    # 提交附件
    submit_file = ['css','div.layui-layer-btn.layui-layer-btn- > a.layui-layer-btn0']
    # 导入弹窗列表
    file_iframe = ['xpath','//*[starts-with(@id,"layui-layer-iframe")]']
    # 添加文件
    add_file= ['css','button#selectFile']
    # 上传文件
    add_file_submit = ['css', 'button#uploadAction']
    # 导入窗口列表
    import_frame=['xpath','//*[starts-with(@id,"layui-layer-iframe")]']
    # 导入结果按钮
    import_result_button=['xpath','//*[@id="processDiv"]/button']
    # 导入界面输出报错原因
    import_fail_reason=['xpath','//*[@id="processDiv"]']
    # 错误下载按钮
    import_fail_download=['xpath','//*[@id="processDiv"]/button[2]']
    # 导入窗口关闭按钮
    import_hide=['xpath','//*[starts-with(@id,"layui-layer")]/div[3]/a']

    # -------------------------------导出
    # 导出按钮
    outport=['xpath','//*[starts-with(@id,"excelFile")][1]']
    # 导出下载框架
    outport_frame = ['xpath', '//*[starts-with(@id,"layui-layer-iframe")]']
    # 文件生成
    file_download_end =['xpath','//td[text()="文件已生成，请点击下载按钮进行下载！"]']
    # 下载
    outport_load=['css','Button#downloadBtn']
    # 关闭
    export_close = ['xpath', '//*[starts-with(@id,"layui-layer")]/div[3]/a[text()="关闭"]']

    # ---------------------------------编辑页面
    # 编辑页面iframe
    editframe = ['xpath', '//iframe[@id="detailDiv"]/following::iframe[starts-with(@id,"layui-layer-iframe")]']
    # 发货客户
    delivery_customer = ['css', '#objForm > div > div:nth-child(2) > div.layui-row > div:nth-child(2) > div > div > input']
    # 选择客户，uat客户
    customer = ['xpath', '//form[@id="objForm"]/descendant::dd[@lay-value="UATmsy"]']
    # 客户单号
    customer_no = ['xpath', "//form[@id='objForm']/descendant::input[@name='clientOrderNo']"]
    # 客户订单类型下拉框
    customer_type = ['css', '#objForm > div > div:nth-child(2) > div.layui-row > div:nth-child(6) > div > div > input']
    # 选择订单类型
    customtype = ['css',
                  '#objForm > div > div:nth-child(2) > div.layui-row > div:nth-child(6) > div > dl > dd[lay-value="ys28"]']
    # 客户销售单号
    customer_sales_no = ['css', 'input[id="clientSalesNo"]']
    # 重量
    weight = ['css', 'input#totalWeight']
    # 体积
    volume = ['css', 'input#totalVolume']
    # 件数
    quantity = ['css', 'input#totalQty']
    # 点击业务信息，目的是让编辑时费用重算
    business_information = ['xpath','// div[text()= "业务信息"]']
    # business_information = ['xpath','//*[@id="objForm"]/div/div[3]/div[1]']
    # 业务类型下拉框
    business_type = ['css',
                     '#objForm > div > div:nth-child(4) > div:nth-child(2) > div:nth-child(2) > div > div > input']
    # 选择业务类型
    bustype = ['css', '#objForm > div > div:nth-child(4) > div:nth-child(2) > div:nth-child(2) > div > dl > dd[lay-value="1"]']
    #运输方式下拉
    shipping_type = ['css','#tpModule > div:nth-child(2) > div:nth-child(2) > div > div > input']
    #运输方式值
    shipping_type_value =['css','#tpModule > div:nth-child(2) > div:nth-child(2) > div > dl > dd:nth-child(2)']
    # 提货上门
    pickup = ['css', '#tpModule > div:nth-child(2) > div:nth-child(4) > div']
    # 提货方式下拉框
    pickup_type = ['css', '#tpModule > div:nth-child(2) > div:nth-child(6) > div > div > input']
    # 提货方式
    picktype = ['css', '#tpModule > div:nth-child(2) > div:nth-child(6) > div > dl > dd:nth-child(2)']
    # 发货地址编码下拉框
    shipping_address_code = ['css', '#tpModule > div:nth-child(3) > div.layui-col-md2.myWidth-16 > div > div > input']
    # 选择发货地址码
    shippingcode = ['css','#tpModule > div:nth-child(3) > div.layui-col-md2.myWidth-16 > div > dl > dd[lay-value="test0701"]']

    # 收货地址编码下拉框
    receiving_address_code = ['xpath','//*[@id="tpModule"]/div[5]/div[1]/div/div/input']
    # 选择收货地址码
    receivingcode = ['css', '#tpModule > div:nth-child(5) > div.layui-col-md2.myWidth-16 > div > dl > dd[lay-value="test0702"]']
    # 产品栏
    product = ['css', '#layui-tab-title01 > li:nth-child(3)']
    prductlist = ['css','#layui-tab-content01 > div.layui-tab-item.layui-show > div:nth-child(1) > div.layui-col-md2 > div > div > input']
    # 选择产品
    choose_product = ['css','#layui-tab-content01 > div.layui-tab-item.layui-show > div:nth-child(1) > div.layui-col-md2 > div > dl >dd[lay-value="CUATMSYTP201911220003"]']
    # 整车产品
    choose_product_zc= ['css','#layui-tab-content01 > div.layui-tab-item.layui-show > div:nth-child(1) > div.layui-col-md2 > div > dl >dd[lay-value="CUATMSYTP202001060001"]']
    # 输入整车\铁水数量
    complete_vehicle_quality=['xpath','// *[starts-with(@id,"inputVariable")]']

    unit_price = ['xpath','// *[starts-with(@id,"variable_name")]']
    # 铁水产品
    choose_product_ts= ['css','#layui-tab-content01 > div.layui-tab-item.layui-show > div:nth-child(1) > div.layui-col-md2 > div > dl >dd[lay-value="CUATMSYTP201911220005"]']
    # 零担
    choose_product_ld= ['css','#layui-tab-content01 > div.layui-tab-item.layui-show > div:nth-child(1) > div.layui-col-md2 > div > dl >dd[lay-value="CUATMSYTP201910280002"]']
    # 用于通过产品ID选择其他零担产品
    choose_product_ld2= ['css','#layui-tab-content01 > div.layui-tab-item.layui-show > div:nth-child(1) > div.layui-col-md2 > div > dl >dd[lay-value="CUATMSYTP201910280002"]']
    # 整车零担提货
    choose_product_ld_th = ['css','#layui-tab-content01 > div.layui-tab-item.layui-show > div:nth-child(1) > div.layui-col-md2 > div > dl >dd[lay-value="CUATMSYTP202005280001"]']
    # 整车零担提货
    choose_product_ld_sh = ['css','#layui-tab-content01 > div.layui-tab-item.layui-show > div:nth-child(1) > div.layui-col-md2 > div > dl >dd[lay-value="CUATMSYTP202005280002"]']
    # 整车0421
    choose_product_zc_0421 = ['css','#layui-tab-content01 > div.layui-tab-item.layui-show > div:nth-child(1) > div.layui-col-md2 > div > dl >dd[lay-value="CUATMSYTP202001060001"]']
    # 零担0529
    choose_product_ld_0529 = ['css','#layui-tab-content01 > div.layui-tab-item.layui-show > div:nth-child(1) > div.layui-col-md2 > div > dl >dd[lay-value="CUATMSYTP202005290002"]']

    # 提交
    submit = ['xpath', '//*[starts-with(@id,"layui-layer")]/div[3]/a[text()="提交"]']
    #提交弹框
    submit_elastic_frame =['xpath',"//span[@class='layui-layer-setwin']/parent::div//div[@class='layui-layer-content layui-layer-padding']"]
    # 运输总金额
    totalfee=['xpath','//*[@id="transportTotalFee"]']

    # -------------------子订单
    # 子订单列表
    sub_order_frame =['xpath', '//iframe[starts-with(@src,"/oss/oms/TBClientOrder/innerList")]']
    # 子订单号
    sub_order = ['xpath','/html/body/div/div[2]/div/div[1]/div[2]/table/tbody/tr/td[2]/div']

    # 新增订单，客户订单号默认是取程序跑的时间，允许跑的时候输入
    # lg = 'T' 默认要登录   producttype   产品类型 , pcustomer_sales_no 销售单号,
    # pcustomer_no  客户订单号，默认传入时间, pweight  总重量, pvolume 总体积, pquantity  总件数,
    # complete_vehicle_quality  整车/铁水数量，默认是1; row参数是为了解决多进程导致订单号重复的问题
    def add_order(self,case=[],lg='T',producttype='LD',pcustomer_sales_no ='123120003',pcustomer_no= None,pweight='12',pvolume='110',\
                  pquantity='140',complete_vehicle_quality='1',shippingcode=None,receivingcode=None,row=None):
        # global COUNT=global COUNT+1
        # global COUNT=global COUNT+1
        # self.process_lock.acquire()
        self.lock.acquire()
        # global COUNT
        # COUNT += 1
        if pcustomer_no is None:
            print(pcustomer_no)
            print(lg)
            pcustomer_no = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))+"-"+str(row)
            # pcustomer_no = get_customerno()
            time.sleep(3)
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
            self.click(self.close_tab[0], self.close_tab[1])
            self.click(self.close_tab[0], self.close_tab[1])
            self.click(self.close_tab[0], self.close_tab[1])
            # 一级菜单
            self.click(self.order_manage_module[0], self.order_manage_module[1])
            # 二级菜单
            self.click(self.order_deal_with[0], self.order_deal_with[1])
            # 进入列表
            self.in_iframe(self.listframe[0], self.listframe[1])
            time.sleep(3)
            # 点击新增
            self.click(self.add[0], self.add[1])
            # 进入编辑页面框架
            self.in_iframe(self.editframe[0], self.editframe[1])
            # 进入直接点击，下拉是没有值的，这也是界面上确存的一个小BUG，所以暂时先强制等待5秒
            time.sleep(5)
            # self.implicitlty_wait(20)
            # 点击客户下拉框
            self.click(self.delivery_customer[0], self.delivery_customer[1])
            time.sleep(1)
            # 选择客户
            self.click(self.customer[0], self.customer[1])
            time.sleep(1)
            # 输入客户单号
            self.clear(self.customer_no[0], self.customer_no[1])
            self.send(self.customer_no[0], self.customer_no[1], pcustomer_no)
            # 订单类型下拉框
            self.click(self.customer_type[0], self.customer_type[1])
            # 选择订单类型
            self.click(self.customtype[0], self.customtype[1])
            # 输入销售单号
            self.send(self.customer_sales_no[0], self.customer_sales_no[1], pcustomer_sales_no)
            # 输入重量
            self.send(self.weight[0], self.weight[1], pweight)
            # 输入体积
            self.send(self.volume[0], self.volume[1], pvolume)
            # 输入件数
            self.send(self.quantity[0], self.quantity[1], pquantity)
            # 业务类型下拉
            self.click(self.business_type[0], self.business_type[1])
            time.sleep(1)
            # 选择业务类型
            self.click(self.bustype[0], self.bustype[1])
            # 滚动页面
            self.scroll_to_terminal(self.shipping_type[0], self.shipping_type[1])
            # 运输方式下拉
            self.click(self.shipping_type[0], self.shipping_type[1])
            # 选择运输方式
            self.click(self.shipping_type_value[0], self.shipping_type_value[1])
            # 提货上门
            self.click(self.pickup[0], self.pickup[1])
            # 提货方式下拉
            self.click(self.pickup_type[0], self.pickup_type[1])
            # 选择提货方式
            self.click(self.picktype[0], self.picktype[1])

            # 发货地址码下拉
            self.click(self.shipping_address_code[0], self.shipping_address_code[1])
            # 选择发货地址码
            self.shippingcode[1] = '#tpModule > div:nth-child(3) > div.layui-col-md2.myWidth-16 > div > dl > dd[lay-value="{}"]'.format(shippingcode) if shippingcode is not None else self.shippingcode[1]
            time.sleep(3)
            self.click(self.shippingcode[0], self.shippingcode[1])
            # 目的是加载过快，选项没有出来
            time.sleep(5)
            # 收货地址码下拉
            self.click(self.receiving_address_code[0], self.receiving_address_code[1])
            # 选择收货地址码
            self.receivingcode[1]='#tpModule > div:nth-child(5) > div.layui-col-md2.myWidth-16 > div > dl > dd[lay-value="{}"]'.format(receivingcode) if receivingcode is not None else self.receivingcode[1]
            print('输出收货地址',self.receivingcode[1])
            time.sleep(3)
            self.click(self.receivingcode[0], self.receivingcode[1])
            # 滚动页面
            # self.scroll()
            time.sleep(2)
            # js = "var q=document.documentElement.scrollTop=1300"
            # self.driver.execute_script(js)
            # 滚动到产品选择
            self.scroll_to_terminal(self.product[0], self.product[1])
            # 进入产品选择
            self.click(self.product[0], self.product[1])
            # 产品下拉
            self.click(self.prductlist[0], self.prductlist[1])
            time.sleep(1)
            if producttype.upper()=='KD':
                # 选择快递产品
                self.click(self.choose_product[0], self.choose_product[1])
            elif producttype.upper()=='ZC':
                # 选择整车产品
                self.click(self.choose_product_zc[0], self.choose_product_zc[1])
                self.send(self.complete_vehicle_quality[0],self.complete_vehicle_quality[1],complete_vehicle_quality)
                # 点击一下单价，目的是让费用重算
                self.click(self.unit_price[0],self.unit_price[1])

            elif producttype.upper()=='TS':
                # 选择铁水产品
                self.click(self.choose_product_ts[0], self.choose_product_ts[1])
                self.send(self.complete_vehicle_quality[0], self.complete_vehicle_quality[1], complete_vehicle_quality)
                # 点击一下单价，目的是让费用重算
                self.click(self.unit_price[0], self.unit_price[1])

            elif producttype.upper()=='LD':
                # 选择零担产品
                self.click(self.choose_product_ld[0], self.choose_product_ld[1])
            elif producttype.upper()=='LDTH':
                # 选择零担提货产品
                self.click(self.choose_product_ld_th[0], self.choose_product_ld_th[1])
            elif producttype.upper()=='LDSH':
                # 选择零担提送货产品
                self.click(self.choose_product_ld_sh[0], self.choose_product_ld_sh[1])
            elif producttype.upper()=='LD_0529':
                # 选择零担0529
                self.click(self.choose_product_ld_0529[0], self.choose_product_ld_0529[1])
            elif producttype.upper()=='ZC_0421':
                # 选择整车0421
                self.click(self.choose_product_zc_0421[0], self.choose_product_zc_0421[1])
                self.send(self.complete_vehicle_quality[0], self.complete_vehicle_quality[1], complete_vehicle_quality)
                # 点击一下单价，目的是让费用重算
                self.click(self.unit_price[0], self.unit_price[1])
            # 输入产品id,id共性都是有TP（应该是运输的意思），没有考虑整车铁水等选择产品后还有其他操作的情况，这是方便添加零担产品的
            elif 'TP' in producttype.upper():
                self.choose_product_ld2[1]='#layui-tab-content01 > div.layui-tab-item.layui-show > div:nth-child(1) > div.layui-col-md2 > div > dl >dd[lay-value="{}"]'.format(
                    producttype)
                self.click(self.choose_product_ld2[0], self.choose_product_ld2[1])

            else:
                self.text1 = u'产品输入有问题'
                return self.text1
            time.sleep(2)
            # 退出框架
            self.out_iframe()
            # 进入列表框架
            self.in_iframe(self.listframe[0], self.listframe[1])
            print('进入框架哈哈')
            time.sleep(5)
            # 点击提交
            self.click(self.submit[0], self.submit[1])
            print('点击提交！')
            # 运行脚本发现有时候已经点击了提交，但是系统没有反应，需要进行第二次点击，
            # 降低失败的概率,不要截图，截图会占用时间，导致后面提交返回的结果定位不到!
            if self.element(self.submit[0], self.submit[1],time=1,screenshot='n')!='fail':
                self.click(self.submit[0], self.submit[1])
                print('第二次点击提交！')
            else:
                pass


            # 进入编辑页面框架
            self.in_iframe(self.editframe[0], self.editframe[1])
            # self.scroll()
            # 获取提交订单弹框提示语，可用于断言
            text2 = self.element(self.submit_elastic_frame[0], self.submit_elastic_frame[1],time=30).text
            print(text2)
            rpcustomer_no = pcustomer_no if text2==u'新增订单成功' else 'fail'
            print('订单号:{},返回结果：{}'.format(rpcustomer_no,text2))
            self.out_iframe()
            self.in_iframe(self.listframe[0], self.listframe[1])
            time.sleep(3)
            self.out_iframe()
        except Exception as e:
           Mylog().my_log().error('订单新增出错，原因如下：'.format(e))
           text2= u'订单创建出错！'
           rpcustomer_no='fail'
           print(pcustomer_no)
           print(lg)
        # self.quit()
        print(text2,rpcustomer_no)
        return text2,rpcustomer_no

    # 删除订单不输入客户订单号，默认是先跑一遍创建订单方法，删除新建的订单；
    # 删除成功与失败要分开定位，t表示要定位删除成功的，其他则是定位删除失败的（成功与失败元素不相同）
    # 订单删除
    # pcustomer_no 客户订单号，默认是时间
    def del_order(self,lg='t',case=[],pcustomer_no=None,row=None):
        try:
            if pcustomer_no is None:
                text,rpcustomer_no = self.add_order(row=row,case=case)
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
            self.click(self.close_tab[0], self.close_tab[1])
            self.click(self.close_tab[0], self.close_tab[1])
            self.click(self.close_tab[0], self.close_tab[1])
            # 一级菜单
            self.click(self.order_manage_module[0], self.order_manage_module[1])
            # 二级菜单
            self.click(self.order_deal_with[0], self.order_deal_with[1])
            time.sleep(1)

            # 当前打开的所有窗口
            windows = self.driver.window_handles
            # 转换到最新打开的窗口
            self.driver.switch_to.window(windows[-1])
            # 进入列表
            # self.in_iframe(self.listframe[0], self.listframe[1])
            # time.sleep(3)
            # 进入列表
            self.in_iframe(self.listframe[0], self.listframe[1])
            time.sleep(3)
            # 列表查询，客户过滤下拉
            self.click(self.customer_filtering[0], self.customer_filtering[1])
            time.sleep(2)
            # 列表查询，选择要过滤的客户
            with open(os.path.join(BASE_PATH, 'yamlconfig.yml'), mode='r',encoding='utf-8') as f:
                # load_all 读取多个文档
                l = [i for i in yaml.load_all(f)]
            customer_filtering_value = ['xpath','//*[@id="TBClientOrder_queryTable"]/tbody/tr[1]/td[1]/div/div/dl/dd[text()="{}"]'.format(l[1]['customer_filtering_value'])]
            self.click(customer_filtering_value[0],customer_filtering_value[1])
            time.sleep(2)
            # 列表查询，客户订单号过滤
            self.send(self.customer_no_filtering_input[0], self.customer_no_filtering_input[1], self.pcustomer_no)
            # 点击查询
            self.click(self.select_click[0], self.select_click[1])
            # 列表订单复选框
            self.click(self.order_check_box[0], self.order_check_box[1])
            # 删除按钮
            self.click(self.delete_button[0], self.delete_button[1])
            # 确定删除
            self.click(self.accept_delete[0], self.accept_delete[1])
            try:
                # 定位删除失败的提示语，若定位不到证明成功,这么处理的原因是成功与失败的提示框元素一样，但是弹出的时间不一样，所以无法准确定位
                self.text = self.element(self.delete_fail_tips[0], self.delete_fail_tips[1],time=8,screenshot='n').text
                print(self.text)
            except Exception:
                # 也可以考虑查询数据库判断是否删除成功，并且测试删除成功的情况比失败情况少，可以暂时先这么处理
                self.text = u'删除成功'
                print(self.text)
            self.out_iframe()
        except Exception:
            Mylog().my_log().error('删除订单出错!')
            self.text=u'删除订单出错!'
        # self.quit()
        return self.text

    # 编辑，不输入客户订单号，默认是先跑一遍创建订单方法，编辑新建的订单
    # pcustomer_no 客户订单号，默认时间, pweight 总重量, pvolume 重体积, pquantity 总件数，有默认值
    def edit_order(self,lg='t',case=[],pcustomer_no=None,pweight=None,pvolume=None,pquantity=None,row=None):
        try:
            if pcustomer_no is None:
                text, rpcustomer_no = self.add_order(row=row,case=case)
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
            self.click(self.close_tab[0], self.close_tab[1])
            self.click(self.close_tab[0], self.close_tab[1])
            self.click(self.close_tab[0], self.close_tab[1])
            time.sleep(3)
            # 一级菜单
            self.click(self.order_manage_module[0], self.order_manage_module[1])
            # 二级菜单
            self.click(self.order_deal_with[0], self.order_deal_with[1])
            time.sleep(1)
            # 进入列表
            self.in_iframe(self.listframe[0], self.listframe[1])
            time.sleep(3)
            # 列表查询，客户过滤下拉
            self.click(self.customer_filtering[0], self.customer_filtering[1])
            time.sleep(2)
            # 列表查询，选择要过滤的客户
            self.click(self.customer_filtering_value[0], self.customer_filtering_value[1])
            time.sleep(2)
            # 列表查询，客户订单号过滤
            self.send(self.customer_no_filtering_input[0], self.customer_no_filtering_input[1], self.pcustomer_no)
            # time.sleep(5)
            # 点击查询
            self.click(self.select_click[0], self.select_click[1])
            # time.sleep(3)
            # 列表订单复选框
            self.click(self.order_check_box[0], self.order_check_box[1])
            time.sleep(2)
            # 编辑按钮
            self.click(self.update[0], self.update[1])
            # 判断是否出现失败弹框
            if self.element(self.update_fail[0],self.update_fail[1],time=5,screenshot='n')!='fail':
                # print('编辑失败')
                self.text1 = self.element(self.update_fail[0],self.update_fail[1]).text
                return self.text1
            else:
                pass

            # 循环判断金额不为0才点击提交，否则直接进入提交，有些信息没有加载完，会报错。这是页面设计有问题
            for i in range(1, 10):
                try:
                    # 没有定位到总金额元素，继续循环
                    if self.element(self.totalfee[0], self.totalfee[1], time=2, screenshot='f') == 'fail':
                        continue
                    # 定位到总金额元素，但是费用为0，这种情况下提交会有问题，继续循环
                    elif self.element(self.totalfee[0], self.totalfee[1], time=3, screenshot='f').text == '0':
                        continue
                    # 定位到总金额元素，费用不为0则跳出循环
                    else:
                        text=self.element(self.totalfee[0], self.totalfee[1], time=3, screenshot='f').text
                        print(text)
                        break
                except Exception as e:
                    print("出错了")
                    Mylog().my_log().error('出错了', e)

            # 重量体积件数有输入值，则是要修改这部分内容，否则直接进入提交，若线路与产品需要修改，参照以下内容加代码逻辑
            if pweight is not None or pvolume is not None or pquantity is not None:
                self.in_iframe(self.editframe[0], self.editframe[1])
                time.sleep(5)
                if pweight is not None:
                    self.clear(self.weight[0], self.weight[1])
                    # 输入重量
                    self.send(self.weight[0], self.weight[1], pweight)
                    time.sleep(2)
                else:
                    print('重量没有改变！')
                if pvolume is not None:
                    # 输入体积
                    self.clear(self.volume[0], self.volume[1])
                    # 输入件数
                    self.send(self.volume[0], self.volume[1], pvolume)
                    time.sleep(2)
                else:
                    print('体积没有改变！')

                if pquantity is not None:
                    self.clear(self.quantity[0], self.quantity[1])
                    self.send(self.quantity[0], self.quantity[1], pquantity)
                    time.sleep(2)
                else:
                    print('件数没有改变！')
                # 滚动到产品栏
                self.scroll_to_terminal(method=self.product[0],param=self.product[1])
                time.sleep(2)
                # 进入产品选择
                self.click(self.product[0], self.product[1])
                # 产品下拉
                self.click(self.prductlist[0], self.prductlist[1])
                # 选择快递产品
                self.click(self.choose_product[0], self.choose_product[1])
                time.sleep(5)
                # 退出框架
                self.out_iframe()
                # 进入列表框架
                self.in_iframe(self.listframe[0], self.listframe[1])
                time.sleep(5)
            else:
                print('重量体积件数没有修改！')

            # 点击提交
            self.click(self.submit[0], self.submit[1])
            # 进入编辑页面框架
            self.in_iframe(self.editframe[0], self.editframe[1])
            # self.scroll()
            # 获取提交订单弹框提示语，可用于断言
            self.text1 = self.element(self.submit_elastic_frame[0], self.submit_elastic_frame[1],time=30).text
            print(self.text1)
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
            self.click(self.close_tab[0], self.close_tab[1])
            self.click(self.close_tab[0], self.close_tab[1])
            self.click(self.close_tab[0], self.close_tab[1])
            # 一级菜单
            self.click(self.order_manage_module[0], self.order_manage_module[1])
            # 二级菜单
            self.click(self.order_deal_with[0], self.order_deal_with[1])
            time.sleep(1)
            # # 进入订单列表
            # self.in_iframe(self.listframe[0], self.listframe[1])
            # time.sleep(1)
            # 进入订单列表
            self.in_iframe(self.listframe[0], self.listframe[1])
            time.sleep(2)
            # 列表查询，客户过滤下拉
            self.click(self.customer_filtering[0], self.customer_filtering[1])
            time.sleep(2)
            # 列表查询，选择要过滤的客户
            value='#TBClientOrder_queryTable > tbody > tr:nth-child(1) > td:nth-child(1) > div > div > dl > dd[lay-value="{}"]'.format(customer)
            print(value)
            customer_filtering_value_new=['css',value]
            self.click(customer_filtering_value_new[0], customer_filtering_value_new[1])
            time.sleep(2)
            # 列表查询，客户订单号过滤
            self.clear(self.customer_no_filtering_input[0], self.customer_no_filtering_input[1])
            time.sleep(1)
            self.send(self.customer_no_filtering_input[0], self.customer_no_filtering_input[1], pcustomer_no)
            # time.sleep(5)
            # 点击查询
            self.click(self.select_click[0], self.select_click[1])
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
            self.click(self.order_check_box[0], self.order_check_box[1])
            # 点击子订单按钮
            self.click(self.sub_order_button[0],self.sub_order_button[1])
            time.sleep(3)
            self.scroll()
            # 进入子订单列表
            self.in_iframe(self.sub_order_frame[0],self.sub_order_frame[1])
            # 获取子订单号，text
            text=self.element(self.sub_order[0],self.sub_order[1]).text
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
        # 参数化订单号：
        # 获取锁
        self.lock.acquire()
        with open(os.path.join(BASE_PATH, 'yamlconfig.yml'), 'r', encoding='utf-8') as f:
            filepath = [i for i in yaml.load_all(f)][1]['filepath']
            # 对订单号进行参数化并获取订单行数，目的是导入的完成时间会因为订单数量不同，时间不同，所以等待时间要乘行号这个系数
            row = DataOperate().order_upload(filepath, copydata=copydata)
            if row==1:
                text = u'失败，订单行数为0，无法导入'
                print(text)
                return text
            else:
                pass
            # print('订单导入打印返回的行数',row)
        try:

            # 登录
            self.login(username=case[-4],password=case[-3])
            # 关闭所有标签
            self.click(self.close_tab[0], self.close_tab[1])
            self.click(self.close_tab[0], self.close_tab[1])
            self.click(self.close_tab[0], self.close_tab[1])
            # 一级菜单
            self.click(self.order_manage_module[0], self.order_manage_module[1])
            # 二级菜单
            self.click(self.order_deal_with[0], self.order_deal_with[1])
            time.sleep(1)
            # 进入列表
            self.in_iframe(self.listframe[0], self.listframe[1])
            time.sleep(3)

            # 点击上传按钮
            # print('点击上传前')
            self.click(self.upload1[0], self.upload1[1])
            # print('点击上传')
            # 点击确实要上传文件
            self.click(self.update_determine[0], self.update_determine[1])
            # 进入文件弹窗列表
            self.in_iframe(self.file_iframe[0], self.file_iframe[1])
            # 添加文件
            self.click(self.add_file[0], self.add_file[1])
            # 选择文件
            # 由于selenuim 不能定位系统上传窗口，要借助AutoIt工具去定位，文件也要参数化
            # print('导入的地址',filepath)
            os.system(r"E:\software\python3.8.3\UiAuto\file\upload.exe %s"%filepath)
            # time.sleep(3)
            self.click(self.add_file_submit[0],self.add_file_submit[1])
            time.sleep(3)

            # 退出框架
            self.out_iframe()
            # 进入列表框架
            self.in_iframe(self.listframe[0], self.listframe[1])
            # 提交附件
            self.click(self.submit_file[0], self.submit_file[1])
            # print('提交 777')
            # 点击提交附件后再释放锁
            self.lock.release()
            # 进入导入进程窗口列表
            time.sleep(2)
            self.in_iframe(self.import_frame[0],self.import_frame[1])
            # print('进入777')
            # 导入结果提示语
            try:
                result=self.element(method=self.import_result_button[0], param=self.import_result_button[1], time=row*7,screenshot='n')
                # print('进入888')
                if result!='fail':
                    # 失败原因有两种方式 ，一种是界面输出，另外一种是下载文件
                    if result.text!='导入成功':
                        # 下载文件查看失败原因
                        fail_download= self.element(method=self.import_fail_download[0], param=self.import_fail_download[1], screenshot='n')
                        # print('进入9999')
                        if fail_download !='fail':
                            # 下载错误
                            self.click(method=self.import_fail_download[0], param=self.import_fail_download[1])
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
                            # 定位界面的错误原因
                            text=self.element(self.import_fail_reason[0],self.import_fail_reason[1]).text
                    else:
                        # 结果不是失败
                        text = result.text
                    # 退出框架
                    self.out_iframe()
                    # 进入列表框架
                    self.in_iframe(self.listframe[0], self.listframe[1])
                    # 关闭弹窗
                    self.click(self.import_hide[0], self.import_hide[1], time1=3)
                else:
                    text=u'没有定位到导入进程窗口！'
            except Exception:
                text = u'订单导入失败，但下载错误内容出错！'
        except Exception as e:
            Mylog().my_log().error('上传失败！',e)
            text=u'上传出错！'
        print(text)
        self.quit()
        return text

    # 订单下载 LG 是判断是否要登录，filter_lg, 判断是否要登录  customer都是客户，filepath 是文件路径，有默认值
    # 20201012 应该再加一个逻辑，导出的文件记录数应该与界面的一致
    def order_download(self,case=[],lg='T',pcustomer_no='',filter_lg='f',customer='584.00',filepath=FILE):

        try:
            # 登录
            self.login(username=case[-4], password=case[-3])
            self.filter(case=case, lg=filter_lg, pcustomer_no=pcustomer_no, customer=customer)
            # time.sleep(5)
            # 点击导出按钮
            self.click(self.outport[0],self.outport[1])
            # 进入点击下载框架
            # self.in_iframe(self.outport_frame[0],self.outport_frame[1])
            # 这么做的目的是没有进入框架时就不再执行后面语句，因为设置等待的时间太久，但是不这么设置，
            # 前面出错好像也不往后执行了
            if self.in_iframe(self.outport_frame[0],self.outport_frame[1])=='2':
                text =u'导出出错啦！'
                return text
            else:
                # print('进入导出下载框架')
                # 通过定位此提示语，来确定是否下载完成，因为就算没有下载完成，代码仍能点击下载按钮,等待10分钟
                self.click(self.file_download_end[0], self.file_download_end[1], time1=600)
                # print('已经生成文件！')
                re_dirnum = len(
                    [lists for lists in os.listdir(filepath) if os.path.isdir((os.path.join(filepath, lists)))])
                re_firenum = len(
                    [lists for lists in os.listdir(filepath) if os.path.isfile((os.path.join(filepath, lists)))])
                print(re_firenum,re_dirnum)
                # 点击下载按钮
                self.click(method=self.outport_load[0], param=self.outport_load[1])
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
                self.in_iframe(self.listframe[0], self.listframe[1])
                time.sleep(3)
                # 关闭下载弹窗
                self.click(self.export_close[0],self.export_close[1])

        except Exception :
            print('导出出错!')
            text=u'导出出错！'
        self.quit()
        return text


# class OrderPage(BasePage):
#     # 系统首页页签
#     close_tab = ['xpath', '//*[@id="index_tabs"]/div[1]/div[4]/table/tbody/tr/td[3]/a/span']
#     # 订单管理模块
#     order_manage_module = ['xpath', '//td[@title="订单管理"]/child::a[1]']
#     # 订单处理
#     order_deal_with = ['xpath', '//span[text()="订单处理_运输"]/parent::div[starts-with(@id,"_easyui_tree")]']
#     def atest(self):
#         self.login()
#         # 一级菜单
#         self.click(self.order_manage_module[0], self.order_manage_module[1])
#         # 二级菜单
#         self.click(self.order_deal_with[0], self.order_deal_with[1])
#         # 进入列表
#         # self.in_iframe(self.listframe[0], self.listframe[1])
#         time.sleep(3)
#         # 关闭所有标签
#         # self.context_choice(self.tab[0], self.tab[1], index=['down', 'down', 'down', 'down'])
#         # self.context_choice(self.tab[0], self.tab[1], index=['ENTER'])
#         self.click(self.close_tab[0],self.close_tab[1])
#         self.click(self.close_tab[0],self.close_tab[1])
#         self.click(self.close_tab[0],self.close_tab[1])
#         print('右键')
#         time.sleep(13)
#         # # 一级菜单
#         # self.click(self.order_manage_module[0], self.order_manage_module[1])
#         # # 二级菜单
#         # self.click(self.order_deal_with[0], self.order_deal_with[1])
#         # time.sleep(1)


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