#coding=utf-8
#author:decai.li    2018.01.23
from appium import webdriver
import sys
import re
import time
import pytesseract
import ImageHelper
import unittest
import os

global TolerableValue
TolerableValue=3.2

class Student_Overdraw(unittest.TestCase):
    # 家长端 - 可以
    @classmethod
    def setUpClass(self):
        # 配置信息，后期变成可更改的,并增加爬虫安装部分
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '4.4'
        desired_caps['deviceName'] = 'S8S4NNC6OJVSORKR'
        desired_caps['appPackage'] = 'com.A17zuoye.mobile.homework'
        desired_caps['appActivity'] = 'com.A17zuoye.mobile.homework.main.activity.WelcomeActivity'
        global driver
        driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    @classmethod
    def tearDownClass(self):
        driver.quit()

    def test_01_Firstpage(self):
        driver.get_screenshot_as_file(os.path.join('.', 'student_Screenshot', sys._getframe().f_code.co_name[:7] + '.png'))
        res = ImageHelper.getOverDraw('.\\student_Screenshot\\' + sys._getframe().f_code.co_name[:7] + '.png')
        assert res <= TolerableValue, 'Maybe OverDraw,Please check the options with OverDraw Value:' + str(res)

    def test_02_LoginPage(self):
        time.sleep(20)
        driver.get_screenshot_as_file(os.path.join('.', 'student_Screenshot', sys._getframe().f_code.co_name[:7] + '.png'))
        res = ImageHelper.getOverDraw('.\\student_Screenshot\\' + sys._getframe().f_code.co_name[:7] + '.png')
        assert res <= TolerableValue, 'Maybe OverDraw,Please check the options with OverDraw Value:' + str(res)

