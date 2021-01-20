# -*- coding: utf-8 -*-
# @Time    : 2020/6/29 11:46
# @Author  : msy
# @File    : receivable.py
# @Software: PyCharm
# from common.general import *
from decimal import Decimal
# import threading
# from page.order_page import *
from page.api_transport_job_ticket import *
# import requests
from page.order_page import *
from page.merge_charging import *
from page.carpooling import *

# 应收类
class Receivalble(BasePage):

   # 系统首页页签
   close_tab = ['xpath', '//*[@id="index_tabs"]/div[1]/div[4]/table/tbody/tr/td[3]/a/span']
   # -----------------------应收
   # 账务管理一级菜单
   finacial_manage_module = ['xpath', '//*[@title="财务管理"]/a']
   # 应收菜单
   receivalble_manage = ['xpath', '//span[text()="运输应收单管理"]/parent::div[starts-with(@id,"_easyui_tree")]']
   # 列表
   list_frame = ['xpath','//iframe[starts-with(@src,"/oss/finance/receivableOrder/list")]']
   # 展开更多
   open_more = ['xpath','//*[@id="TBFinanceReceiveOrder_queryShowHide"]/a']


   # 客户订单号
   clientorderno = ['css','textarea#client_order_number']
   # 查询按钮
   select_click =['css','#TBFinanceReceiveOrder_form > div > div:nth-child(3) > div:nth-child(1) > button']
   # 应收总金额
   recivalble_cost1 =['xpath','/html/body/div[2]/div/div[2]/div[2]/table/tbody/tr/td[13]/div']

   # -------------------订单管理
   # 订单管理模块
   order_manage_module = ['xpath', '//td[@title="订单管理"]/child::a[1]']
   # 订单处理
   order_deal_with = ['xpath', '//span[text()="订单处理_运输"]/parent::div[starts-with(@id,"_easyui_tree")]']
   # 菜单列表iframe
   listframe = ['xpath', '//iframe[@src="/oss/oms/TBClientOrder/todoList"]']
   # 查看按钮
   check_button = ['css', '#see']
   # 列表查询，客户过滤下拉
   customer_filtering = ['css','#TBClientOrder_queryTable > tbody > tr:nth-child(1) > td:nth-child(1) > div > div > div > input']

   # 列表查询，选择要过滤的客户(执行删除时，过滤客户不稳定，有时会执行到下一个客户，但定位时确实是定位到uat客户)
   customer_filtering_value = ['css','#TBClientOrder_queryTable > tbody > tr:nth-child(1) > td:nth-child(1) > div > div > dl > dd[lay-value="UATmsy"]']
   # 列表查询，客户订单号过滤
   customer_no_filtering_input = ['css', '#myClientOrderNo']
   # 点击查询
   select_click2 = ['css', '#TBClientOrder_form > div > div:nth-child(3) > div:nth-child(1) > button']
   # 列表订单复选框
   order_check_box = ['css',
                      'body > div.weadmin-body > div > div.layui-table-box > div.layui-table-fixed.layui-table-fixed-l > div.layui-table-body > table > tbody > tr > td > div > div > i']
   # 查看页面列表

   check_list = ['xpath','//iframe[starts-with(@src,"/oss/oms/TBClientOrderSee/see")]']
   check_transport_cost = ['xpath','//*[@id="mainDiv"]/div/div/div[1]/div[2]/table/tbody/tr/td[29]/div']

   # 作业单总金额
   def recivalble_cost(self,lg='t',customerno=None,case=[],row=None):
      try:
         # 登录
         if lg == 't':
            # 登录
            self.login(username=case[-4], password=case[-3])
         else:
            print('不需要登录')

         # 关闭所有标签
         self.click(self.close_tab[0], self.close_tab[1])
         self.click(self.close_tab[0], self.close_tab[1])
         self.click(self.close_tab[0], self.close_tab[1])
         # 进入财务系统
         self.click(self.finacial_manage_module[0],self.finacial_manage_module[1])
         # 进入应收菜单
         self.click(self.receivalble_manage[0],self.receivalble_manage[1])
         # 进入应收列表
         self.in_iframe(self.list_frame[0],self.list_frame[1])
         time.sleep(2)
         # 展开更多
         self.click(self.open_more[0],self.open_more[1])
         # 输入客户订单号
         self.send(self.clientorderno[0],self.clientorderno[1],customerno)
         # 点击查询
         self.click(self.select_click[0],self.select_click[1])
         # 直接滚动到目标元素
         target = self.element(self.recivalble_cost1[0], self.recivalble_cost1[1])
         if target=='fail':
            text = 'fail'
            return text
         else:
            self.driver.execute_script("arguments[0].scrollIntoView(false);", target)
         # 应收总金额
         text=self.element(self.recivalble_cost1[0],self.recivalble_cost1[1]).text
         self.out_iframe()
         # print(text)
         # 订单查看页面不用逗号显示，所以要去掉
         c=text.count(',')
         # print(c)
         if c!=0:
            text=text.replace(',', '')
            # print('替换后打印',text)
            # 由于订单查看页面、应收页面数据小数数是不一致的，所以要统一处理成保留四位
            text = Decimal(text).quantize(Decimal("0.00"))
         else:
            pass
         print(text)
      except Exception as e:
         print(e)
         text = 'fail'
      # self.quit()
      return text

   # 订单查看页面金额
   def order_cost(self,lg='t',customerno=None,case=[],row=None):
      try:
         # 登录
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
         self.send(self.customer_no_filtering_input[0], self.customer_no_filtering_input[1],customerno)
         # 点击查询
         self.click(self.select_click2[0], self.select_click2[1])
         # 列表订单复选框
         element1=self.element(self.order_check_box[0], self.order_check_box[1])
         if element1=='fail':
            text = 'fail'
            return text
         else:
            self.click(self.order_check_box[0], self.order_check_box[1])
         # 查看按钮
         self.click(self.check_button[0], self.check_button[1])
         self.out_iframe()
         # 查看列表
         self.in_iframe(self.check_list[0],self.check_list[1])
         time.sleep(10)
         # 直接滚动到目标元素
         # target = self.element(self.check_transport_cost[0], self.check_transport_cost[1])
         # if target == 'fail':
         #    text = 'fail'
         #    return text
         # else:
         #    self.driver.execute_script("arguments[0].scrollIntoView(false);", target)

         self.scroll_to_terminal(self.check_transport_cost[0], self.check_transport_cost[1])
         # 应收界面的运输总金额
         if self.element(self.check_transport_cost[0], self.check_transport_cost[1]) !='fail':
            text1 = self.element(self.check_transport_cost[0], self.check_transport_cost[1]).text
            # 保留两位，目的是订单获取到的在返回也是保留成两位
            text= Decimal(text1).quantize(Decimal("0.00"))
            # 转换成功列表
            # text=str(text2)
            print('打印text:', text)
         else:
            text='fail'
            print('查看页面定位总金额出错！')
         self.out_iframe()

      except Exception as e:
         print(e)
         text = 'fail'
      print(text)
      self.quit()
      return text

   # 数据库应收金额
   def database_cost(self,customerno,case=[],row=None):

      db,cur=self.connet_database()
      sql="select total_receivable_amount from t_b_finance_receivable_order where client_order_number ='{}'".format(customerno)
      # print(sql)
      try:
         # 执行sql语句
         cur.execute(sql)
         # 提交到数据库执行
         db.commit()
         # 获取返回结果
         result = cur.fetchone()[0]
         # 把结果转换成6位小数，目的是避免订单金额只有两位小数导致对比不一致的情况，但现在订单返回的是两位的，所以暂时只取两位
         result = Decimal(result).quantize(Decimal("0.00"))
      except:
          # 如果出错回滚
          db.rollback()
          result='fail'
      # 关闭数据库连接
      cur.close()
      db.close()
      print(result)
      self.quit()
      return result

   # 应收界面 、订单查看界面、数据库对比结果
   def compare_cost(self,lg='t',customerno=None,merge=None,carpooling=None,row=None,case=[]):
      try:
         # 如果没有输入订单号，不需要合并计费，则创建一个订单号
         if customerno is None and merge is None and carpooling is None:
            customerno = OrderPage().add_order(row=row,case=case)[1]
            # 创建成功则接着创建作业单以生产应收
            if customerno != 'fail':
               customernolist = []
               customernolist.append(customerno)
            else:
               print('订单创建失败！')
               result = '订单创建失败！'
               return result
            # 做作业单
            text = TransportJobTicket().operate_job2(orderno_list=customernolist,case=case,row=row)
            if '接口作业单出错' in text:
               print('作业单创建失败！')
               result = '作业单创建失败！'
               return result
            else:
               pass
         # 合并计费
         elif customerno is None and merge is not None:
            customernolist = []
            # 创建两个订单，merge是产品类型
            for i in range(2):
               customernolist.append(OrderPage().add_order(producttype=merge,row=row,case=case)[1])
            # 订单的大于一个则合并计费
            if len(customernolist) > 1:
               # 做作业单
               text = TransportJobTicket().operate_job2(orderno_list=customernolist,case=case,row=row)
               if '接口作业单出错' in text:
                 print('作业单创建失败！')
                 result = '作业单创建失败！'
                 return result
               else:
                  # 合并计费并审核
                  MergeChargingPage().approval_merge(add_clientorder_margerfeeno=customernolist,row=row,case=case)

            else:
               print('订单小于两个，不能合并计费')
               result = '订单小于两个，不能合并计费'
               return result

         # 客户拼车
         elif customerno is None and carpooling is not None:
            customernolist = []
            # 创建两个订单，merge是产品类型
            for i in range(2):
               customernolist.append(OrderPage().add_order(producttype=carpooling,row=row,case=case)[1])
            # 订单的大于一个则合并计费
            if len(customernolist) > 1:
               # 做作业单
               text = TransportJobTicket().operate_job2(orderno_list=customernolist,case=case,row=row)
               if '接口作业单出错' in text:
                  print('作业单创建失败！')
                  result = '作业单创建失败！'
                  return result
               else:
                  # 拼车并审核
                  print('00999')
                  CarpoolingPage().approval_carpoolling(add_clientorder_carpoollingfeeno=customernolist,row=row,case=case)
                  print('0032222')

            else:
               print('订单小于两个，不能拼车')
               result = '订单小于两个，不能拼车'
               return result

         else:
            print('对比金额参数输入出错，请检查')
            result = '对比金额参数输入出错，请检查'
            return result


      except Exception:
         result = 'fail'
         print('对比金额出现异常')
         return result

      try:
         # 应收金额，要转换成字符串，不转换，对比不相等，可能是数据库获取到不是是字符串类型
         result1 = str(self.recivalble_cost(customerno=customernolist[0],case=case,row=row))
         # 订单金额
         result2 = str(self.order_cost(customerno=customernolist[0],case=case,row=row))
         # 数据库金额
         result3 = str(self.database_cost(customerno=customernolist[0],case=case,row=row))
         print(type(result1))
         print(type(result2))
         print(type(result3))
         print('订单号：{},应收、订单及数据库金额分别是：{}/{}/{}'.format(customernolist[0], result1, result2, result3))
         # print(result1)
         # print(result2)
         # print(result3)
         # 如果有个结果是失败就判断失败
         if result1=='fail' or result2=='fail' or result3=='fail':
            result='fail'
            return result
         else:
            # 如果返回结果相等就判断成功
            if result1==result2 and result1==result3:
               result = u'相等,对比订单、应收/订单金额/数据库金额分别是：{}、{}/{}/{}'.format(customernolist[0],result1,result2,result3)
            else:
               result = u'不等,对比订单、应收/订单金额/数据库金额分别是：{}、{}/{}/{}'.format(customernolist[0],result1,result2,result3)
      except Exception:
         result = 'fail'
         return result
      # print()
      # self.quit()
      print(result)
      return result


if __name__=='__main__':
   # 先创建订单返回客户订单号列表
   order=OrderPage()
   productlist = ['zc']
   rcustomer_no_list = []
   no1 = order.add_order(producttype='LD')[1]
   # 只有创建成功的订单才加入列表
   if no1 != 'fail':
      rcustomer_no_list.append(no1)
   else:
      print('订单创建失败！不加入列表')
   for i in productlist:
      no2 = order.add_order(lg='N', producttype=i)[1]
      if no2 != 'fail':
         rcustomer_no_list.append(no2)
      else:
         pass
   # 创建完订单退出列表
   order.quit()
   print('客户订单号类型',type(rcustomer_no_list))
   # 订单号列表不为空时，做作业单及对比应收金额
   if len(rcustomer_no_list)>0:
      # 做作业单
      apijob = TransportJobTicket()
      apijob.make_operate_job(cutomernolist=rcustomer_no_list)

      # 对比金额
      for j in rcustomer_no_list:
         run = Receivalble()
         run.compare_result(j)
         print('新增订单对比订单及应收数据库金额')

      # 编辑提交使产生红冲
      order = OrderPage()
      for i in rcustomer_no_list:
         order.edit_order(pcustomer_no=i)

      # 对比金额
      for j in rcustomer_no_list:
         run = Receivalble()
         run.compare_result(j)
         print('编辑修改订单对比订单及应收数据库金额')

   else:
      print('请输入订单号')




   # rcustomer_no_list=['20200703143422','20200703143541']
   # for j in rcustomer_no_list:
   #    run = Receivalble()
   #    run.compare_result(j)
   # 查询子订单号
         # print('订单创建失败！不加入列表')
   # run = Receivalble()
   # run.recivalble_cost('2020063002')
   # run.order_cost('2020063002')
   # run.database_cost('2020063002')
   # run.compare_result(2020063002)
   # thread1.daemon(True)
   # run2 = Receivalble()
   # run3 = Receivalble()
   # print('11')
   # thread1=threading.Thread(target=run.recivalble_cost,args=('2020063002',))
   # thread2=threading.Thread(target=run2.order_cost,args=('2020063002',))
   # thread3=threading.Thread(target=run3.database_cost,args=('2020063002',))
   #
   # # 目的是主线程运行完，可以退出，守护线程是指守护主线程的
   # thread1.setDaemon(True)
   # thread2.setDaemon(True)
   #
   # thread1.start()
   # thread2.start()
   # thread3.start()
   # # 目的是是要等待主线程执行完再继续执行主线程
   # thread1.join()
   # thread2.join()
   # thread3.join()
