"""用来查看log
"""
from selector import *
from airtest.core.api import connect_device
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
import time
import subprocess


class RunnerTest:
    def __init__(self):
        self.poco = AndroidUiautomationPoco()
    
    def runner(self):
        """
        1、启动crashlog
        2、subprocess启动runner Test
        """
        i = 1
        while True:
            print("\n第 %d 次 开始" % i, "time: ",time.strftime("%Y%m%d %H:%M:%S"),"\n")
            self.pid = subprocess.Popen("C:/Users/cm/AppData/Local/Programs/Python/Python37/python.exe ./tools/LoadCases.py", shell=True)
            while self.crashLogsPoco() == False:
                time.sleep(1)
                if self.pid.poll() == 0:
                    # 说明这次没有崩溃，结束了进程
                    # 因此成功结束本次
                    break
            if self.crashLogsPoco():
                while self.pid.poll() == None:
                    self.pid.kill()
                    time.sleep(1.5)
                while self.poco(text="^.*重新打开应用.*$").exists():
                    self.poco(text="^.*重新打开应用.*$").click()
                    time.sleep(1.5)
                #self.pid = subprocess.Popen("python ./LoadCases.py")
                #print("\n第 %d 次 重新开始" % i, "time: ",time.strftime("%Y%m%d %H:%M:%S"),"\n")
                
            while self.pid.poll() == None:
                self.pid.kill()
                time.sleep(1.5)
            print("")
            print("\n第 %d 次 结束" % i, "time: ",time.strftime("%Y%m%d %H:%M:%S"),"\n")
            i += 1
        
    def crashLogsPoco(self):
        '''观察是否有崩溃'''
        self.crash = False  
        if self.poco(text="^.*崩溃.*$").exists():
            print("发生崩溃")
            self.catch_picture() # 得到图片
            self.crash = True
        time.sleep(3)  
        return self.crash

    def catch_picture(self):
        from airtest.core.api import snapshot
        import datetime,os
        filename = "./Result/picture/" + datetime.datetime.now().strftime("%Y%m%d-%H%H%S") + ".png"
        msg = "崩溃"
        snapshot(filename=filename, msg=msg, quality=ST.SNAPSHOT_QUALITY)

class CrashLogsUI2:
    def __init__(self):
        self.page = adbPage() # 传入adb

    def catch_picture(self):
        self.page.screenshot() # 得到图片

    def watchUI2(self):
        '''观察是否有崩溃'''
        crash = ('resourceId','android:id/alertTitle')
        close_crash = ('resourceId', 'android:id/aerr_close')
        while True:
            print("read")
            if self.page.isExist(crash):
                print("发生崩溃")
                self.catch_picture() # 得到图片
                break
            time.sleep(3)
        while not self.page.isExist(close_crash):
            time.sleep(3)
        self.page.click_gone(close_crash)


runner = RunnerTest()
runner.runner()