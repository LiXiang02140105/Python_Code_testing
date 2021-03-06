from cases import *
import unittest,time
import subprocess
import datetime
from tools.analysisReport import *

def runnerTest():
    logfile = "./logs/deviceLog_"  + time.strftime("%Y%m%d_%H%M%S") + ".txt"
    with open(logfile, "w+",encoding="utf-8") as fp:
        logRecord_pid = subprocess.Popen("D:/platform-tools_r29.0.5-windows/platform-tools/adb.exe logcat",stdout=fp, shell=True)
        logCrash_pid = subprocess.call("C:/Users/cm/AppData/Local/Programs/Python/Python37/python.exe ./tools/CrashLogs.py", shell=True) # 阻塞等待完成
        time.sleep(10)
        while logRecord_pid.poll() == None:
            logRecord_pid.kill()
            time.sleep(1.5)
        fp.close()

def local_test(starttime):
    import datetime,schedule
    from apscheduler.schedulers.background import BackgroundScheduler

    schedule.every().day.at(starttime).do(runnerTest)
    while True:
        try:
            schedule.run_pending()
        finally:
            pass
            # analysisReport()

def jenkins_test():
    runnerTest()
    
if __name__ == "__main__":
    # jenkins_test() # 使用Jenkins
    starttime = (datetime.datetime.now() + datetime.timedelta(seconds=60)).strftime("%H:%M")
    print(starttime)
    local_test(starttime) # 本地跑