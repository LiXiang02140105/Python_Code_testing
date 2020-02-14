'''封装adb查找元素的方法
'''
import uiautomator2 as u2
import time, datetime


class adbApp():
    '''封装对pad的一些基础的操作
    shell/ 截图/ 检查更新、安装新的APP/ 检测崩溃
    '''
    def __init__(self):
        self.d = u2.connect_adb_wifi("192.168.1.105:5555")
    
    
    def shell(self, cmd):
        '''调用adb的shell方法
        cmd:需要使用的shell命令
        '''
        return self.d.shell(cmd, timeout=30)
    

class adbPage(adbApp):
    '''获取页面对象的方法封装'''
    def __init__(self):
        # activity
        super().__init__()
        #print(self.d.info) # 重写父类, 得到父类初始化的方法
        #self.activity = activity
    
    def click(self, obj):
        '''封装点击事件
        '''
        if obj[0] == 'xpath':
            self.d.xpath(obj[1]).click()

        elif obj[0] in ['resourceId','className','text']:
            click_obj = self.findObj(obj) # 返回找到的对象
            if click_obj:
                click_obj.click() # 点击对象
            else:
                return False
            
        else:
            # 数字
            self.d.click(obj[0],obj[1])
        return True

    def click_gone(self, obj):
        '''封装 点击-直到消失 事件
        '''
        if obj[0] in ['resourceId','className','text']:
            click_obj = self.findObj(obj) # 返回找到的对象
            if click_obj:
                click_obj.click_gone(maxretry=10, interval=2.5) # 点击对象
            else:
                return False        
        else:
            print("暂不支持!")
            return False
        return True

    def swipe_to_End(self):
        ''' 界面 上拉加载 '''
        return self.d(scrollable=True).fling.toEnd()

    def swipe_from_Top(self):
        ''' 界面 下拉刷新 '''
        return self.d(scrollable=True).fling.vert.backward()

    def get_info(self,obj):
        '''封装获取控件信息
        返回获取控件信息
        '''
        if obj[0] == 'xpath':
            info = {
                'text' : self.d.xpath(obj[1]).all()[0].text,
                'attr' : self.d.xpath(obj[1]).all()[0].attrib
            }
            
        elif obj[0] in ['resourceId','className','text']:
            obj = self.findObj(obj) # 返回找到的对象
            if obj:
                info = {
                    'text' : obj.get_text(),
                    'attr' : obj.info
                }
                # print(info,'\n', obj[1])
            else:
                return False
            
        else:
            # 数字
            print("暂不支持")
        return info

    def keyboard(self, type):
        '''封装键盘事件'''
        pass
    
    def home(self):
        '''返回首页'''
        self.shell("am start -n com.ainirobot.moduleapp/.MainActivity")
        time.sleep(1)
        obj = ('text','脑疾病问诊')
        face_click = (0.5, 0.5)
        while not self.isExist(obj):
            print('没有找到首页')
            self.click(face_click)
            time.sleep(1)
        print("首页")
            
    def isExist(self,obj):
        '''当不确定用检查对象是否存在'''
        if self.findObj(obj).exists(timeout=10):
            print('对象 %s 存在' % self.findObj(obj).info['text'])
            return True
        else:
            return False
              

    def findObj(self, obj):
        '''封装查找方法
        返回对象(用来点击)
        '''
        method, value = obj[0], obj[1]
        if method == 'resourceId':
            return self.d(resourceId = value)
        elif method == 'text':
            return self.d(text = value)
        elif method == 'className':
            return self.d(className = value)
        elif method == 'xpath':
            return self.d.xpath(obj[1])
        else:
            print("当前方法不支持")
            return False
        
    def checkActivity(self):
        app_activity = self.activity # APP 需要的 activity
        cur_activity = self.shell("dumpsys window w | grep name=")
        if app_activity in activity.output.split()[0]:
            return True
        else:
            return False

    def screenshot(self, path=".\Result\picture"):
        pic_name = datetime.datetime.now().strftime("%y%m%d_%H%M%S")
        self.d.screenshot(path + pic_name + ".jpg")

class adbLog(adbApp):
    pass


if __name__ == "__main__":
    #app = adbApp()
    page = adbPage()
    activity = page.shell("dumpsys window w | grep name=")
    if 'BrainTestActivity' in activity.output.split()[0]:
        print(True)
    else:
        print(False)
