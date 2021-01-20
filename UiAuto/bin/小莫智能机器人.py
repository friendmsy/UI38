from apscheduler.schedulers.blocking import BlockingScheduler
import time
from datetime import datetime
import subprocess


def job():
    print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    bat_name = 'E:\\software\\Python3.8.3\\UiAuto\\bin\\multiprocess(2)_start.bat'
    print(bat_name)
    # cmd = 'cmd.exe ' + bat_name
    # 其中input_var是输入参数变量
    p = subprocess.Popen("cmd.exe /c " + bat_name, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    curline = p.stdout.readline()
    while (curline != b''):
        if len(curline) > 2:
            print(curline.decode('gbk'))
    curline = p.stdout.readline()

    p.wait()


scheduler = BlockingScheduler()
scheduler.add_job(job, 'cron', hour='0-23', minute='42')
scheduler.start()


# scheduler.add_job(job, 'cron', day_of_week='1-5', hour=6, minute=1)
# scheduler.add_job(my_job, 'date', run_date=date(2009, 11, 6), args=['text'])
# scheduler.add_job(my_job, 'date', run_date=datetime(2009, 11, 6, 16, 30, 5), args=['text'])
# scheduler.add_job(my_job, 'date', run_date='2009-11-06 16:30:05', args=['text'])
# scheduler.add_job(my_job, args=['text'])
# scheduler.add_job(job, 'interval', seconds=5)  # 在运行程序5秒后，第一次输出时间。
# scheduler.add_job(job, 'interval', minutes=60)  # 在运行程序5秒后，第一次输出时间。
