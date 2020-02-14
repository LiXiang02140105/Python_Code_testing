'''
监测文件上传
'''
import subprocess,os
from datetime import datetime
import queue
'''遗留问题
1、不知道是哪个病患的文件上传: 可以等到检测到上传完成后再进行新一轮上传
2、在获取time_sum的时候，需要更新到获取的log中的日期
3、没有做图表
'''

def FileUpload():
    '''
    属性:
        1、cmd_sys: logcat的命令行对象
        2、result: 返回
    '''
    cmd_sys = ''
    #file.queue = 
    def __init__(self):
        self.get_devices_Info()
        #self.clear_log()
        self.cmd_sys = subprocess('adb -s %s logcat | grep "UploadService".*"upload"',shell=True, stdout=subprocess.PIPE, bufsize=1, stderr=subprocess.STDOUT)


    def start_Upload(self):
        '''在结束脑疾病测试时开始获取log
        判断是不是开始上传文件
        False: 等待了 5min10, 还没有开始上传
        True: 开始上传了
        '''
        startTime = datetime.now()
        while ((datetime.now()-startTime).seconds < 310) and self.cmd_sys.poll() is None:
            self.line = self.cmd_sys.stdout.readline() # byte-like object, 所以需要从 byte -> str
            self.line = str(self.line.strip(), encoding="utf-8")
            if "UploadService: start upload file:_tongue.mp4" in self.line:
                line_next = fp.readline() # 下一行
                if "result:true" in line:
                    # 如果上传成功 开始计时
                    start_time = line_next.split(" ")
                    self.date,self.time = start_time[0],start_time[1]
                    #self.
                    # 开始计时
                    interval = self.start_count_time(self.line,line_next)
            line = fp.readline() # 获得下一行
        print("当前 5 分钟没有上传的文件")
        return False
    
    def clear_log(self):
        os.system('adb -s %s logcat -c' % self.serial, shell=True)


    def get_devices_Info(self):
        '''得到设备 sn号
        '''
        out = os.system('adb devices', shell=True, stdout=subprocess.PIPE)
        devicesList = out.stdout.read().splitlines()
        serial = ''
        if len(devicesList) > 2:
            for item in devicesList:
                #if 'L1A' in str(item, encoding='utf-8'):
                serial = item.split()[0]

            self.serial = str(serial_nos, encoding='utf-8')
            return self.serial
        else:
            return -1

def start_count_time(line,line_next):
    '''当开始上传文件时,记录每次上传文件所需的时间
    '''
    start = line.split(" ")
    time_1 = start[0] + ' ' + start[1]
    time_1 = datetime.strptime(datetime.now().strftime('%Y-') + time_1, '%Y-%m-%d %H:%M:%S.%f')
    end = line_next.split(" ")
    time_2 = end[0] + ' ' + end[1]
    time_2 = datetime.strptime(datetime.now().strftime('%Y-') + time_2, '%Y-%m-%d %H:%M:%S.%f')
    interval = time_2 - time_1
    return interval


if __name__ == "__main__":
    file_names = ['_tongue.mp4','_tongue_2.mp4','_tongue_3.mp4','_word_f.mp4','_pic.jpg','_word_l.mp4','_color_f.mp4','_color_l.mp4']
    file_queue = queue.Queue()
    for name in file_names:
        file_queue.put(name)
    time_sum = datetime.strptime(datetime.now().strftime('%Y-%m-%d') + ' 00:00:00.000', '%Y-%m-%d %H:%M:%S.%f')
    with open('../upload.txt',encoding='utf-8') as fp:
        name = file_queue.get()
        line = fp.readline()
        while line:
            if "UploadService: start upload file:%s" % name in line:
                line_next = fp.readline() # 下一行
                print('line_next:', line_next)
                if 'end upload file:%s' % name in line_next and "result:true" in line_next:
                    # 如果上传成功 开始计时
                    #self.
                    # 开始计时
                    interval = start_count_time(line,line_next)
                    time_sum += interval
                    print(interval)
                    print("sum:",time_sum)
                    
                    name = file_queue.get()
            line = fp.readline() # 获得下一行
            
        
