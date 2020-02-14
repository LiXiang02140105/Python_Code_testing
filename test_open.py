from airtest.core.api import connect_device
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
from airtest.core.api import start_app, stop_app, Template, exists
import unittest
import time,random,datetime,os

class test_open(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.poco = AndroidUiautomationPoco()
        # 桌面 的APP text
        cls.parent = "爱优校-家长"
        cls.teacher = "爱优校-园丁"
        cls.manager = "校园门禁通-园丁"

        cls.poco.device.wake() # 回到首页 home键的首页
        cls.poco.device.home()
        cls.child = "卡布达"

    def test_01_open_app(self):
        self.poco(text="爱优校-家长").click()
        # APP 底部的button
        self.school_button = self.poco("android:id/content").child("android.view.View").child("android.view.View").child("android.view.View").child("android.view.View").child("android.widget.ImageView")[0]
        self.interact_button = self.poco("android:id/content").child("android.view.View").child("android.view.View").child("android.view.View").child("android.view.View").child("android.widget.ImageView")[1]
        self.myself_button = self.poco("android:id/content").child("android.view.View").child("android.view.View").child("android.view.View").child("android.view.View").child("android.widget.ImageView")[2]

        self.school_button.click()
        self.assertTrue(self.poco(text="人脸录入").exists(), msg="未进入APP")


    def test_02_change_child(self):
        while(self.poco(text=self.child).exists() == False):
            self.poco(text="车轮滚...").click()
            time.sleep(1.5)
        self.poco(text=self.child).click()
        self.assertTrue(self.poco(text=self.child).exists(), msg="未切换成功")
        
    


