#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/5/6 10:41
# @Author : msy

# from config import *
# import os.
import shutil
import xlrd
# import xlwt
from xlutils.copy import copy
# import Exception
# import requests
from common.log import *
# import json
import requests
from selenium import webdriver
# from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import pymysql
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
import yaml
# import pyautogui
class BasePage():
    # shutil.copyfile()
    # webbroser：浏览器，downloadpath：下载文件的路径，time=：等待时间
    # 默认是谷歌浏览器，下载路径也默认
    def __init__(self,webbroser=WEBBROSER,downloadpath=FILE,time=25):
        # 运行脚本时不用打开浏览器
        # options.add_argument("--headless")
        # 要加多下面两个设置，如果不加，运行时有元素会定位不到,但目录订单导入会有问题，没有上传到附件
        # options.add_argument('window-size=1920x1080')
        # options.add_argument('--start-maximized')

        # 定义浏览器
        if webbroser == 'chrome':
            # 隐性等待，要网页加载完成，隐性等待对整个driver的周期都起作用，所以只要设置一次即可
            options = webdriver.ChromeOptions()
            # 浏览器默认下载路径
            prefs = {'profile.default_content_settings.popups': 0, 'download.default_directory': downloadpath}
            options.add_experimental_option('prefs', prefs)
            # 指定浏览器驱动的目的是能正确启动浏览器 ，如果不指定，项目执行时可能找不到驱动
            self.driver = webdriver.Chrome(executable_path=r'C:\Users\Administrator\AppData\Local\Google\Chrome\Application\chromedriver.exe', chrome_options=options)
            # 65服务器
            # self.driver = webdriver.Chrome(executable_path=r'E:\software\Python3.8.3\UiAuto\common\chromedriver.exe',
            #                                chrome_options=options)
        elif webbroser == 'ie':
            option = webdriver.IeOptions()
            option.add_argument('headless')
            self.driver = webdriver.Ie(ie_options=option)
            # self.driver=webdriver.Ie()
        elif webbroser == 'firefox':
            option = webdriver.FirefoxOptions()
            # option.add_argument('headless')
            self.driver = webdriver.Firefox(executable_path=r'E:\software\Python3.8.3\UiAuto\bin\geckodriver.exe',firefox_options=option)
        else:
            print('请输入谷歌、火狐、IE中的一种！')
            Mylog().my_log().info('请输入谷歌、火狐、IE中的一种！')

    # url:要测试的网站登录地址, username ：登录账号, password ：登录密码
    def login(self,url=URL,username='sybmsy',password='12345678'):
        try:
            # 由于多进程时，如果同一账号同时跑，则由于ERP登录机制，一个浏览器同一账号不能登录多个，
            # 会导致上一个进程退出时影响到下一个进程用例被迫退出导致用例结果不准确，所以账号也要参数化
            # with open(os.path.join(BASE_PATH, 'yamlconfig.yml'), mode='r',encoding='utf-8') as f:
            #     # load_all 读取多个文档
            #     l = [i for i in yaml.load_all(f)]
            self.driver.get(url)
            # 浏览器窗口最大化
            self.driver.maximize_window()
            self.send(send=username,method='xpath',param='//*[@id="username"]',time=300)
            # self.driver.implicitly_wait(3)
            time.sleep(1)
            self.send(send=password,method='id',param='password')
            # self.driver.implicitly_wait(2)
            # time.sleep(1)
            # 万能验证码8888。       2021-01-15验证码去掉了
            # self.send(send='8888',method='id',param='captchaCode')
            # self.driver.implicitly_wait(2)
            time.sleep(1)
            self.click(method='id',param='login')
            time.sleep(2)
        except Exception as e:
            print(e)
            Mylog().my_log().info(e)

    #定位元素方法
    def element(self,method,param,time=25,screenshot='f'):
        # Mylog().my_log().info('element方法')
        try:
            #定位方法ID
            if method == 'id':

                # 显性等待，指定元素加载完成，一般比整个页面加载完成快，
                # 对于UAT很多字段要等待整个页面加载完成才能操作，可能用隐性等待更好
                # (实践证明，uat也不适用，然后会加载不到选项就跳过)
                # self.implicitlty_wait(time)
                element = (By.ID, param)
                WebDriverWait(self.driver, time).until(EC.visibility_of_element_located(element))
                self.e=self.driver.find_element_by_id(param)
            # 定位方法name
            elif method == 'name':
                element = (By.NAME,param)
                WebDriverWait(self.driver, time).until(EC.visibility_of_element_located(element))
                self.e = self.driver.find_element_by_name(param)
            # 定位方法xpaht
            elif method == 'xpath':
                # self.implicitlty_wait(time)
                element = (By.XPATH,param)
                WebDriverWait(self.driver,time,0.5).until(EC.visibility_of_element_located(element))
                self.e = self.driver.find_element_by_xpath(param)
            # 定位方法classname
            elif  method =='classname':
                element = (By.CLASS_NAME,param)
                WebDriverWait(self.driver, time).until(EC.visibility_of_element_located(element))
                self.e = self.driver.find_element_by_class_name(param)

            # 定位方法tag
            elif  method =='tagname':
                element = (By.TAG_NAME,param)
                WebDriverWait(self.driver, time).until(EC.visibility_of_element_located(element))
                self.e = self.driver.find_element_by_tag_name(param)

            elif  method =='css':
                # self.implicitlty_wait(time)
                element = (By.CSS_SELECTOR,param)
                WebDriverWait(self.driver, time,0.5).until(EC.visibility_of_element_located(element))
                self.e = self.driver.find_element_by_css_selector(param)

            # 定位方法link
            elif  method =='linktext':
                element = (By.LINK_TEXT,param)
                WebDriverWait(self.driver, time).until(EC.visibility_of_element_located(element))
                self.e = self.driver.find_element_by_link_text(param)

            # 定位方法parlinktext
            elif method =='parlinktext':
                element = (By.PARTIAL_LINK_TEXT,param)
                WebDriverWait(self.driver, time).until(EC.visibility_of_element_located(element))
                self.e = self.driver.find_element_by_partial_link_text(param)

            else:
                print('不存在定位方法！',method,param)
        # 捕获异常，可以在系统有异常时仍能跳过，继续执行后面的代码，如果不捕获，程序直接抛错，不再执行后面的代码
        except Exception as f:
            # self.e='2'
            print('无法找到元素！methond:{},param:{},错误原因：{}'.format(method,param,f))
            self.e = 'fail'
            Mylog().my_log().error(f)
            # t,默认是不截图，目前截图没有分析意义，截图较耗时，非必要，不要截图，加快用例执行速度
            if screenshot == 't':
                self.screen_shot()
            else:
                # print("不需要截图")
                Mylog().my_log().info("不需要截图")

        return self.e

    def elements(self, method, param, time=25, screenshot='t',index=0):
        try:
            #定位方法ID
            if method == 'id':

                # 显性等待，指定元素加载完成，一般比整个页面加载完成快，
                # 对于UAT很多字段要等待整个页面加载完成才能操作，可能用隐性等待更好
                # (实践证明，uat也不适用，然后会加载不到选项就跳过)
                # self.implicitlty_wait(time)
                element = (By.ID, param)
                WebDriverWait(self.driver, time).until(EC.visibility_of_element_located(element))
                self.e=self.driver.find_elements_by_id(param)[index]
            # 定位方法name
            elif method == 'name':
                element = (By.NAME,param)
                WebDriverWait(self.driver, time).until(EC.visibility_of_element_located(element))
                self.e = self.driver.find_elements_by_name(param)[index]
            # 定位方法xpaht
            elif method == 'xpath':
                # self.implicitlty_wait(time)
                element = (By.XPATH,param)
                WebDriverWait(self.driver,time,0.5).until(EC.visibility_of_element_located(element))
                self.e = self.driver.find_elements_by_xpath(param)[index]
            # 定位方法classname
            elif  method =='classname':
                element = (By.CLASS_NAME,param)
                WebDriverWait(self.driver, time).until(EC.visibility_of_element_located(element))
                self.e = self.driver.find_elements_by_class_name(param)[index]

            # 定位方法tag
            elif  method =='tagname':
                element = (By.TAG_NAME,param)
                WebDriverWait(self.driver, time).until(EC.visibility_of_element_located(element))
                self.e = self.driver.find_elements_by_tag_name(param)[index]

            elif  method =='css':
                # self.implicitlty_wait(time)
                element = (By.CSS_SELECTOR,param)
                WebDriverWait(self.driver, time,0.5).until(EC.visibility_of_element_located(element))
                self.e = self.driver.find_elements_by_css_selector(param)[index]

            # 定位方法link
            elif  method =='linktext':
                element = (By.LINK_TEXT,param)
                WebDriverWait(self.driver, time).until(EC.visibility_of_element_located(element))
                self.e = self.driver.find_elements_by_link_text(param)[index]

            # 定位方法parlinktext
            elif method =='parlinktext':
                element = (By.PARTIAL_LINK_TEXT,param)
                WebDriverWait(self.driver, time).until(EC.visibility_of_element_located(element))
                self.e = self.driver.find_elements_by_partial_link_text(param)[index]

            else:
                print('不存在定位方法！',method,param)
        # 捕获异常，可以在系统有异常时仍能跳过，继续执行后面的代码，如果不捕获，程序直接抛错，不再执行后面的代码
        except Exception as f:
            # self.e='2'
            print('无法找到元素！methond:{},param:{},错误原因：{}'.format(method,param,f))
            self.e = 'fail'
            Mylog().my_log().error(f)
            # t,默认是截图
            if screenshot == 't':
                self.screen_shot()
            else:
                # print("不需要截图")
                Mylog().my_log().info("不需要截图")

        return self.e

    # 单击
    def click(self,method,param,time1=20,screenshot='t'):
        Mylog().my_log().info('进入click方法')
        try:
            # element = (By.CLASS_NAME, param)
            # WebDriverWait(self.driver, time).until(EC.visibility_of_element_located(element))
            self.element(method=method, param=param,time=time1,screenshot=screenshot).click()
        except Exception as e:
            Mylog().my_log().info('点击出错，详情如下：{}'.format(e))
    #
    # 双击
    def double_click(self,method,param):
        # self.implicitltywait(5)
        ActionChains(self.driver).double_click(self.element(method=method,param=param)).perform()

    # 右击
    def context_click(self, method, param):
        ActionChains(self.driver).context_click(self.element(method=method, param=param)).perform()
    '''
    # 右击选择菜单
    def context_choice(self, method, param,index=[]):
        self.context_click(method, param)
        time.sleep(3)
        print('右键11111111')
        pyautogui.typewrite(index)
        print('右键2222222222222222')
    '''

    # 拖动
    def drag_drop(self, method, param):
        ActionChains(self.driver).drag_and_drop(self.element(method=method, param=param)).perform()

    # 复制、粘贴
    def keys(self,method,param,send):
        self.element(method=method,param=param).send_keys(Keys.CONTROL,send)

    # 功能快捷键
    def function_key(self,method,param,send):
        self.element(method=method,param=param).send_keys('Keys.'+'{}'.format(send))

    # 文本输入
    def send(self,method,param,send,time=30):
        Mylog().my_log().info('进入send方法')
        try:
            self.element(method=method,param=param,time=time).send_keys(send)
            print(method,param,send)
            print('运行send结束！')
        except Exception as e:
            Mylog().my_log().info('文本输入出错，详情如下：{}'.format(e))
    #切换到iframe
    def in_iframe(self,method,param):
        Mylog().my_log().info('进入in_iframe方法')
        print('进入frame')
        self.driver.switch_to_frame(self.element(method=method,param=param))
        # time.sleep(8)
        print('退出！')
        # time.sleep(5)
    #退出iframe
    def out_iframe(self):
        Mylog().my_log().info('进入outiframe方法')
        # self.driver.switch_to_default_content()
        self.driver.switch_to_default_content()
        print('退出到根iframe')

    #滚动,定长滚动
    def scroll(self):
        Mylog().my_log().info('进入scroll方法')
        # js = "var q=document.documentElement.scrollTop=1500"
        js = "var q=document.documentElement.scrollTop=1350"
        # self.mc.driver.execute_script(js)
        self.driver.execute_script(js)

    #滚动到指定目标
    def scroll_to_terminal(self,method,param):
        Mylog().my_log().info('进入scroll方法')
        target=self.element(method=method,param=param)
        self.driver.execute_script("arguments[0].scrollIntoView();",target)

    #弹窗确认
    def accept(self):
        self.implicitlty_wait(5)
        self.driver.switch_to.alert.accept()        #点击确认按钮

        # 弹窗取消
    def dismiss(self):
        self.implicitlty_wait(5)
        self.driver.switch_to.alert.dismiss()  # 点击取消按钮

    # 切换窗口
    def switch_window(self,num):
        # self.implicitlty_wait(5)
        all_handles=self.driver.window_handles
        print(all_handles)
        self.driver.switch_to_window(all_handles[num])

    #刷新
    def reflush(self):
        # self.implicitlty_wait(5)
        self.driver.refresh()
    #前进
    def forward(self):
        # self.implicitlty_wait(5)
        self.driver.forward()
    #后退
    def rollback(self):
        # self.implicitlty_wait(5)
        self.driver.back()
    #退出浏览器
    def quit(self):
        # 退出浏览器
        self.driver.quit()
    #隐性等待
    def implicitlty_wait(self,time):
        self.driver.implicitly_wait(time)
    #显性等待
    def sleep(self,time):
        time.sleep(time)
    #窗口最大化
    def maximize(self):
        self.driver.maximize_window()
    #截图
    def screen_shot(self,page='system'):
        # print('进入截图方法')
        # 目录
        pfile=os.path.join(SCREEN_SHOT,page)
        tm=time.strftime('%Y%m%d',time.localtime(time.time()))
        tm2=time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))
        # 目录2
        file=os.path.join(pfile,tm)
        name=tm2+'.png'
        print(name)
        filenme=os.path.join(file,name)
        print(filenme)
        #不能同时创建多级目录,否则会报错
        if not os.path.exists(pfile):
            os.mkdir(pfile)
            print('输出创建的目录',pfile)
        else:
            print('不需要创建访目录')
        if not os.path.exists(file):
            os.mkdir(file)
            print('输出创建的目录',file)
        else:
            print('不需要创建访目录')
        result=self.driver.get_screenshot_as_file(filenme)
        print(filenme)
        print(result)
        time.sleep(6)

    #清空文本内容
    def clear(self,method,param):
        self.element(method=method,param=param).clear()

    #连接数据库，返回数据库对象,游标对象
    # @classmethod
    def connet_database(self,host=HOST,port=PORT,user=USER,password=DBPASSWORD,database=DATABASE,dbtype=DATATYPE,charset='utf8mb4'):
        if dbtype=='mysql':
           db=pymysql.Connect(host=host,port=port,user=user,password=password,database=database,charset=charset)
           cur = db.cursor()
        # elif dbtype=='sql':
        #    db=sqlite3.Connect(host=host,port=port,usename=usename,passwd=passwd,db=db,chartset=chartset)
        else:
            cur='fail'
            print('输入的数据库类型错误！')
            Mylog().my_log().info('输入的数据库类型错误！')

        # cur.execute(sql)
        # db.commit()
        # # cur.close()
        # try:
        #     # 执行sql语句
        #     cursor.execute(sql)
        #     # 提交到数据库执行
        #     db.commit()
        # except:
        #     # Rollback in case there is any error
        #     db.rollback()
        #
        # # 关闭数据库连接
        # db.close()

        return db,cur

    def bget(self, url):    #params是str类型，有&和=的数据
        print('进入get方法')
        try:
            resp = requests.get(url=url)   # params对应的数据是字典类型,*是列表，**是字典
            print(resp)
        except Exception as e:
            Mylog().my_log().error(e)
            print(e)
            resp='get请求失败！'
            print(resp)

        return resp

'''
    @staticmethod
    def get_case(file):   #传入文件名就可以， 不用传入全路径，用例文件要放在case目录下
        all_cases = []  # 创建一个空列表，用于存放用例

        book = xlrd.open_workbook(os.path.join(CASEPATH, file))  # 创建一个excel操作对象
        print(os.path.join(CASEPATH, file))
        sheet = book.sheet_by_index(0)  # 创建一个sheet操作实例,读取的是第一个excel，如果需要也可以参数化
        nnrow = sheet.nrows  # 获取行数
        # row=nnrow
        # print('打印获取到的行数',row)
        # nrows = sheet.nrows
        #print(nnrow)

        for j in range(2, nnrow):   #不是从0开始读取，从第三行开始读取
            if sheet.row_values(j)[2]!='#':  #  '#'表示此行跳过，不获取，第三列valid
                list1=list(sheet.row_values(j)[3:14])
                list1.append(j)
                # 把行数也加入到列表，目的是写入时方便定位到对应的行数;指定行指定列数据，从valid开始到row
                all_cases.append(list1)    #append里面不能再调用append，会导致返回的是None
        # print(self.all_cases)
        Mylog().my_log().info('i遍历获取用例')

        return all_cases

    # 把结果写回excel
    #当文件打开时，运行方法会报错（或者数据写不进去！！！！！），不允许操作，所以运作时一定要关闭文件，另外重新运作，新插入数据会覆盖原有的
    def write_result(self, row, result, tester, casefile):  # 文件不用写全路径，只写文件名只可
        case_path=os.path.join(CASEPATH, casefile)
        print(case_path)
        book = xlrd.open_workbook(case_path)  # 创建一个excel操作对象
        book2 =copy(book) #复制book对象  #管道作用:利用xlutils.copy函数，将xlrd.Book转为xlwt.Workbook，再用xlwt模块进行存储
        sheet = book2.get_sheet(0)  # 创建一个sheet操作实例,读取的是第一个excel ,#通过get_sheet()获取的sheet有write()方法
        sheet.write(row, 12, result)
        sheet.write(row, 13, tester)
        # book2.save(case_path)
        book2.save(case_path)
        print('结果写入保存成功！')
        sheet2=book.sheet_by_index(0)
        print(sheet2.cell_value(row,12))
        # print('保存后')

'''

#方法调试
if __name__ == '__main__':
    mycase=BasePage(WEBBROSER)
    print(mycase.get_case('POcase.xlsx'))
    # mycase.login(URL)
    # time.sleep(8)
    # # 一级
    # mycase.click(method='xpath',param='//td[@title="订单管理"]/child::a[1]')
    # time.sleep(2)
    # 订单二级
    #订单管理三级
    # mycase.click(method='xpath', param='//span[text()="订单处理"]/parent::div[starts-with(@id,"_easyui_tree")]')
    # print('订单管理菜单')
    # # 订单管理选项卡
    # time.sleep(2)
    # el=mycase.driver.find_element_by_xpath('//iframe[@src="/oss/oms/TBClientOrder/todoList"]')
    # time.sleep(2)
    # mycase.driver.switch_to_frame(el)   #切换到iframe
    #
    # time.sleep(3)
    # mycase.click(method='xpath', param='//*[@id="create"]')
    # # mycase.implicitltywait(6)
    # time.sleep(3)
    # print('新增')

    # ee = mycase.driver.find_element_by_xpath('//div[text()="新增"]/parent::div[@type="iframe"]')
    #
    # time.sleep(2)
    # mycase.driver.switch_to_frame(ee)  # 切换到iframe


    # mycase.driver.switchTo().defaultContent()

   #  ell=mycase.driver.find_element_by_xpath('//iframe[@id="detailDiv"]/following::iframe[starts-with(@id,"layui-layer-iframe")]')
   #
   #  time.sleep(2)
   #  # mycase.driver.switch_to_frame(ell)   #切换到iframe
   #  print('iframe',ell)
   #  time.sleep(5)
   #  # if mycase.element(method='xpath', param='//*[@id="objForm"]/div/div[1]/div[2]/div[1]/div/div/i').is_enabled():
   #  #     print('可操作')
   #  print('打印', mycase.element(method='xpath', param='//*[@id="objForm"]/div/div[1]/div[2]/div[1]/div/div/i'))
   #  mycase.click(method='xpath', param='//*[@id="objForm"]/div/div[1]/div[2]/div[1]/div/div/i')
   #
   #  # else:
   #  #     print('不可操作哦！！！！1')
   #  time.sleep(2)
   #  if mycase.element(method='xpath', param='//form[@id="objForm"]/descendant::dd[@lay-value="UATmsy"]').is_enabled():
   #      print(mycase.element(method='xpath', param='//form[@id="objForm"]/descendant::dd[@lay-value="UATmsy"]'))
   #      print('可操作12')
   #
   #      mycase.click(method='xpath', param='//form[@id="objForm"]/descendant::dd[@lay-value="UATmsy"]')
   #      time.sleep(2)
   #      print('打印选择到的客户名称', mycase.element(method='xpath',param='//*[@id="objForm"]/div/div[1]/div[2]/div[1]/div/div/input').get_attribute("value"))
   #  else:
   #      print('不可操作！！！！1')
   #  time.sleep(2)
   #  print('定位客户单号')
   #  mycase.send(method='xpath', param='//form[@id="objForm"]/descendant::input[@name="clientOrderNo"]',send='2020032600001')
   #  time.sleep(1)
   #  print('打印输入的单号',mycase.element(method='xpath', param='//form[@id="objForm"]/descendant::input[@name="clientOrderNo"]').get_attribute("value"))
   #  # mycase.keys(method='xpath', param='//form[@id="objForm"]/descendant::input[@name="clientOrderNo"]', send='a')
   #  #
   #  # mycase.keys(method='xpath', param='//form[@id="objForm"]/descendant::input[@name="clientOrderNo"]',send='c')
   #  # time.sleep(1)
   #  # mycase.keys(method='css',param='#clientSalesNo',send='v')
   #  # mycase.contextclick(method='css',param='#clientSalesNo')
   #  mycase.click(method='css',param='#objForm > div > div:nth-child(2) > div.layui-row > div:nth-child(6) > div > div > input')
   #  mycase.click(method='css',param='#objForm > div > div:nth-child(2) > div.layui-row > div:nth-child(6) > div > dl > dd:nth-child(3)')
   #  mycase.send(method='css', param="input[id='clientSalesNo']",send='2020032500003')
   #  if mycase.element(method='css', param='input#totalWeight').is_displayed():
   #      print('可见')
   #      mycase.send(method='css', param='input#totalWeight', send='123')
   #  else:
   #      print('定位有问题哦！！！！1')
   #  if mycase.element(method='css', param='input#totalVolume').is_enabled():
   #      print('可操作')
   #      mycase.send(method='css', param='input#totalVolume', send='1')
   #  else:
   #      print('定位有问题哦！！！！1')
   #  mycase.send(method='css', param='input#totalQty', send='123')
   #  mycase.click(method='css', param='#objForm > div > div:nth-child(4) > div:nth-child(2) > div:nth-child(2) > div > div > input')
   #  mycase.click(method='css',param='#objForm > div > div:nth-child(4) > div:nth-child(2) > div:nth-child(2) > div > dl > dd:nth-child(3)')
   #  mycase.click(method='css',param='#tpModule > div:nth-child(2) > div:nth-child(2) > div > div > input')
   #  mycase.click(method='css',param='#tpModule > div:nth-child(2) > div:nth-child(2) > div > dl > dd:nth-child(2)')
   #  #是否提货
   #  mycase.click(method='css',param='#tpModule > div:nth-child(2) > div:nth-child(4) > div')
   #  time.sleep(2)
   #  #提货方式
   #  mycase.click(method='css',param='#tpModule > div:nth-child(2) > div:nth-child(6) > div > div > input')
   #  mycase.click(method='css',param='#tpModule > div:nth-child(2) > div:nth-child(6) > div > dl > dd:nth-child(2)')
   #  time.sleep(2)
   #  #发货地址码
   #  mycase.click(method='css',param='#tpModule > div:nth-child(3) > div.layui-col-md2.myWidth-16 > div > div > input')
   #  mycase.click(method='css',param='#tpModule > div:nth-child(3) > div.layui-col-md2.myWidth-16 > div > dl > dd[lay-value="test0701"]')
   #  # mycase.click(method='css',param='#tpModule > div:nth-child(3) > div.layui-col-md2.myWidth-16 > div > dl > dd[lay-value="test0701"]')
   #  #收货地址
   #  js = "var q=document.documentElement.scrollTop=1500"
   #  mycase.driver.execute_script(js)
   #  time.sleep(2)
   #  mycase.click(method='css', param='#tpModule > div:nth-child(5) > div.layui-col-md2.myWidth-16 > div > div > input')
   #  # mycase.click(method='css', param='#tpModule > div:nth-child(3) > div.layui-col-md2.myWidth-16 > div > dl > dd[lay-value="test0702"]')
   #  mycase.click(method='css', param='#tpModule > div:nth-child(5) > div.layui-col-md2.myWidth-16 > div > dl > dd:nth-child(2)')
   #  #进入产品选择
   #  mycase.click(method='css', param='#layui-tab-title01 > li:nth-child(3)')
   #  mycase.click(method='css', param='#layui-tab-content01 > div.layui-tab-item.layui-show > div:nth-child(1) > div.layui-col-md2 > div > div > input')
   #  #选择产品
   #  mycase.click(method='css', param='#layui-tab-content01 > div.layui-tab-item.layui-show > div:nth-child(1) > div.layui-col-md2 > div > dl > dd[lay-value="CUATMSYTP201910280002"]')
   #  #提交
   #  time.sleep(5)
   #  # mycase.driver.execute_script(js)
   #  # mycase.driver.switch_to_default_content()
   #  # time.sleep(2)
   #  mycase.driver.execute_script(js)
   #  print('下拉！')
   #
   #  mycase.driver.switch_to_default_content()
   #  time.sleep(2)
   #  print('跳出！')
   #  # mycase.driver.switch_to.parentFrame()
   #  mycase.driver.switch_to_frame(el)
   #  time.sleep(2)
   #  print('进入框架')
   #  mycase.click(method='css', param='div.layui-layer-btn.layui-layer-btn- > a.layui-layer-btn0')
   #  time.sleep(3)
   #  mycase.driver.switch_to_frame(ell)
   #  mycase.implicitltywait(5)
   #  jss= "var q=document.documentElement.scrollTop=1500"
   #  mycase.driver.execute_script(js)
   #  mycase.implicitltywait(5)
   #  text11=mycase.element(method='xpath',param="//span[@class='layui-layer-setwin']/parent::div//div[@class='layui-layer-content layui-layer-padding']").text
   #  # if text11=='"新增订单成功"':
   #  #     print('结束')
   #  # else:
   #  #     print('新增订单失败！')
   #  print(text11)
   # # mycase.click(method='xpath', param="//span[@class='layui-layer-setwin']/parent::div//i")
   #
   #
   #
   #







