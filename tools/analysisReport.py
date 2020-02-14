import os,datetime

def get_filename():
    return os.listdir("../report") 

def check_report(filename, failresult):
    path = os.getcwd()
    path = "../report"
    failcase = []
    with open(path + "/" + filename, "r", encoding="utf-8") as fp:
        contents = fp.readlines()
    #print(contents)
    for line in contents:
        #if "ok" in line:
        if "... FAIL" in line or "... ERROR" in line:
            print(line)
            failcase.append(line)
    name = filename.split(".")[-2].split("_")
    name = name[-2] + "_" + name[-1]
    if failcase != []:
        failresult[name] = failcase
    
    fp.close()    
    return failresult

def write_result(failresult):
    """ 把check的结果放进一个文件里 """
    fp = open("../report/txt" + datetime.datetime.now().strftime("%Y%m%d_%H%M%S") + ".txt", "w+", encoding="utf-8")
    for name, results in failresult.items():
        fp.writelines(name + "\n")
        for re in results:
            fp.write("\t" + re)
    fp.close()

def analysisReport():
    failresult = {}
    files = get_filename()
    for file in files:
        failresult = check_report(file,failresult)  
    write_result(failresult)

if __name__ == "__main__":
    failresult = {}
    files = get_filename()
 
    failresult = check_report("/result_20200210_163413.txt",failresult)
    write_result(failresult)