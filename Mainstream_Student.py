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
import subprocess

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
      #  assert res <= TolerableValue, 'Maybe OverDraw,Please check the options with OverDraw Value:' + str(res)

    def test_02_LoginPage(self):
        time.sleep(20)
        driver.get_screenshot_as_file(os.path.join('.', 'student_Screenshot', sys._getframe().f_code.co_name[:7] + '.png'))
        res = ImageHelper.getOverDraw('.\\student_Screenshot\\' + sys._getframe().f_code.co_name[:7] + '.png')
      #  assert res <= TolerableValue, 'Maybe OverDraw,Please check the options with OverDraw Value:' + str(res)

    def test_03_LogingStudent(self):
        driver.find_element_by_id("com.A17zuoye.mobile.homework:id/main_guid_login_btn").click()

        driver.find_element_by_id("com.A17zuoye.mobile.homework:id/main_login_edit_account").click()
        driver.find_element_by_id("com.A17zuoye.mobile.homework:id/main_login_edit_account").send_keys("11030000001")
        driver.find_element_by_id("com.A17zuoye.mobile.homework:id/main_login_edit_pwd").click()
        driver.find_element_by_id("com.A17zuoye.mobile.homework:id/main_login_edit_pwd").send_keys("123")
        driver.find_element_by_id("com.A17zuoye.mobile.homework:id/main_login_btn_login").click()

        time.sleep(15)
        driver.get_screenshot_as_file(
            os.path.join('.', 'student_Screenshot', sys._getframe().f_code.co_name[:7] + '.png'))
        res = ImageHelper.getOverDraw('.\\student_Screenshot\\' + sys._getframe().f_code.co_name[:7] + '.png')

      #  assert res <= TolerableValue, 'Maybe OverDraw,Please check the options with OverDraw Value:' + str(res)

 #   def test_04_GrowWorld(self):
 #       driver.find_elements_by_id("com.A17zuoye.mobile.homework:id/primary_student_funny_function_image")[0].click()
 #       time.sleep(3)
 #       driver.get_screenshot_as_file(
 #           os.path.join('.', 'student_Screenshot', sys._getframe().f_code.co_name[:7] + '.png'))
 #       res = ImageHelper.getOverDraw('.\\student_Screenshot\\' + sys._getframe().f_code.co_name[:7] + '.png')

    #  assert res <= TolerableValue, 'Maybe OverDraw,Please check the options with OverDraw Value:' + str(res)

    def test_04_InfoCenter(self):
        time.sleep(20)
        driver.press_keycode(4)
        driver.find_element_by_id("com.A17zuoye.mobile.homework:id/primary_student_message_btn").click()
        time.sleep(5)
        driver.get_screenshot_as_file(
            os.path.join('.', 'student_Screenshot', sys._getframe().f_code.co_name[:7] + '.png'))
        res = ImageHelper.getOverDraw('.\\student_Screenshot\\' + sys._getframe().f_code.co_name[:7] + '.png')
        assert res <= TolerableValue, 'Maybe OverDraw,Please check the options with OverDraw Value:' + str(res)

    def test_05_MyPersonalPage(self):
        time.sleep(5)
        driver.press_keycode(4)
        driver.find_elements_by_id("com.A17zuoye.mobile.homework:id/primary_rel")[3].click()
        time.sleep(5)
        driver.get_screenshot_as_file(
            os.path.join('.', 'student_Screenshot', sys._getframe().f_code.co_name[:7] + '.png'))
        res = ImageHelper.getOverDraw('.\\student_Screenshot\\' + sys._getframe().f_code.co_name[:7] + '.png')

    

