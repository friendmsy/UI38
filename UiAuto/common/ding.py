from datetime import datetime
import requests
import json
import os
import sys
from dingtalkchatbot.chatbot import DingtalkChatbot
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
from config import *
from common.general import *
COMMONPATH=os.path.join(BASE_PATH,'common')
sys.path.append(COMMONPATH)
from common.send_report_to_email import *


# WebHook地址

def dinghtml(title, msg):
    webhook = "https://oapi.dingtalk.com/robot/send?access_token=6376792f2ca10ab2e9222220477ccd0a095b9e6849438761779e4ddaef2b5e00"
    xiaoding = DingtalkChatbot(webhook)  # 方式一：通常初始化方式
    xiaoding.send_markdown(title=title, text=msg, is_at_all=False)


def dingmessage(msg):
    # 请求的URL，WebHook地址
    webhook = "https://oapi.dingtalk.com/robot/send?access_token=6376792f2ca10ab2e9222220477ccd0a095b9e6849438761779e4ddaef2b5e00"

    # 构建请求头部
    header = {
        "Content-Type": "application/json",
        "Charset": "UTF-8"
    }
    # 构建请求数据
    time_now = datetime.now().strftime('%Y-%m-%d %H:%M')  # 精确到分钟
    text = "ERP测试报告( " + time_now + " )\n" + msg
    message = {

        "msgtype": "text",
        "text": {
            "content": text
        },
        "at": {
            # "isAtAll": True
            "isAtAll": False
        }

    }
    # 对请求的数据进行json封装
    message_json = json.dumps(message)
    # 发送请求
    info = requests.post(url=webhook, data=message_json, headers=header)
    # 打印返回的结果
    print(info.text)

class Ding(BasePage):

    def dingtext(self,dir=None):
        # time.sleep(8)
        try:
            webhook = "https://oapi.dingtalk.com/robot/send?access_token=6376792f2ca10ab2e9222220477ccd0a095b9e6849438761779e4ddaef2b5e00"
            # xiaoding = DingtalkChatbot(webhook)
            dirlist = []
            if dir is None:
                # 获取发送报告的附件
                l = send()
                # 判断是否有html或者zip结尾的文件
                for i in l:
                    if os.path.basename(i).split('.')[1] == 'html' or os.path.basename(i).split('.')[1] == 'zip':
                        dirlist.append(i)
                    else:
                        pass
                if len(dirlist) == 0:
                    msg = '没有生成测试报告'
                elif len(dirlist) != 1:
                    msg = '测试报告有多个，无法确定要统计哪个报告的数据'
                else:
                    # 报告的路径的格式有两种，html和zip，zip是allure，所以不能直接在浏览器打开此路径，要在tomcat中打开
                    if os.path.basename(dirlist[0]).split('.')[1] == 'zip':
                        with open(os.path.join(BASE_PATH, 'yamlconfig.yml'), 'r', encoding='utf-8') as f:
                            myyaml = [i for i in yaml.load_all(f)]
                        reportpath = os.path.normpath(
                            os.path.split(dirlist[0])[0] + r'\\' + os.path.basename(dirlist[0]).split('.')[0])
                        tomcatpath = myyaml[2]['filepath'] + os.path.basename(dirlist[0]).split('.')[0]
                        # print('tomcatpath',tomcatpath)
                        dirlist[0] = myyaml[2]['url'] + os.path.basename(dirlist[0]).split('.')[0]
                        # print(dirlist[0])
                        # 删除文件夹，把文件夹也删除了
                        if os.path.exists(tomcatpath):
                            shutil.rmtree(tomcatpath)
                            time.sleep(5)
                            print('原文件夹已删除')
                        else:
                            pass
                        # 移动文件夹，如果report存在，会报错
                        shutil.copytree(reportpath, tomcatpath)
                        time.sleep(5)
                        print('文件夹已复制到tomcat目录下')
                    else:
                        pass
            else:
                dirlist.append(dir)

            print('dirlist[0]', dirlist[0])

            driver1 = BasePage()
            driver1.driver.get(url=dirlist[0])
            # 打开后会自动关闭，所以要强行等待，使能读取到报告的信息
            time.sleep(3)
            # pytest的报告
            # 通过的用例
            case_pass = ['xpath', '/html/body/span[1]']
            # 跳过的用例
            case_skipped = ['xpath', '/html/body/span[2]']
            # 失败的用例
            case_failed = ['xpath', '/html/body/span[3]']
            # case_errors = ['xpath', '/html/body/span[4]']
            # 总耗时
            total_time = ['xpath', '/html/body/p[2]']

            # beautifulreport报告
            bcase_pass = ['xpath', '//*[@id="testPass"]']
            bcase_skipped = ['xpath', '//*[@id="testSkip"]']
            bcase_failed = ['xpath', '//*[@id="testFail"]']
            # bcase_errors = ['xpath', '/html/body/span[4]']
            btotal_time = ['xpath', '//*[@id="totalTime"]']

            # allure报告
            acase_pass = ['xpath', '//*[@id="content"]/div/div[2]/div/div[1]/div/div[2]/div[3]/div/div/div[3]/span']
            acase_skipped = ['xpath', '//*[@id="content"]/div/div[2]/div/div[1]/div/div[2]/div[3]/div/div/div[4]/span']
            acase_failed = ['xpath', '//*[@id="content"]/div/div[2]/div/div[1]/div/div[2]/div[3]/div/div/div[1]/span']
            # acase_errors = ['xpath', '/html/body/span[4]']
            atotal_time = ['xpath', '//*[@id="content"]/div/div[2]/div/div[1]/div[1]/div[2]/div/div/div[1]/h2/div']
            showall = ['xpath', '//*[@id="content"]/div/div[2]/div/div[1]/div[4]/div[2]/div/div/a/div']

            # E 开头是pytest-html报告
            if os.path.basename(dirlist[0]).startswith('E'):
                total_time_text = driver1.element(method=total_time[0], param=total_time[1]).text
                case_pass_text = driver1.element(method=case_pass[0], param=case_pass[1]).text
                case_failed_text = driver1.element(method=case_failed[0], param=case_failed[1]).text
                case_skipped_text = driver1.element(method=case_skipped[0], param=case_skipped[1]).text
                # case_errors_text = driver1.element(method=case_errors[0], param=case_errors[1]).text
                msg = '此次运行耗时：{}\n通过的用例:{}\n失败的用例:{}\n跳过的用例:{}\n' \
                    .format(total_time_text, case_pass_text, case_failed_text, case_skipped_text)

            # i 开头是allure报告
            elif dirlist[0].startswith('http'):
                if driver1.element(method=atotal_time[0], param=atotal_time[1], time=8, screenshot='n') == 'fail':
                    msg = '没有获取到报告的数据，请确认tomcat服务是否打开'
                else:
                    total_time_text = driver1.element(method=atotal_time[0], param=atotal_time[1]).text
                    driver1.click(method=showall[0], param=showall[1])
                    case_pass_text = driver1.element(method=acase_pass[0], param=acase_pass[1]).text
                    case_failed_text = driver1.element(method=acase_failed[0], param=acase_failed[1]).text
                    case_skipped_text = driver1.element(method=acase_skipped[0], param=acase_skipped[1]).text
                    # case_errors_text = driver1.element(method=acase_errors[0], param=acase_errors[1]).text
                    msg = '此次运行耗时：{}\n通过的用例:{}\n失败的用例:{}\n跳过的用例:{}\n' \
                        .format(total_time_text, case_pass_text, case_failed_text, case_skipped_text)
            # beautiful报告
            else:
                total_time_text = driver1.element(method=btotal_time[0], param=btotal_time[1]).text
                case_pass_text = driver1.element(method=bcase_pass[0], param=bcase_pass[1]).text
                case_failed_text = driver1.element(method=bcase_failed[0], param=bcase_failed[1]).text
                case_skipped_text = driver1.element(method=bcase_skipped[0], param=bcase_skipped[1]).text
                # case_errors_text = driver1.element(method=bcase_errors[0], param=bcase_errors[1]).text
                msg = '此次运行耗时：{}\n通过的用例:{}\n失败的用例:{}\n跳过的用例:{}\n' \
                    .format(total_time_text, case_pass_text, case_failed_text, case_skipped_text)
            driver1.quit()

            # 构建请求头部
            header = {
                "Content-Type": "application/json",
                "Charset": "UTF-8"
            }
            time_now = datetime.now().strftime('%Y-%m-%d %H:%M')  # 精确到分钟
            text = "ERP测试报告( " + time_now + " )\n" + msg
            message = {

                "msgtype": "text",
                "text": {
                    "content": text
                },
                "at": {
                    # "isAtAll": True
                    "isAtAll": False
                }

            }
            # 对请求的数据进行json封装
            message_json = json.dumps(message)
            # 发送请求
            info = requests.post(url=webhook, data=message_json, headers=header)
            # 打印返回的结果
            print(info.text)
            print('发送钉钉结束！')
            time.sleep(13)
        except Exception as e:
            print(e)


# 若要发送邮件，启用即可
Ding().dingtext()
# ding=Ding().dingtext(dir='http://localhost:8080/report')

