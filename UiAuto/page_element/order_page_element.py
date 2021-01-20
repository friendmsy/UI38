# -*- coding: utf-8 -*-
# @Time    : 2020/12/4 14:56
# @Author  : msy
# @File    : order_page_element.py
# @Software: PyCharm

from common.general import *
from config import *
from common.log import *
import time
from common.data_operate import *
import threading
# import lock
# from multiprocessing import Lock,Process

class OrderPageE(BasePage):

    #----------------------------------菜单

    # 订单管理模块
    def click_order_manage_module(self,method='xpath',param='//td[@title="订单管理"]/child::a[1]',time=20,*args,**kwargs):
    # def click_order_manage_module(self,method='id',param='1b20e9c60fb4fbb9eec63a6c0631111',time=20,*args,**kwargs):
        self.click(method=method,param=param,time1=time)
    # 订单处理
    def click_order_deal_with(self,method='xpath',param='//span[text()="订单处理_运输"]/parent::div[starts-with(@id,"_easyui_tree")]',time=20,*args,**kwargs):
    # def click_order_deal_with(self,method='css',param='#_easyui_tree_44 > span.tree-title',time=20,*args,**kwargs):
        self.click(method=method,param=param,time1=time)

    # ---------------------------------订单管理列表
    # 菜单列表iframe
    def frame_listframe(self,method='xpath',param='//iframe[@src="/oss/oms/TBClientOrder/todoList"]',*args,**kwargs):
        self.in_iframe(method=method,param=param)

    # 系统首页页签
    def click_close_tab(self,method='xpath',param='//*[@id="index_tabs"]/div[1]/div[4]/table/tbody/tr/td[3]/a/span',time=20,*args,**kwargs):
        self.click(method=method,param=param,time1=time)
    # 新增
    def click_add (self,method='xpath',param='//*[@id="create"]',time=20,*args,**kwargs):
        self.click(method=method,param=param,time1=time)
    # 子单按钮
    def click_sub_order_button(self,method='css',param='#queryInner',time=20,*args,**kwargs):
        self.click(method=method,param=param,time1=time)

    # 编辑
    def click_update(self,method='css',param='#myUpdate',time=20,*args,**kwargs):
        self.click(method=method,param=param,time1=time)
    # 上传失败
    def click_update_fail(self,method='xpath',param='//*[starts-with(@id,"layui-layer")]//following-sibling::div[@class="layui-layer-content layui-layer-padding"]',time=20,*args,**kwargs):
        self.click(method=method,param=param,time1=time)
    def element_update_fail(self,method='xpath',param='//*[starts-with(@id,"layui-layer")]//following-sibling::div[@class="layui-layer-content layui-layer-padding"]',time=20,*args,**kwargs):
        return method,param
    # 上传按钮
    def click_upload1 (self,method='css',param='button#importTp:nth-child(8)',time=20,*args,**kwargs):
        self.click(method=method,param=param,time1=time)
    # 导入成功提示语
    def click_upload_success (self,method='xpath',param='//div[text()="导入成功"]',time=20,*args,**kwargs):
        self.click(method=method,param=param,time1=time)

    # 导入失败定位下载按钮提示语
    def click_upload_fail (self,method='css',param='div.layui-layer-content.layui-layer-padding > a>span',time=20,*args,**kwargs):
        self.click(method=method,param=param,time1=time)

    # 导入失败下载
    def click_upload_fail_load (self,method='css',param='div.layui-layer-content.layui-layer-padding > a',time=20,*args,**kwargs):
        self.click(method=method,param=param,time1=time)

    # 列表查询，客户过滤下拉
    def click_customer_filtering (self,method='css',param='#TBClientOrder_queryTable > tbody > tr:nth-child(1) > td:nth-child(1) > div > div > div > input',time=20,*args,**kwargs):
        self.click(method=method,param=param,time1=time)

    # 列表查询，选择要过滤的客户(执行删除时，过滤客户不稳定，有时会执行到下一个客户，但定位时确实是定位到uat客户)
    def click_customer_filtering_value (self,method='css',param='#TBClientOrder_queryTable > tbody > tr:nth-child(1) > td:nth-child(1) > div > div > dl > dd[lay-value="UATmsy"]',time=20,*args,**kwargs):
        self.click(method=method,param=param,time1=time)

    # 列表查询，客户订单号过滤
    def send_customer_no_filtering_input (self,method='css',param='#myClientOrderNo',send=None,time=20,*args,**kwargs):
        self.send(method=method,param=param,send=send,time=time)
    def clear_customer_no_filtering_input (self,method='css',param='#myClientOrderNo',time=20,*args,**kwargs):
        self.clear(method=method,param=param)
    # 点击查询
    def click_select_click (self,method='css',param='#TBClientOrder_form > div > div:nth-child(3) > div:nth-child(1) > button',time=20,*args,**kwargs):
        self.click(method=method,param=param,time1=time)

    # 列表订单复选框
    def click_order_check_box (self,method='css',param='body > div.weadmin-body > div > div.layui-table-box > div.layui-table-fixed.layui-table-fixed-l > div.layui-table-body > table > tbody > tr > td > div > div > i',time=20,*args,**kwargs):
        self.click(method=method,param=param,time1=time)

   # --------------------------------删除

    # 删除按钮
    def click_delete_button (self,method='css',param='#remove',time=20,*args,**kwargs):
        self.click(method=method,param=param,time1=time)

    #确定删除
    def click_accept_delete (self,method='xpath',param='//*[starts-with(@id,"layui-layer")]/div[3]/a[1][text()="确定"]',time=20,*args,**kwargs):
        self.click(method=method,param=param,time1=time)

    # 确认弹窗提示语
    def click_is_delete (self,method='xpath',param='//*[starts-with(@id,"layui-layer")]/div[2]',time=20,*args,**kwargs):
        self.click(method=method,param=param,time1=time)

    #删除失败提示语
    def click_delete_fail_tips (self,method='xpath',param='//*[starts-with(@id,"layui-layer")]/div[2][contains(text(),"失败")]',time=20,*args,**kwargs):
        self.click(method=method,param=param,time1=time)
    def element_delete_fail_tips (self,method='xpath',param='//*[starts-with(@id,"layui-layer")]/div[2][contains(text(),"失败")]',time=20,*args,**kwargs):
        return method,param

    #删除成功提示语
    def click_delete_success_tips (self,method='xpath',param='//*[starts-with(@id,"layui-layer")]/div[text()="删除成功！"]',time=20,*args,**kwargs):
        self.click(method=method,param=param,time1=time)

    # -----------------------------------------导入
    def click_update_determine (self,method='xpath',param='//*[starts-with(@id,"layui-layer")]/div[3]/a[1]',time=20,*args,**kwargs):
        self.click(method=method,param=param,time1=time)

    # 提交附件
    def click_submit_file (self,method='css',param='div.layui-layer-btn.layui-layer-btn- > a.layui-layer-btn0',time=20,*args,**kwargs):
        self.click(method=method,param=param,time1=time)

    # 导入弹窗列表
    def frame_file_iframe (self,method='xpath',param='//*[starts-with(@id,"layui-layer-iframe")]',*args,**kwargs):
        self.in_iframe(method=method,param=param)

    # 添加文件
    def click_add_file (self,method='css',param='button#selectFile',time=20,*args,**kwargs):
        self.click(method=method,param=param,time1=time)

    # 上传文件
    def click_add_file_submit (self,method='css',param='button#uploadAction',time=20,*args,**kwargs):
        self.click(method=method,param=param,time1=time)

    # 导入窗口列表
    def frame_delete_success_tips (self,method='xpath',param='//*[starts-with(@id,"layui-layer-iframe")]',*args,**kwargs):
        self.in_iframe(method=method,param=param)

    # 导入结果按钮
    def click_import_result_button (self,method='xpath',param='//*[@id="processDiv"]/button',time=20,*args,**kwargs):
        self.click(method=method,param=param,time1=time)
    def element_import_result_button (self,method='xpath',param='//*[@id="processDiv"]/button',time=20,*args,**kwargs):
        return method,param

    def frame_import_frame (self,method='xpath',param='//*[starts-with(@id,"layui-layer-iframe")]',*args,**kwargs):
        self.in_iframe(method=method,param=param)

    # 导入界面输出报错原因
    def click_import_fail_reason (self,method='xpath',param='//*[@id="processDiv"]',time=20,*args,**kwargs):
        self.click(method=method,param=param,time1=time)
    def element_import_fail_reason (self,method='xpath',param='//*[@id="processDiv"]',time=20,*args,**kwargs):
        return method,param
    # 错误下载按钮
    def click_import_fail_download (self,method='xpath',param='//*[@id="processDiv"]/button[2]',time=20,*args,**kwargs):
        self.click(method=method,param=param,time1=time)
    def element_import_fail_download (self,method='xpath',param='//*[@id="processDiv"]/button[2]',time=20,*args,**kwargs):
        return method,param
    # 导入窗口关闭按钮
    def click_import_hide (self,method='xpath',param='//*[starts-with(@id,"layui-layer")]/div[3]/a',time=20,*args,**kwargs):
        self.click(method=method,param=param,time1=time)

    # -------------------------------导出
    # 导出按钮
    def click_outport (self,method='xpath',param='//*[starts-with(@id,"excelFile")][1]',time=20,*args,**kwargs):
        self.click(method=method,param=param,time1=time)

    # 导出下载框架
    def frame_outport_frame (self,method='xpath',param='//*[starts-with(@id,"layui-layer-iframe")]',*args,**kwargs):
        self.in_iframe(method=method,param=param)

    # 文件生成
    def click_file_download_end (self,method='xpath',param='//td[text()="文件已生成，请点击下载按钮进行下载！"]',time=20,*args,**kwargs):
        self.click(method=method,param=param,time1=time)

    # 下载
    def click_outport_load (self,method='css',param='Button#downloadBtn',time=20,*args,**kwargs):
        self.click(method=method,param=param,time1=time)

    # 关闭
    def click_export_close (self,method='xpath',param='//*[starts-with(@id,"layui-layer")]/div[3]/a[text()="关闭"]',time=20,*args,**kwargs):
        self.click(method=method,param=param,time1=time)


    # ---------------------------------编辑页面
    # 编辑页面iframe
    def frame_editframe (self,method='xpath',param='//iframe[@id="detailDiv"]/following::iframe[starts-with(@id,"layui-layer-iframe")]',*args,**kwargs):
        self.in_iframe(method=method,param=param)

    # 发货客户
    def click_delivery_customer (self,method='css',param='#objForm > div > div:nth-child(2) > div.layui-row > div:nth-child(2) > div > div > input',time=20,*args,**kwargs):
        self.click(method=method,param=param,time1=time)

    # 选择客户，uat客户
    def click_customer  (self,method='xpath',param='//form[@id="objForm"]/descendant::dd[@lay-value="UATmsy"]',time=20,*args,**kwargs):
        self.click(method=method,param=param,time1=time)

    # 客户单号
    def send_customer_no (self,method='xpath',param="//form[@id='objForm']/descendant::input[@name='clientOrderNo']",send=None,time=20,*args,**kwargs):
        self.send(method=method,param=param,send=send,time=time)
    def clear_customer_no (self,method='xpath',param="//form[@id='objForm']/descendant::input[@name='clientOrderNo']",*args,**kwargs):
        self.clear(method=method,param=param)

    # 客户订单类型下拉框
    def click_customer_type (self,method='css',param='#objForm > div > div:nth-child(2) > div.layui-row > div:nth-child(6) > div > div > input',time=20,*args,**kwargs):
        self.click(method=method,param=param,time1=time)

    # 选择订单类型
    def click_customtype (self,method='css',param='#objForm > div > div:nth-child(2) > div.layui-row > div:nth-child(6) > div > dl > dd[lay-value="ys28"]',time=20,*args,**kwargs):
        self.click(method=method,param=param,time1=time)

    # 客户销售单号
    def send_customer_sales_no (self,method='css',param='input[id="clientSalesNo"]',send=None,time=20,*args,**kwargs):
        self.send(method=method,param=param,send=send,time=time)

    # 重量
    def send_weight(self,method='css',param='input#totalWeight',send=None,time=20,*args,**kwargs):
        self.send(method=method,param=param,send=send,time=time)
    def clear_weight(self,method='css',param='input#totalWeight',*args,**kwargs):
        self.clear(method=method,param=param)

    # 体积
    def send_volume (self,method='css',param='input#totalVolume',send=None,time=20,*args,**kwargs):
        self.send(method=method,param=param,send=send,time=time)
    def clear_volume(self,method='css',param='input#totalWeight',*args,**kwargs):
        self.clear(method=method,param=param)

    # 件数
    def send_quantity(self,method='css',param='input#totalQty',send=None,time=20,*args,**kwargs):
        self.send(method=method,param=param,send=send,time=time)
    def clear_quantity(self,method='css',param='input#totalWeight',*args,**kwargs):
        self.clear(method=method,param=param)

    # 点击业务信息，目的是让编辑时费用重算
    def click_business_information(self, method='xpath', param='// div[text()= "业务信息"]', time=20,*args, **kwargs):
        self.click(method=method, param=param, time1=time)

    # 业务类型下拉框
    def click_business_type(self, method='css', param='#objForm > div > div:nth-child(4) > div:nth-child(2) > div:nth-child(2) > div > div > input', time=20,
                       *args, **kwargs):
        self.click(method=method, param=param, time1=time)

    # 选择业务类型
    def click_bustype(self, method='css', param='#objForm > div > div:nth-child(4) > div:nth-child(2) > div:nth-child(2) > div > dl > dd[lay-value="1"]', time=20,
                       *args, **kwargs):
        self.click(method=method, param=param, time1=time)

    #运输方式下拉
    def click_shipping_type(self, method='css', param='#tpModule > div:nth-child(2) > div:nth-child(2) > div > div > input', time=20,
                       *args, **kwargs):
        self.click(method=method, param=param, time1=time)

    def scroll_shipping_type(self, method='css', param='#tpModule > div:nth-child(2) > div:nth-child(2) > div > div > input',
                       *args, **kwargs):
        self.scroll_to_terminal(method=method, param=param)
    #运输方式值
    def click_shipping_type_value(self, method='css', param='#tpModule > div:nth-child(2) > div:nth-child(2) > div > dl > dd:nth-child(2)', time=20,
                       *args, **kwargs):
        self.click(method=method, param=param, time1=time)

    # 提货上门
    def click_pickup(self, method='css', param='#tpModule > div:nth-child(2) > div:nth-child(4) > div', time=20,
                       *args, **kwargs):
        self.click(method=method, param=param, time1=time)
    # 提货方式下拉框
    def click_pickup_type(self, method='css', param='#tpModule > div:nth-child(2) > div:nth-child(6) > div > div > input', time=20,
                       *args, **kwargs):
        self.click(method=method, param=param, time1=time)

    # 提货方式
    def click_picktype(self, method='css', param='#tpModule > div:nth-child(2) > div:nth-child(6) > div > dl > dd:nth-child(2)', time=20,
                       *args, **kwargs):
        self.click(method=method, param=param, time1=time)

    # 发货地址编码下拉框
    def click_shipping_address_code(self, method='css', param='#tpModule > div:nth-child(3) > div.layui-col-md2.myWidth-16 > div > div > input', time=20,
                       *args, **kwargs):
        self.click(method=method, param=param, time1=time)

    # 选择发货地址码
    def click_shippingcode(self, method='css', param='#tpModule > div:nth-child(3) > div.layui-col-md2.myWidth-16 > div > dl > dd[lay-value="test0701"]', time=20,
                       *args, **kwargs):
        self.click(method=method, param=param, time1=time)

    # 收货地址编码下拉框
    def click_receiving_address_code (self,method='xpath',param='//*[@id="tpModule"]/div[5]/div[1]/div/div/input',time=20,*args,**kwargs):
        self.click(method=method,param=param,time1=time)

    # 选择收货地址码
    def click_receivingcode (self,method='css',param='#tpModule > div:nth-child(5) > div.layui-col-md2.myWidth-16 > div > dl > dd[lay-value="test0702"]',time=20,*args,**kwargs):
        self.click(method=method,param=param,time1=time)

    # 产品栏
    def click_product (self,method='css',param='#layui-tab-title01 > li:nth-child(3)',time=20,*args,**kwargs):
        self.click(method=method,param=param,time1=time)
    def scroll_to_terminal_product (self,method='css',param='#layui-tab-title01 > li:nth-child(3)',time=20,*args,**kwargs):
        self.scroll_to_terminal(method=method,param=param)

    def scroll_product (self,method='css',param='#layui-tab-title01 > li:nth-child(3)',*args,**kwargs):
        self.scroll_to_terminal(method=method,param=param)

    def click_prductlist (self,method='css',param='#layui-tab-content01 > div.layui-tab-item.layui-show > div:nth-child(1) > div:nth-child(2) > div > div > input',time=20,*args,**kwargs):
        self.click(method=method,param=param,time1=time)

    # 选择产品
    def click_choose_product (self,method='css',param='#layui-tab-content01 > div.layui-tab-item.layui-show > div:nth-child(1) > div:nth-child(2) > div > dl >dd[lay-value="CUATMSYTP201911220003"]',time=20,*args,**kwargs):
        self.click(method=method,param=param,time1=time)

    # 整车产品
    def click_choose_product_zc (self,method='css',param='#layui-tab-content01 > div.layui-tab-item.layui-show > div:nth-child(1) > div:nth-child(2) > div > dl >dd[lay-value="CUATMSYTP202001060001"]',time=20,*args,**kwargs):
        self.click(method=method,param=param,time1=time)

    # 输入整车\铁水数量
    def send_complete_vehicle_quality (self,method='xpath',param='// *[starts-with(@id,"inputVariable")]',send=None,time=20,*args,**kwargs):
        self.send(method=method,param=param,send=send,time=time)
    complete_vehicle_quality=['xpath','// *[starts-with(@id,"inputVariable")]']
    def click_unit_price (self,method='xpath',param='// *[starts-with(@id,"variable_name")]',time=20,*args,**kwargs):
        self.click(method=method,param=param,time1=time)

    # 铁水产品
    def click_choose_product_ts (self,method='css',param='#layui-tab-content01 > div.layui-tab-item.layui-show > div:nth-child(1) > div:nth-child(2) > div > dl >dd[lay-value="CUATMSYTP201911220005"]',time=20,*args,**kwargs):
        self.click(method=method,param=param,time1=time)

    # 零担
    def click_choose_product_ld (self,method='css',param='#layui-tab-content01 > div.layui-tab-item.layui-show > div:nth-child(1) >div:nth-child(2) > div > dl >dd[lay-value="CUATMSYTP201910280002"]',time=20,*args,**kwargs):
        self.click(method=method,param=param,time1=time)

    # 用于通过产品ID选择其他零担产品
    def click_choose_product_ld2 (self,method='css',param='#layui-tab-content01 > div.layui-tab-item.layui-show > div:nth-child(1) > div:nth-child(2) > div > dl >dd[lay-value="CUATMSYTP201910280002"]',time=20,*args,**kwargs):
        self.click(method=method,param=param,time1=time)

    # 整车零担提货
    def click_choose_product_ld_th (self,method='css',param='#layui-tab-content01 > div.layui-tab-item.layui-show > div:nth-child(1) > div:nth-child(2) > div > dl >dd[lay-value="CUATMSYTP202005280001"]',time=20,*args,**kwargs):
        self.click(method=method,param=param,time1=time)

    # 整车零担提货
    def click_choose_product_ld_sh (self,method='css',param='#layui-tab-content01 > div.layui-tab-item.layui-show > div:nth-child(1) > div:nth-child(2) > div > dl >dd[lay-value="CUATMSYTP202005280002"]',time=20,*args,**kwargs):
        self.click(method=method,param=param,time1=time)

    # 整车0421
    def click_choose_product_zc_0421 (self,method='css',param='#layui-tab-content01 > div.layui-tab-item.layui-show > div:nth-child(1) > div:nth-child(2) > div > dl >dd[lay-value="CUATMSYTP202001060001"]',time=20,*args,**kwargs):
        self.click(method=method,param=param,time1=time)

    # 零担0529
    def click_choose_product_ld_0529 (self,method='css',param='#layui-tab-content01 > div.layui-tab-item.layui-show > div:nth-child(1) > div:nth-child(2) > div > dl >dd[lay-value="CUATMSYTP202005290002"]',time=20,*args,**kwargs):
        self.click(method=method,param=param,time1=time)


    # 提交
    def click_submit (self,method='xpath',param='//*[starts-with(@id,"layui-layer")]/div[3]/a[text()="提交"]',time=20,*args,**kwargs):
        self.click(method=method,param=param,time1=time)
    def element_submit (self,method='xpath',param='//*[starts-with(@id,"layui-layer")]/div[3]/a[text()="提交"]',time=25,screenshot='n',*args,**kwargs):
        return method,param


    #提交弹框
    def click_submit_elastic_frame (self,method='xpath',param="//span[@class='layui-layer-setwin']/parent::div//div[@class='layui-layer-content layui-layer-padding']",time=20,*args,**kwargs):
        self.click(method=method,param=param,time1=time)

    def element_submit_elastic_frame(self, method='xpath',param="//span[@class='layui-layer-setwin']/parent::div//div[@class='layui-layer-content layui-layer-padding']",*args, **kwargs):
        # element=[method,param]  如果调用element方法，有问题，会导致点位不到，有可能是封装后，执行时间多了，导致弹窗已消失
        return method,param
    # 运输总金额
    def click_totalfee (self,method='xpath',param='//*[@id="transportTotalFee"]',time=20,*args,**kwargs):
        self.click(method=method,param=param,time1=time)
    def element_totalfee (self,method='xpath',param='//*[@id="transportTotalFee"]',time=20,*args,**kwargs):
        return method,param

    # -------------------子订单
    # 子订单列表
    def frame_sub_order_frame  (self,method='xpath',param='//iframe[starts-with(@src,"/oss/oms/TBClientOrder/innerList")]',*args,**kwargs):
        self.in_iframe(method=method,param=param)

    # 子订单号
    def click_sub_order (self,method='xpath',param='/html/body/div/div[2]/div/div[1]/div[2]/table/tbody/tr/td[2]/div',time=20,*args,**kwargs):
        self.click(method=method,param=param,time1=time)

    def element_sub_order (self,method='xpath',param='/html/body/div/div[2]/div/div[1]/div[2]/table/tbody/tr/td[2]/div',time=20,*args,**kwargs):
        return method,param

    # -------------------批量修改导入
    # 修改上传按钮
    def click_import_edit_button(self,method='css',param='#updataImportTp',time=10,*args,**kwargs):
        self.click(method=method, param=param, time1=time)

