# -*- coding: utf-8 -*-
# @Time    : 2020/7/16 9:35
# @Author  : msy
# @File    : reconciliation.py
# @Software: PyCharm

from common.general import *
from page.api_transport_job_ticket import TransportJobTicket

# 对账单类
class Reconciliation(BasePage):

    # 系统首页页签
    close_tab = ['xpath', '//*[@id="index_tabs"]/div[1]/div[4]/table/tbody/tr/td[3]/a/span']
    # 账务管理一级菜单
    finacial_manage_module = ['xpath', '//*[@title="财务管理"]/a']
    # 对账单管理模块一级
    reconciliation_manage=['xpath','//*[@id="RightAccordion"]/div[2]/div[1]/div[1]']
    # 应收对账单二级
    receivalble_reconciliation=['xpath','//*[@class="tree-node"]/span[text()="应收对账单"]']
    # 对账单三级
    receivalble_reconciliation_manage =['xpath','//*[@class="tree-node"]/span[text()="应收对账单管理"]']
    # 列表
    listframe=['xpath','//*/iframe[@src="/oss/finance/receivableStatement/list"]']
    # 新增按钮
    add_reconciliation_button =['xpath','//*[@id="update"]/preceding-sibling::button[@id="create"]']
    # 编辑列表
    editframe=['xpath','//*/iframe[starts-with(@src,"/oss/finance/receivableStatement/detail")]']
    # 请选择客户
    choose_custome=['xpath','//*[@id="objForm"]/table/tbody/tr[1]/td[2]/div[2]/div/div/input']
    # 选择客户
    cutome_value=['xpath','//*[@id="objForm"]/table/tbody/tr[1]/td[2]/div[2]/div/dl/dd[@lay-value="UATmsy"]']
    # 对账开始日期
    statementStartDate=['xpath','//*[@id="statementStartDate"]']
    # 对账结束日期,获取现在
    statementEndDate=['xpath','//*[@id="statementEndDate"]']
    # 指定对账客户订单号
    clientOrderNumber=['xpath','//*[@id="clientOrderNumber"]']
    # 提交按钮
    submit=['xpath','//*[starts-with(@id,"layui-layer")]/div[3]/a[1]']
    # 返回结果列表
    resultframe = ['xpath', '//*[starts-with(@src,"/file/checkImportFileReady")]']
    # 创建成功标识
    success=['xpath','//*[@id ="processDiv"]/button[text()="导入成功"]']

    # 添加对账单
    # client_order_number 客户订单号列表
    def add_reconciliation(self, lg='t',client_order_number=[],case=[],row=None):
        # 对订单先做作业单
        text=TransportJobTicket().operate_job2(lg=lg,orderno_list=client_order_number,row=row,case=case)
        if '接口作业单出错' in text:
            return text
        else:
            pass

        try:
            if lg == 't':
                # 登录
                self.login(username=case[-4], password=case[-3])
            else:
                print('不需要登录')

            # 关闭所有标签
            self.click(self.close_tab[0], self.close_tab[1])
            self.click(self.close_tab[0], self.close_tab[1])
            self.click(self.close_tab[0], self.close_tab[1])
            # 账务管理一级菜单
            self.click(self.finacial_manage_module[0],self.finacial_manage_module[1])
            # 对账单管理模块一级
            self.click(self.reconciliation_manage[0], self.reconciliation_manage[1])
            # 应收对账单二级
            self.click(self.receivalble_reconciliation[0], self.receivalble_reconciliation[1])
            # 对账单三级
            self.click(self.receivalble_reconciliation_manage[0], self.receivalble_reconciliation_manage[1])
            # 列表
            self.in_iframe(self.listframe[0],self.listframe[1])
            # 新增按钮
            print(1)
            self.click(self.add_reconciliation_button[0],self.add_reconciliation_button[1])
            print(3)
            # 编辑列表
            self.in_iframe(self.editframe[0], self.editframe[1])
            print(2)
            time.sleep(5)
            # 请选择客户
            self.click(self.choose_custome[0], self.choose_custome[1])
            time.sleep(1)
            # 选择客户
            self.click(self.cutome_value[0], self.cutome_value[1])
            time.sleep(1)
            # 对账开始日期
            self.send(self.statementStartDate[0],self.statementStartDate[1],'2020-01-01')
            time.sleep(3)
            # 对账结束日期
            self.send(self.statementEndDate[0], self.statementEndDate[1], '2031-01-01')
            # 指定对账客户订单号
            time.sleep(3)
            for i in client_order_number:
                self.send(self.clientOrderNumber[0], self.clientOrderNumber[1], i)
                self.element(self.clientOrderNumber[0], self.clientOrderNumber[1]).send_keys(Keys.ENTER)

            # 退出框架
            self.out_iframe()
            # 列表
            self.in_iframe(self.listframe[0], self.listframe[1])
            # 提交按钮
            self.click(self.submit[0], self.submit[1])
            # 退出框架
            self.out_iframe()
            # 列表
            self.in_iframe(self.listframe[0], self.listframe[1])
            # 返回结果列表
            self.in_iframe(self.resultframe[0], self.resultframe[1])
            # 创建成功标识
            if self.element(self.success[0], self.success[1],time=60)!='fail':
                text='创建对账单成功'
            else:
                text = '创建对账单失败'
            self.out_iframe()

        except Exception as e:
            print(e)
            text = '创建对账单出错'
        print(text)
        return text



if __name__ == '__main__':
    Reconciliation().add_reconciliation(client_order_number=['20201021092435','20201021092605'])
