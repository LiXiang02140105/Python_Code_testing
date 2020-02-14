import unittest,time,os
import HtmlTestRunner
 
def get_allCases(folders = []):
    '''获取所有测试用例
    []: 默认全部
    '''
    suite = unittest.TestSuite()
    case_path = './cases'
    if folders == []:
        discover = unittest.defaultTestLoader.discover(case_path,pattern='test*.py')
        suite.addTest(discover)
    else:
        for folder in folders:
            path = (case_path + "/" + folder)
            print(path)
            discover = unittest.defaultTestLoader.discover(path,pattern='test*.py')
            suite.addTest(discover)
    return suite

def runCase(folders = []):
    """
    with open("./Result/" + time.strftime("%Y%m%d_%H%M%S") + ".txt", 'w+', encoding='utf-8') as fp:  
        runner = unittest.TextTestRunner(stream=fp,verbosity=2)
        runner.run(get_allCases(folders))
    """
    with open("./Result/HTML/" + time.strftime("%Y%m%d_%H%M%S") + ".txt", 'w+') as fp:
        runner = HtmlTestRunner.HTMLTestRunner(stream=fp, report_title='Kindergraden Auto Test', descriptions=time.strftime("%Y%m%d_%H%M%S"), verbosity=2)
        # report_title='幼儿园自动化测试', 
        runner.run(get_allCases(folders))
        time.sleep(10)
        fp.close()
["yangxinzhi"]
runCase(["yangxinzhi"])