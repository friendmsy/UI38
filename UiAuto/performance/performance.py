# from config import *
# import os

from statistics import mean
import xlrd
# import xlwt
from xlutils.copy import copy
from common.log import *
from gevent import monkey
monkey.patch_all()
import gevent
import requests
import json
from gevent.queue import Queue


class ApiGeneral():

    # get方法
    # @classmethod # 类方法可以不实例化调用
    def get(self, url, params,**kwargs):    #params是str类型，有&和=的数据

        print('进入get方法')
        dictdata = self.str_to_dict(params)  #转换成字典
        print(dictdata)
        # print('打印传入的参数',type(url),type(params))
        try:
            resp = requests.get(url=url, params=dictdata,**kwargs)   # params对应的数据是字典类型,*是列表，**是字典
            print(resp)
        except Exception as e:
            Mylog().my_log().error(e)
            print(e)
            resp='get请求失败！'
            print(resp)

        return resp

    def getd(self, url, data, **kwargs):
        print('进入get方法')
        try:
            resp = requests.get(url=url, data=data, **kwargs)  # params对应的数据是字典类型,*是列表，**是字典
            print(resp)
        except Exception as e:
            Mylog().my_log().error(e)
            print(e)
            resp = 'get请求失败！'
            print(resp)

        return resp

    # post方法
    @classmethod # 类方法可以不实例化调用
    def post(self, url,**kwargs):
        # session = requests.Session().get('https://uaterp.pgl-world.com.cn')
        try:
            # resp = requests.post(url=url, data=data,**kwargs)    #data应该是字典类型
            resp = requests.post(url=url, **kwargs)
            # print(resp.content)
        except Exception as e:
            Mylog().my_log().error(e)
            resp='fail'
            print(e)
            # print(resp)
        return resp


    # # 如果请求含附件
    #文件打开方式是rb，二进制，其他方式打开会报错，文件路径格式可以是\\,\,/,文件
    # 可以是字典，也可以是列表，可以有多个文件同时上传，文件定义时多个元组或者键值对，
    # filename一般是代码的文件参数名，但试过如果不是也能上传成功，Content-Type是json的话，参数主是json形式的，要dumps，其他是dict(取出的是str就lodas下)
    @classmethod  # 类方法可以不实例化调用   .encode('utf-8')
    def filepost(self, url,file, **kwargs):
        # with open(file, 'rb') as f:
        try:
            files = {'file': open(file, 'rb')}  #先实例一个字典类型的文件对象
            rsp = requests.post(url=url,files=files, **kwargs) #不需要转换成json(json.dumps),因为是表单的数据
            # rsp = requests.post(url=url, files=f, json=json.dumps(json.loads(data)), **kwargs)  # 要用json，不能用data
            # print(resp.content)
        except Exception as e:
            Mylog().my_log().error(e)
            print(e)
            # print(resp)
        return rsp

    # # get方法	,有附件
    # @classmethod# 类方法可以不实例化调用
    # def get(self, url, params, cookies, file):
    #     with open(file, 'a') as f:
    #         jdata = self.str_to_dict(params)
    #         try:
    #             resp = requests.get(url=url, parms=params, cookies=cookies, files=f)
    #         except Exception as e:
    #             Mylog().my_log().error(e)
    #     return resp

    # 字符串转换成字典方法
    @classmethod
    def str_to_dict(self, data):
        dict1 = {}
        for i in data.split('&'):   #用&切割成两部分，形成一个列表
            key = i.split('=')[0]  #第一个是键
            value = i.split('=')[1] #第二个是值
            dict1[key] = value
        return dict1
    #
    #
    # # 响应结果对比并写入结果,主要是对比code一样就通过
    def result(self, expectresult, actualresult):   #两个参数传入是str
        jdate1=json.loads(expectresult)
        jdate2 = json.loads(actualresult)
        # for k in jdate1.keys():
        #     if k=='code':
        #         c=k
        #     if k=='msg':
        #         m=k
        if jdate1['code']==jdate2['code']:  #   通过code和msg共同判断是否通过，可能这样的粒度有点粗，后续看情况优化
            if jdate1['msg']==jdate2['msg']:
                result_status = '1'  # 通过
            else:
                result_status = '0'  # 不通过
        else:
            result_status = '0'  # 不通过
        return result_status

    #
    #     # for i in actualresult:
    #     #     if i not in expectresult:
    #     #         result_status = '0' #不通过
    #     #         result_status = '1' # 通过
    #     #
    #     #     else:
    #     #         result_status = '0' #不通过
    #     # return result_status
    #
    #
    # 把结果写回excel
    #当文件打开时，运行方法会报错（或者数据写不进去！！！！！），不允许操作，所以运作时一定要关闭文件，另外重新运作，新插入数据会覆盖原有的
    def write_result(self, row, actualresult, result, tester, casefile):  # 文件不用写全路径，只写文件名只可
        case_path=os.path.join(CASEPATH, casefile)
        print(case_path)
        book = xlrd.open_workbook(case_path)  # 创建一个excel操作对象
        book2 =copy(book) #复制book对象  #管道作用:利用xlutils.copy函数，将xlrd.Book转为xlwt.Workbook，再用xlwt模块进行存储
        sheet = book2.get_sheet(0)  # 创建一个sheet操作实例,读取的是第一个excel ,#通过get_sheet()获取的sheet有write()方法
        sheet.write(row, 13, actualresult)
        sheet.write(row, 14, result)
        sheet.write(row, 15, tester)

        # book2.save(case_path)
        book2.save(case_path)
        print('结果写入保存成功！')
        # print('保存后1')
        # sheet2=book.sheet_by_index(0)
        # print(sheet2.cell_value(row,12))
        # print('保存后')

    #通过登录动态获取cookies
    def get_cookies(self,url,params):   #通过登录获取cookie供后续接口调用,由于调试项目登录接口参数是&格式的，具体按实际项目进行修改调整
        respond=self.get(url=url,params=params)
        self.cookies=respond.cookies.get_dict()     #respond.cookies只会获取到一个cookiejar对象，一定要有get_dict()方法，返回dict类型
        print(self.cookies)
        print(type(self.cookies))
        self.strcookies=json.dumps(self.cookies)   #由于get方法传入参数会loads成dict类型，所以传入的一定是str，所以要转换成str
        print('打印strcookies',self.strcookies)
        print(type(self.strcookies))
        return self.strcookies
# 并发
class ConCurrent():
    # 请求成功
    pass_number=0
    # 请求失败
    fail_number=0
    # 断言失败
    assertfail=0
    # 断言通过
    assertpass=0
    # 执行时长
    run_time_list=[]
    api=ApiGeneral()

    # 接口请求,number：循环次数,url：接口地址,data：请求体,assertion:断言
    def concurrent(self,number,url,data,num,assertion=None,*args,**kwargs):
        print(data)
        print(type(data))
        if isinstance(data,dict):
            pass
        else:
            data = eval(data)
        print('第一次', num)
        # print('打印输入的data',data)
        for i in range(number):
            # 开始时间
            start_time=time.time()
            # 如果是界面并发，修改成调用的方法也可，也是通过返回做断言
            respond=self.api.post(url=url,data=json.dumps(data))
            # gevent.sleep(5)
            # 结束时间
            end_time = time.time()
            print(respond.content.decode('utf-8'))

            # 结束减去开始时间，保留四位小数
            run_time=round(end_time-start_time,4)
            self.run_time_list.append(run_time)
            if respond.status_code==200:
                self.pass_number=self.pass_number+1
                # 请求成功的进行断言
                content=eval(respond.content.decode('utf-8'))
                if assertion is not None:
                    print(content['msg'],assertion)
                    if assertion in content['msg']:
                        self.assertpass = self.assertpass + 1
                    else:
                        self.assertfail = self.assertfail + 1
                else:
                    # 用'0000'表示没有断言
                    self.assertpass = '0000'
                    self.assertfail = '0000'
            else:
                self.fail_number = self.fail_number + 1
        print('第二次', num)

    # threadings：线程，用户数, number：循环次数, url：地址, data：请求体, file：参数化数据文件，parameterized：是否参数化
    def concurrent_run(self,threadings,number,url,data=None,file=None,*args,**kwargs):
        if isinstance(data, dict):
            pass
        else:
            data = eval(data)
        if file is not None:
            book = xlrd.open_workbook(file)  # 创建一个excel操作对象
            # print(os.path.join(CASEPATH, file))
            sheet = book.sheet_by_index(0)  # 创建一个sheet操作实例,读取的是第一个excel，如果需要也可以参数化
            nnrow = sheet.nrows  # 获取行数
            # 创建一个空列表，用于存放用例
            all_data = []
            # 存放最后一列，最后一列放断言
            all_data2 = []
            # print('空列表长度',len(all_case))
            # 第一行写参数名称
            firstrow=sheet.row_values(0)
            firstrow_len=len(sheet.row_values(0))
            param = list(firstrow[0:firstrow_len-1])
            # print(param)

            for j in range(1, nnrow):
                list1 = list(sheet.row_values(j)[0:firstrow_len-1])
                all_data.append(list1)
            # print(all_data)
            # 获取倒数第一行，是断言
            for j in range(1, nnrow):
                list1 = sheet.row_values(j)[firstrow_len-1]
                all_data2.append(list1)
            # print('断言',all_data2)
            data_list = []
            # 嵌套层不不适用参数化，只能是第一层参数
            for row,a in zip(all_data,all_data2):
                for key, value in zip(param, row):
                    data[key] = value
                # 没有转换成str的情况，只会把最后一个data重复加入列表，不知道原因
                # data_list.append(data)
                l=[str(data),a]
                # l=[data,a]
                # data_list.append(str(data))
                data_list.append(l)

            # print('哈哈',data_list)
            print("请求URL: {url}".format(url=url))
            print("用户数：{}，循环次数: {}".format(threadings, number))
            print("============== Running ===================")
            # 参数化个数与线程数要一致，按以下代码设计，如果不一致，可能会有问题
            jobs = [gevent.spawn(self.concurrent, number=number, url=url,data=j[0],num=i,assertion=j[1]) for i, j in zip(range(threadings), data_list)]
            # jobs = [gevent.spawn(self.concurrent, number=number, url=url,data=j,num=i,) for i, j in zip(range(threadings), data_list)]

        else:
            print('不需要参数化')
            print("请求URL: {url}".format(url=url))
            print("用户数：{}，循环次数: {}".format(threadings, number))
            print("============== Running ===================")
            # 参数化个数与线程数要一致，以下代码如果不一致，可能会有问题
            jobs = [gevent.spawn(self.concurrent, number, url, data,i) for i in range(threadings)]
        gevent.joinall(jobs)
        # gevent.wait(jobs)

        print("\n============== Results ===================")
        print("最大:       {} s".format(str(max(self.run_time_list))))
        print("最小:       {} s".format(str(min(self.run_time_list))))
        print("平均:       {} s".format(str(round(mean(self.run_time_list), 4))))
        print("请求成功", self.pass_number)
        print("请求失败", self.fail_number)
        print("断言成功", self.assertpass)
        print("断言失败", self.assertfail)
        print("============== end ===================")

if __name__ == '__main__':
    dit = {
        "jobNo": "202012090111",
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
        "jobStatus": "未完成",
        "detailList": [
          {
            "mainOrderNo": "DD20201207000027",
            "subOrderNo": "DD20201207000027T001",
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
          },
          {
            "mainOrderNo": "DD20201203000016",
            "subOrderNo": "DD20201203000016T001",
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

          },
          {
            "mainOrderNo": "DD20201207000026",
            "subOrderNo": "DD20201207000026T002",
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

          },
          {
            "mainOrderNo": "DD20201207000028",
            "subOrderNo": "DD20201207000028T001",
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
        ]
        }
    url11='https://uaterp.pgl-world.com.cn/api/service?method=pgl.erp.api.oms.jobOrderTp.add&appCode=pgl-erp-oss-oms&companyCode=PGLKY&timestamp=2020-12-09%2018:09:00&version=1.0&sign=M2f8gkzZEzMKPgq&departCode=PGLKY03'
    con = ConCurrent()
    con.concurrent_run(20, 1,data=dit,url=url11,file=r'E:\software\Python3.8.3\UiAuto\file\condata.xlsx')


