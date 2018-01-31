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

class Parent_Overdraw(unittest.TestCase):
    # 家长端 - 可以
    @classmethod
    def setUpClass(self):
        # 配置信息，后期变成可更改的,并增加爬虫安装部分
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '4.4'
        desired_caps['deviceName'] = 'S8S4NNC6OJVSORKR'
        desired_caps['appPackage'] = 'com.yiqizuoye.jzt'
        desired_caps['appActivity'] = 'com.yiqizuoye.jzt.activity.WelcomeActivity'
        global driver
        driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    @classmethod
    def tearDownClass(self):
        driver.quit()

    def test_01_FirstPage(self):
        driver.implicitly_wait(20)
        driver.get_screenshot_as_file(os.path.join('.','parent_Screenshot',sys._getframe().f_code.co_name[:7] + '.png'))
        res = ImageHelper.getOverDraw('.\\parent_Screenshot\\' + sys._getframe().f_code.co_name[:7] + '.png')
        assert res <= TolerableValue, 'Maybe OverDraw,Please check the options with OverDraw Value:' + str(res)

    def parent_swipe(x, y):
        driver.swipe(6 / 7 * x, 1 / 2 * y, 1 / 7 * x, 1 / 2 * y, 1000)
        time.sleep(4)

    def test_02_SwipeWelcomePage(self):
        #首次启动之后有三次页面的滑动
        time.sleep(20)
        x = driver.get_window_size()['width']
        y = driver.get_window_size()['height']
        for i in range(3):
            Parent_Overdraw.parent_swipe(x,y)
        driver.get_screenshot_as_file('.\\parent_Screenshot\\' + sys._getframe().f_code.co_name[:7] + '.png')
       # res = ImageHelper.getOverDraw('.\\parent_Screenshot\\' + sys._getframe().f_code.co_name[:7] + '.png')
        driver.find_element_by_id("com.yiqizuoye.jzt:id/guid_login_btn").click()
     #   assert res <= TolerableValue, 'Maybe OverDraw,Please check the options with OverDraw Value:' + str(res)




    def test_03_LoginPage(self):
        driver.implicitly_wait(20)
        driver.find_element_by_id("com.yiqizuoye.jzt:id/login_new_user_skip").click()
        driver.implicitly_wait(10)
        driver.get_screenshot_as_file('.\\parent_Screenshot\\' + sys._getframe().f_code.co_name[:7] + '.png')
        res = ImageHelper.getOverDraw('.\\parent_Screenshot\\' + sys._getframe().f_code.co_name[:7] + '.png')
        time.sleep(3)
        assert res <= TolerableValue, 'Maybe OverDraw,Please check the options with OverDraw Value:' + str(res)


    def test_04_MyProfile(self):
        driver.find_element_by_id("com.yiqizuoye.jzt:id/activity_main_bottom_tab_user_img").click()
        driver.get_screenshot_as_file('.\\parent_Screenshot\\' + sys._getframe().f_code.co_name[:7] + '.png')
        res = ImageHelper.getOverDraw('.\\parent_Screenshot\\' + sys._getframe().f_code.co_name[:7] + '.png')
        print(driver.current_activity)
        time.sleep(3)
        assert res <= TolerableValue, 'Maybe OverDraw,Please check the options with OverDraw Value:' + str(res)

        #中间两个模块，涉及到webview，暂时获取不到



