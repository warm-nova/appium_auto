import unittest
import Mainstream_Teacher
import Mainstream_Parent
import Mainstream_Student
import configparser
import unittest
from HtmlTestRunner import HTMLTestRunner
import subprocess

#主流程
if __name__ == "__main__":
    order = 'adb shell setprop debug.hwui.overdraw count'  # 打开渲染开关
    pi = subprocess.Popen(order, shell=True, stdout=subprocess.PIPE)

    suite = unittest.makeSuite(Mainstream_Teacher.Teacher_Overdraw , 'test')
    suite.addTests(unittest.makeSuite(Mainstream_Parent.Parent_Overdraw,'test'))

    #联动到配置文件里，上野联动一死一送
    
    outputName = 'OverDraw'
    runner = HTMLTestRunner(output=outputName)
    cf = configparser.ConfigParser()
    cf.read('config.conf')
    cf.set('folder','Keyfolder',outputName)
    cf.write(open("config.conf","w"))

    runner.run(suite)
    orderoff = 'adb shell setprop debug.hwui.overdraw false'  # 打开渲染开关
    pi = subprocess.Popen(order, shell=True, stdout=subprocess.PIPE)
