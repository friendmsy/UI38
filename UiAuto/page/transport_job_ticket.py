# -*- coding: utf-8 -*-
# @Time    : 2020/6/12 8:54
# @Author  : msy
# @File    : transport_job_ticket.py
# @Software: PyCharm

from common.general import *
# from config import *
# from common.log import *
# import time
from common.data_operate import *
# from selenium.webdriver.common.keys import Keys
from page.order_page import OrderPage

# 手工作业单
class TransportJobTicket(BasePage):

    # 系统首页页签
    close_tab = ['xpath', '//*[@id="index_tabs"]/div[1]/div[4]/table/tbody/tr/td[3]/a/span']
    # ----------------------------------菜单
    # 运营管理模块
    operate_manage_module = ['xpath', '//td[@title="运营管理"]/child::a[1]']
    # 运输作业单
    transport_job = ['xpath', '//span[text()="运输作业单"]/parent::div[starts-with(@id,"_easyui_tree")]']

    # ---------------------------------订单管理列表
    # 菜单列表iframe
    listframe = ['xpath', '//iframe[@src="/oss/oms/jobOrderTp/list"]']
    # 新增
    add = ['css', 'div[lay-id="TBJobOrderTptable"]>div>div>button#create']
    # 提交
    sumbit=['css','div.layui-layer-btn.layui-layer-btn- > a.layui-layer-btn0']
    sumbit_success_tips=['css','#layui-layer2 > div']
    # 选中,列表第一个作业单
    check_box = ['css','body > div.weadmin-body > div[lay-id="TBJobOrderTptable"]> div.layui-table-box > div.layui-table-fixed.layui-table-fixed-l > div.layui-table-body > table > tbody > tr:nth-child(1) > td']
    job_detail_button = ['css','#addDetail']
    # 作业单过滤
    job_order_filter=['css','#jobNo']
    # 查询按钮
    select_click = ['css','#TBJobOrderTp_form > div > div:nth-child(3) > div:nth-child(1) > button']

    # ------------------------审核
    # 审核按钮
    approval_button = ['css', '#audit']
    # 确定审核
    accept_approval = ['xpath', '//*[starts-with(@id,"layui-layer")]/div[3]/a[1][text()="确定"]']
    # 审核失败提示语
    approval_fail_tips = ['xpath', '//*[starts-with(@id,"layui-layer")]/div[2][contains(text(),"失败")]']
    # 审核成功提示语
    approval_success_tips = ['xpath', '//*[starts-with(@id,"layui-layer")]/div[text()="审核成功"]']
    # ----------------------编辑页面
    # 编辑页面列表
    edit_frame=['xpath', '//iframe[starts-with(@src,"/oss/oms/jobOrderTp/detail")]']
    # 作业单号
    job_no=['css','form#objForm>table>tbody>tr>td:nth-child(2)>input#jobNo']
    # 供应商编号
    supplierid=['css','#objForm > table > tbody > tr:nth-child(1) > td:nth-child(4) > div > div > input']
    supplierid_value=['css','#objForm > table > tbody > tr:nth-child(1) > td:nth-child(4) > div > dl > dd:nth-child(2)']
    # 运输方式
    transporttype=['css','#objForm > table > tbody > tr:nth-child(1) > td:nth-child(6) > div > div > input']
    transporttype_value=['css','#objForm > table > tbody > tr:nth-child(1) > td:nth-child(6) > div > dl > dd:nth-child(1)']
    # 车型
    cartype = ['css','#objForm > table > tbody > tr:nth-child(2) > td:nth-child(2) > div > div > input']
    cartype_value = ['css','#objForm > table > tbody > tr:nth-child(2) > td:nth-child(2) > div > dl > dd:nth-child(2)']
    # 始发省市区
    start_province = ['css','#objForm > table > tbody > tr:nth-child(3) > td:nth-child(2) > div:nth-child(1) > div > div > input']
    start_province_value = ['css','#objForm > table > tbody > tr:nth-child(3) > td:nth-child(2) > div:nth-child(1) > div > dl > dd:nth-child(2)']
    start_city = ['css','#objForm > table > tbody > tr:nth-child(3) > td:nth-child(2) > div:nth-child(2) > div > div > input']
    start_city_value = ['css','#objForm > table > tbody > tr:nth-child(3) > td:nth-child(2) > div:nth-child(2) > div > dl > dd:nth-child(2)']
    start_district = ['css','#objForm > table > tbody > tr:nth-child(3) > td:nth-child(2) > div:nth-child(3) > div > div > input']
    start_district_value = ['xpath','//*[@id="objForm"]/table/tbody/tr[3]/td[2]/div[3]/div/dl/dd[2]']

    # 到达省市区
    arrive_province=['css','#objForm > table > tbody > tr:nth-child(4) > td:nth-child(2) > div:nth-child(1) > div > div > input']
    arrive_province_value=['css','#objForm > table > tbody > tr:nth-child(4) > td:nth-child(2) > div:nth-child(1) > div > dl > dd:nth-child(2)']
    arrive_city = ['css','#objForm > table > tbody > tr:nth-child(4) > td:nth-child(2) > div:nth-child(2) > div > div > input']
    arrive_city_value = ['css','#objForm > table > tbody > tr:nth-child(4) > td:nth-child(2) > div:nth-child(2) > div > dl > dd:nth-child(2)']
    arrive_district = ['css','#objForm > table > tbody > tr:nth-child(4) > td:nth-child(2) > div:nth-child(3) > div > div > input']
    arrive_district_value = ['xpath','//*[@id="objForm"]/table/tbody/tr[4]/td[2]/div[3]/div/dl/dd[3]']
    # 重量
    weight = ['css', 'input#totalWeight']
    # 体积
    volume = ['css', 'input#totalVolume']
    # 件数
    quantity = ['css', 'input#totalQty']
    # 计划作业时间
    plan_to_jobtime = ['css','input#planJobTime']
    plan_to_jobtime_value = ['css','#layui-laydate1 > div.layui-laydate-footer > div > span.laydate-btns-now']
    # 实际作业时间
    realistic_to_jobtime = ['css','input#actuallyJobTime']
    realistic_to_jobtime_value = ['css','#layui-laydate2 > div.layui-laydate-footer > div > span.laydate-btns-now']

    # -------------------------明细页面
    # 明细列表
    detail_frame = ['xpath', '//iframe[starts-with(@src,"/oss/oms/jobOrderTpDetail/detail")]']
    # 子订单号
    add_sub_order = ['css','#subOrderNo']
    # 计划重量
    plan_weight = ['css', '#planWorkloadWeight']
    # 计划体积
    plan_volume = ['css', '#planWorkloadVolume']
    # 计划件数
    plan_quantity = ['css', '#planWorkloadQty']
    # 实际重量
    actual_weight = ['css', '#actualWorkloadWeight']
    # 实际体积
    actual_volume = ['css', '#actualWorkloadVolume']
    # 实际件数
    actual_quantity = ['css', '#actualWorkloadQty']

    # 新增作业单
    # job_detail 是否传入子订单号，默认不传入，字符串类型
    def add_job(self,job_detail='t',row=None,case=[]):

        tm=time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))
        try:
            if job_detail == 't':
                productlist = ['zc']
                rcustomer_no_list = []
                run = OrderPage()
                no1 = run.add_order(producttype='LD',row=row,case=case)[1]
                # 只有创建成功的订单才加入列表
                if no1 != 'fail':
                    rcustomer_no_list.append(no1)
                else:
                    print('订单创建失败！不加入列表')
                for i in productlist:
                    no2 = run.add_order(lg='N', producttype=i,row=row,case=case)[1]
                    if no2 != 'fail':
                        rcustomer_no_list.append(no2)
                    else:
                        print('订单创建失败！不加入列表')
                if len(rcustomer_no_list) == '0':
                    clientorder_margerfeeno = 'fail'
                    text = u'输入订单号为空，请重新输入！'
                    return text, clientorder_margerfeeno
                else:
                    print(rcustomer_no_list)
                    print(len(rcustomer_no_list))

                # 根据客户单号查出子订单号，也可通过数据库查
                rcustomer_subno_list=[]
                for i in rcustomer_no_list:
                    rcustomer_subno_list.append(run.filter_subno(lg='f', pcustomer_no=i,case=case,row=row))
                time.sleep(3)
                run.quit()
            else:
                rcustomer_subno_list = job_detail.split(',')
                print(rcustomer_subno_list)

            print('输出子订单',rcustomer_subno_list)
            # 关闭所有标签
            self.click(self.close_tab[0], self.close_tab[1])
            self.click(self.close_tab[0], self.close_tab[1])
            self.click(self.close_tab[0], self.close_tab[1])
            self.login(username='kyadmin')
            # 运营管理
            self.click(self.operate_manage_module[0],self.operate_manage_module[1])
            # 运输作业单菜单
            self.click(self.transport_job[0], self.transport_job[1])
            self.in_iframe(self.listframe[0],self.listframe[1])
            time.sleep(5)
            # 菜单列表iframe
            listframe = ['xpath', '//iframe[@src="/oss/oms/jobOrderTp/list"]']
            # 新增
            self.click(self.add[0], self.add[1])
            # 编辑列表
            self.in_iframe(self.edit_frame[0], self.edit_frame[1])
            time.sleep(3)
            # 作业单号
            self.send(self.job_no[0], self.job_no[1],tm)
            # 供应商编号
            self.click(self.supplierid[0], self.supplierid[1])
            self.click(self.supplierid_value[0], self.supplierid_value[1])
            # 运输方式
            self.click(self.transporttype[0], self.transporttype[1])
            self.click(self.transporttype_value[0], self.transporttype_value[1])
            # 车型
            self.click(self.cartype[0], self.cartype[1])
            self.click(self.cartype_value[0], self.cartype_value[1])
            # 始发省市区
            self.click(self.start_province[0], self.start_province[1])
            self.click(self.start_province_value[0], self.start_province_value[1])
            self.click(self.start_city[0], self.start_city[1])
            self.click(self.start_city_value[0], self.start_city_value[1])
            time.sleep(1)
            self.click(self.start_district[0], self.start_district[1])
            time.sleep(1)
            self.click(self.start_district_value[0], self.start_district_value[1])
            # 到达省市区
            self.click(self.arrive_province[0], self.arrive_province[1])
            self.click(self.arrive_province_value[0], self.arrive_province_value[1])
            self.click(self.arrive_city[0], self.arrive_city[1])
            self.click(self.arrive_city_value[0], self.arrive_city_value[1])
            time.sleep(1)
            self.click(self.arrive_district[0], self.arrive_district[1])
            time.sleep(1)
            self.click(self.arrive_district_value[0], self.arrive_district_value[1])
            # 重量
            self.send(self.weight[0],self.weight[1],12)
            # 体积
            self.send(self.volume[0], self.volume[1], 12)
            # 件数
            self.send(self.quantity[0], self.quantity[1], 12)
            # 计划作业时间
            self.click(self.plan_to_jobtime[0],self.plan_to_jobtime[1])
            self.click(self.plan_to_jobtime_value[0],self.plan_to_jobtime_value[1])
            # 实际作业时间
            self.click(self.realistic_to_jobtime[0], self.realistic_to_jobtime[1])
            self.click(self.realistic_to_jobtime_value[0], self.realistic_to_jobtime_value[1])

            self.out_iframe()
            self.in_iframe(self.listframe[0],self.listframe[1])
            # 提交
            self.click(self.sumbit[0],self.sumbit[1])
            self.in_iframe(self.edit_frame[0],self.edit_frame[1])
            try:
                text=self.element(self.sumbit_success_tips[0],self.sumbit_success_tips[1]).text
                print(text)
            except Exception as e:
                text=u'定位失败或者创建失败！'
                return text
            self.out_iframe()
            self.in_iframe(self.listframe[0], self.listframe[1])
            time.sleep(4)
            # 添加作业单明细
            for i in rcustomer_subno_list:
                self.add_job_detail(job_no=tm,suborder=i,case=case,row=row)
            self.approval_job_no(job_no=tm)

        except Exception as e :
            print('做作业单出错了')
            text=u'做作业单出错了'
        print(text)

    # 添加作业单明细
    # job_no  作业单号, suborder 子订单号
    def add_job_detail(self, job_no,suborder,case=[],row=None):
        try:
            # 输入要过滤的作业单号
            self.clear(self.job_order_filter[0], self.job_order_filter[1])
            self.send(self.job_order_filter[0], self.job_order_filter[1], job_no)
            # 点击查询
            self.click(self.select_click[0], self.select_click[1])
            # 选中作业单
            self.click(self.check_box[0], self.check_box[1])
            # 点击添加明细按钮
            self.click(self.job_detail_button[0], self.job_detail_button[1])
            # 进入添加明细列表
            self.in_iframe(self.detail_frame[0], self.detail_frame[1])
            time.sleep(2)
            # 子订单号
            self.clear(self.add_sub_order[0], self.add_sub_order[1])
            self.send(self.add_sub_order[0], self.add_sub_order[1], suborder)
            # 计划重量
            self.clear(self.plan_weight[0], self.plan_weight[1])
            self.send(self.plan_weight[0], self.plan_weight[1], 11)
            # 计划体积
            self.clear(self.plan_volume[0], self.plan_volume[1])
            self.send(self.plan_volume[0], self.plan_volume[1], 11)
            # 计划件数
            self.clear(self.plan_quantity[0], self.plan_quantity[1])
            self.send(self.plan_quantity[0], self.plan_quantity[1], 11)
            # 实际重量
            self.clear(self.actual_weight[0], self.actual_weight[1])
            self.send(self.actual_weight[0], self.actual_weight[1], 11)
            # 实际体积
            self.clear(self.actual_volume[0], self.actual_volume[1])
            self.send(self.actual_volume[0], self.actual_volume[1], 11)
            # 实际件数
            self.clear(self.actual_quantity[0], self.actual_quantity[1])
            self.send(self.actual_quantity[0], self.actual_quantity[1], 11)
            self.out_iframe()
            self.in_iframe(self.listframe[0], self.listframe[1])
            # 提交
            self.click(self.sumbit[0], self.sumbit[1])
            self.in_iframe(self.detail_frame[0], self.detail_frame[1])
            try:
               text = self.element(self.sumbit_success_tips[0], self.sumbit_success_tips[1]).text
            except Exception as e:
               text = u'定位失败或者创建失败！'
               # return text
               # return u'定位失败或者创建失败！'
            time.sleep(4)
            self.out_iframe()
            self.in_iframe(self.listframe[0], self.listframe[1])
            time.sleep(1)

        except Exception as e:
            text = u'定位失败或者创建失败！'
        print(text)

    # 审核作业单
    # job_no 作业单号
    def approval_job_no(self, job_no,case=[]):
        # f 默认不输入拼车单号
        try:
            # 输入要过滤的作业单号
            self.clear(self.job_order_filter[0], self.job_order_filter[1])
            self.send(self.job_order_filter[0], self.job_order_filter[1], job_no)
            # 点击查询
            self.click(self.select_click[0], self.select_click[1])
            # 选中作业单
            self.click(self.check_box[0], self.check_box[1])
            # 审核按钮
            self.click(self.approval_button[0], self.approval_button[1])
            # 确定审核
            self.click(self.accept_approval[0], self.accept_approval[1])
            # 失败与成功的弹窗不同，第一个定位完，弹窗消失，所以第二个也会定位失败,所以不能分开定位
            try:
                self.text = self.element(self.approval_fail_tips[0], self.approval_fail_tips[1], time=6).text
                print(self.text)
            except Exception:
                # 也可以考虑数据查询判断是否删除成功，并且测试删除成功的情况比失败情况少，可以暂时先这么处理
                self.text = u'审核成功'
                print(self.text)

        except Exception as e:
            self.text = u'审核作业单出错!'
        # self.quit()
        return self.text


if __name__=='__main__':
    run=TransportJobTicket()
    list='DD20200612000060T001,DD20200612000061T001'
    # run.add_job(job_detail=list)
    run.add_job()




