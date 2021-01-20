# -*- coding: utf-8 -*-
# @Time    : 2020/6/25 22:51
# @Author  : msy
# @File    : api_transport_job_ticket.py
# @Software: PyCharm

from common.api_general import *
import json
from page.order_page import *

# 接口作业单类

class TransportJobTicket(ApiGeneral):

    # 接口作业单,list 为子订单号列表
    def operate_job(self, list=[],case=[],row=None,nojob=None):
        try:
            # 时间年月日时分
            Y = time.strftime('%Y', time.localtime(time.time()))
            m = time.strftime('%m', time.localtime(time.time()))
            d = time.strftime('%d', time.localtime(time.time()))
            H = time.strftime('%H', time.localtime(time.time()))
            M = time.strftime('%M', time.localtime(time.time()))
            S = time.strftime('%S', time.localtime(time.time()))
            # 作业单号
            jobno = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
            jobno2 = get_customerno()
            if nojob is not None:
                jobno=jobno2
            else:
                pass
            # 时效,如果分大于50，小时就加1，否则分加5，分不能大于60，一般23点之后也不会操作，
            # 所以也不会超过24时的情况，就不考虑
            if int(M)>54:
                H=int(H)+1
                M = '03'
            else:
                M=int(M)+5
            tm = '{}-{}-{} {}:{}:00'.format(Y, m, d, H,M)
            # print(tm)
            url = '{}/api/service?method=pgl.erp.api.oms.jobOrderTp.add&appCode=pgl-erp-oss-oms&companyCode=PGLKY&timestamp={}&version=1.0&sign=M2f8gkzZEzMKPgq&departCode=PGLKY03'.format(
                URL,tm)
            # 主体
            dit = {
                "jobNo": jobno,
                "transportMode": "QY",
                "supplierCode": "smp0910",
                "plateNumber": "粤B12318",
                "driverName": "测试司机18",
                "carType": "DF96",
                "startProvinceCode": "370000",
                "startCityCode": "370300",
                "startCountyCode": "370321",
                "endProvinceCode": "370000",
                "endCityCode": "370300",
                "endCountyCode": "370322",
                "planJobTime": "2019-10-11 15:00:00",
                "actuallyJobTime": "2019-10-17 15:00:00",
                "totalWeight": 155,
                "totalVolume": 115,
                "totalQty": 160,
                "operateCompanyCode": "PGLKY",
                "operateDepartCode": "PGLKY03",
                "jobStatus": "未完成"
            }
            # 明细
            list1=[]
            for i in list:
                # print(i)
                mainorder = str(i).split('T')[0]
                # print(mainorder)
                dd = {
                    "mainOrderNo":mainorder,
                    "subOrderNo":i,
                    "planWorkloadWeight": 30,
                    "actualWorkloadWeight": 30,
                    "planWorkloadVolume": 13,
                    "actualWorkloadVolume": 1111,
                    "planWorkloadQty": 1115,
                    "actualWorkloadQty": 5,
                    "clientProductList": [],
                    "supplierProductList": [],
                    "jobTime": "2019-10-18 15:00:00",
                    "remark": "测试快递运输费18"
                    }
                list1.append(dd)
            dit['detailList'] = list1
            if nojob is not None:
                return tm,dit
            else:
                # post data 字典类型要dumps成字符串
                result = self.post(url=url, data=json.dumps(dit)).content.decode('utf-8', '转换失败')
            # print(result)
        except Exception as e:
            print('接口作业单出错',e)
            Mylog().my_log().error('接口作业单出错',e)
            result='接口作业单出错'
        print(result)
        return result

    # 创建订单，并获取子订单号
    # plist 是产品列表，cutomernolist 是客户订单号列表
    def make_operate_job(self,plist=['ld','ld'],cutomernolist=[],row=None,case=[]):
        tm = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
        print(cutomernolist)
        print(type(cutomernolist))

        print('打印',len(cutomernolist))
        try:
            if len(cutomernolist)==0:
                productlist = plist
                rcustomer_no_list = []
                run = OrderPage()
                no1 = run.add_order(producttype=plist[0],row=row,case=case)[1]
                # 只有创建成功的订单才加入列表
                if no1 != 'fail':
                    rcustomer_no_list.append(no1)
                else:
                    print('订单创建失败！不加入列表')
                productlist.pop(0)
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
                rcustomer_subno_list = []
                for i in rcustomer_no_list:
                    rcustomer_subno_list.append(run.filter_subno(lg='f', pcustomer_no=i,case=case,row=row))
                time.sleep(3)
                run.quit()
            else:
                rcustomer_no_list = cutomernolist
                print(rcustomer_no_list)
                # 根据客户单号查出子订单号，也可通过数据库查
                run = OrderPage()
                rcustomer_subno_list = []

                # 第一个登录，后面不用登录
                lent=len(rcustomer_no_list)
                if lent>1:
                    print(rcustomer_no_list[0])
                    rcustomer_subno_list.append(run.filter_subno(case=case,lg='t', pcustomer_no=rcustomer_no_list[0],row=row))
                    rcustomer_no_list.pop(0)
                    print(type(rcustomer_no_list))
                    print(rcustomer_no_list)

                    for i in rcustomer_no_list:
                        print(i)
                        rcustomer_subno_list.append(run.filter_subno(lg='f',case=case,pcustomer_no=i,row=row))
                else:
                    rcustomer_subno_list.append(run.filter_subno(lg='t',case=case, pcustomer_no=rcustomer_no_list[0],row=row))
                time.sleep(3)
                run.quit()
                print(rcustomer_subno_list)
            # 调用接口作业单
            result=self.operate_job(list=rcustomer_subno_list,case=case,row=row)
            print(result)

        except Exception as e:
            Mylog().my_log().error('接口作业单出错', e)
            result='接口作业单出错'
        return result

    # 输入客户订单号做作业单
    def operate_job2(self, lg='t',orderno_list=[],case=[],row=None):
        try:
            rcustomer_subno_list=[]
            # 查询出子单号
            orderpage=OrderPage()
            print(len,rcustomer_subno_list)
            if len(orderno_list)==1:
                rcustomer_subno_list.append(orderpage.filter_subno(lg=lg, pcustomer_no=orderno_list[0], case=case, row=row))
            else:
                rcustomer_subno_list.append(orderpage.filter_subno(lg=lg, pcustomer_no=orderno_list[0], case=case, row=row))
                for i in orderno_list[1:]:
                    rcustomer_subno_list.append(orderpage.filter_subno(lg='f', pcustomer_no=i, case=case, row=row))

                # rcustomer_subno_list.append(filter_subno(lg=lg,pcustomer_no=i,case=case,row=row))
            print(rcustomer_subno_list)
            if len(rcustomer_subno_list)>0:
                text=self.operate_job(list=rcustomer_subno_list,case=case,row=row)
                if '接口作业单出错' in text:
                    return text
                else:
                    pass
            else:
                print('输入子订单号小于1个，不做作业单')
        except Exception as e:
            print('接口作业单出错',e)
            Mylog().my_log().error('接口作业单出错',e)
            text = '接口作业单出错'
        print(text)
        return text


# if __name__ == '__main__':
    # apijob=TransportJobTicket()
    # list1='DD20200616000010T001,DD20200616000011T001'
    # list11=['DD20200703000010T001','DD20200703000011T001']
    # list1=['630103359','630103360','630103361','630103362','630103363','630103364']
    # apijob.operate_job(list=list11)
    # apijob.make_operate_job(cutomernolist=list1)
    # apijob.make_operate_job()
    # for i in list1:
    #     print(i)
    # TransportJobTicket().operate_job2(orderno_list=['20201021092435','20201021092605'])