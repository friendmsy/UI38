#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/5/6 10:43
# @Author : msy

import smtplib  # 导入smtplib模块
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.header import Header
# 6 from .logger import *
import  time


# 1. subject：邮件主题 
# 2. content：邮件正文 
# 3. filepath：附件的地址, 输入格式为["","",...] 
# 4. receive_email：收件人地址, 输入格式为["","",...]，有默认邮箱
def send_email(filepath,receive_email=['moshuangyou@pgl-world.com','john@pgl-world.com']):
    try:
        # tm=time.strftime('%Y%m%d')
        tm = time.strftime('%Y%m%d', time.localtime(time.time()))
        retm = tm + '  ' + u'ERP自动化测试报告'
        content = u'        尊敬的领导好！请查收' + retm + '，' + u'报告详情见附件。注：报告可能有两种格式，html和zip两种格式。\nhtml格式附件建议用谷歌浏览器打开,zip格式附件请解压到tomcat的webapps目录下，访问tomcat打开'
        # qq邮件服务器
        # smtpserver = 'smtp.qq.com'
        # smtpserver = 'SMTP.foxmail.com'
        # foxmail 邮件服务器
        smtpserver = 'mail.pgl-world.com'
        # 发件人和密码
        # sender = '1746053395@qq.com'
        # foxmail 账号
        sender = 'moshuangyou@pgl-world.com'
        # password = 'doxomckblzupdfjj'  #不是真实的邮箱密码，需要去邮箱设置pop3，会收到短信， sender = '1746053395@qq.com'
        # foxmail 密码
        password = 'msy19931214'  # 不是真实的邮箱密码，需要去邮箱设置pop3，会收到短信，
        # 此短信就用于自动化的邮箱密码;过段时间使用显示已经关闭，要重新开通
        # 接收人
        receivers = receive_email
        # 邮件主题
        subject = retm
        msgRoot = MIMEMultipart()
        msgRoot['Subject'] = subject
        msgRoot['From'] = sender
        # 判断输入邮箱长度，大于1则群发
        if len(receivers) > 1:
            msgRoot['To'] = ','.join(receivers)
            # msgRoot['To']=receivers
        else:
            msgRoot['To'] = receivers[0]
        part = MIMEText(content)
        msgRoot.attach(part)

        # ----------------------------------------------------------
        # 添加附件
        for path in filepath:
            file_name = path.split("\\")[-1]
            part = MIMEApplication(open(path, 'rb').read())
            part.add_header('Content-Disposition', 'attachment', filename=file_name)
            msgRoot.attach(part)
        # ----------------------------------------------------------
        # 连接登录邮箱
        server = smtplib.SMTP(smtpserver, 25)
        server = smtplib.SMTP(smtpserver, 25)
        server.login(sender, password)
        # ----------------------------------------------------------
        # 发送邮件
        # server.sendmail(sender, receivers, msgRoot.as_string())
        server.sendmail(sender, msgRoot['To'].split(','), msgRoot.as_string())
        server.quit()
        print("发送成功!")
    except Exception as e:
        print(e)

