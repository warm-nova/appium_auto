#coding=utf-8
#author:decai.li    2018.01.23
from appium import webdriver
import sys
import time
import pytesseract
import ImageHelper
import unittest
from PIL import Image
import HtmlTestRunner
import AipOcr
import subprocess
import configparser

#超过层级大于此，则报错
global TolerableValue
TolerableValue=3.2


class Teacher_Overdraw(unittest.TestCase):
    #超过多少层级,则报错
    @classmethod
    def setUpClass(self):
        # 配置信息，后期变成可更改的,并增加爬虫安装部分
        cf = configparser.ConfigParser()
        cf.read("config.conf")

        desired_caps = {}
        desired_caps['platformName'] = cf.get('device', 'platformName')
        desired_caps['platformVersion'] = cf.get('device', 'platformVersion')
        desired_caps['deviceName'] = cf.get('device', 'deviceName')
        desired_caps['appPackage'] = cf.get('packageinfo', 'teacherPackage')
        desired_caps['appActivity'] = cf.get('packageinfo', 'teacherActivity')
        global driver
        driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    @classmethod
    def tearDownClass(self):
        driver.quit()

    def test_01_WelcomePage(self):
        # 1-欢迎界面
        driver.implicitly_wait(10)
        driver.get_screenshot_as_file('.\\teacher_Screenshot\\'+sys._getframe().f_code.co_name[:7]+'.png')
        res = ImageHelper.getOverDraw('.\\teacher_Screenshot\\'+sys._getframe().f_code.co_name[:7]+'.png')
        assert res<=TolerableValue ,'Maybe OverDraw,Please check the options with OverDraw Value:'+str(res)

    def test_02_LoginPage(self):
        # 2-登录界面
        driver.implicitly_wait(10)
        time.sleep(5)
        driver.find_element_by_id("com.yiqizuoye.teacher:id/teacher_guide_btn_login").click()
        driver.get_screenshot_as_file('.\\teacher_Screenshot\\'+sys._getframe().f_code.co_name[:7]+'.png')
        res = ImageHelper.getOverDraw('.\\teacher_Screenshot\\'+sys._getframe().f_code.co_name[:7]+'.png')
        assert res<=TolerableValue , 'Maybe OverDraw,Please check the options with OverDraw Value:'+str(res)

    def test_03_TeacherMainPage(self):
        # 3-输入用户名和密码
        driver.find_elements_by_class_name("android.widget.EditText")[0].click()
        driver.find_elements_by_class_name("android.widget.EditText")[0].send_keys("10030000003")
        driver.find_elements_by_class_name("android.widget.EditText")[1].click()
        driver.find_elements_by_class_name("android.widget.EditText")[1].send_keys("123")
        driver.find_element_by_id("com.yiqizuoye.teacher:id/teacher_login_btn_login").click()
        time.sleep(10)
        driver.get_screenshot_as_file('.\\teacher_Screenshot\\'+sys._getframe().f_code.co_name[:7]+'.png')
        res = ImageHelper.getOverDraw('.\\teacher_Screenshot\\'+sys._getframe().f_code.co_name[:7]+'.png')
        assert res <= TolerableValue, 'Maybe OverDraw,Please check the options with OverDraw Value:' + str(res)

    def test_04_AssignHomework(self):
        # 4-布置作业
        driver.find_element_by_id("com.yiqizuoye.teacher:id/teacher_set_homework_btn").click()
        time.sleep(5)
        driver.get_screenshot_as_file('.\\teacher_Screenshot\\'+sys._getframe().f_code.co_name[:7]+'.png')
        res = ImageHelper.getOverDraw('.\\teacher_Screenshot\\'+sys._getframe().f_code.co_name[:7]+'.png')
        assert res <= TolerableValue, 'Maybe OverDraw,Please check the options with OverDraw Value:' + str(res)

    def test_05_CheckHomework(self):
        # 5-检查作业
        driver.press_keycode(4)
        driver.find_element_by_id("com.yiqizuoye.teacher:id/teacher_check_homework_btn").click()
        time.sleep(5)
        driver.get_screenshot_as_file('.\\teacher_Screenshot\\'+sys._getframe().f_code.co_name[:7]+'.png')
        res = ImageHelper.getOverDraw('.\\teacher_Screenshot\\'+sys._getframe().f_code.co_name[:7]+'.png')
        assert res <= TolerableValue, 'Maybe OverDraw,Please check the options with OverDraw Value:' + str(res)

    #非native页面数值均不准确，不予以测试

    def test_06_MyStatus(self):
        # 6-我的界面
        driver.press_keycode(4)
        driver.find_element_by_id("com.yiqizuoye.teacher:id/teacher_main_activity_bottom_tab_me").click()
        time.sleep(3)
        driver.get_screenshot_as_file('.\\teacher_Screenshot\\'+sys._getframe().f_code.co_name[:7]+'.png')
        res = ImageHelper.getOverDraw('.\\teacher_Screenshot\\'+sys._getframe().f_code.co_name[:7]+'.png')
        assert res <= TolerableValue, 'Maybe OverDraw,Please check the options with OverDraw Value:' + str(res)

    def test_07_EnterMyClass(self):
        # 7-我的班级
        driver.find_element_by_id("com.yiqizuoye.teacher:id/teacher_clazz_info_layout").click()
        driver.find_element_by_id("com.yiqizuoye.teacher:id/tv_class_create").click()
        time.sleep(3)
        driver.get_screenshot_as_file('.\\teacher_Screenshot\\'+sys._getframe().f_code.co_name[:7]+'.png')
        res = ImageHelper.getOverDraw('.\\teacher_Screenshot\\' + sys._getframe().f_code.co_name[:7] + '.png')
        assert res <= TolerableValue, 'Maybe OverDraw,Please check the options with OverDraw Value:' + str(res)


    def test_08_PersonalInfo(self):
        # 8-我的个人信息
        driver.find_element_by_id("com.yiqizuoye.teacher:id/teacher_common_header_left_button").click()
        time.sleep(2)
        driver.find_element_by_id("com.yiqizuoye.teacher:id/teacher_common_header_left_button").click()
        time.sleep(3)
        driver.find_elements_by_id("com.yiqizuoye.teacher:id/grid_item_layout")[0].click()
        driver.get_screenshot_as_file('.\\teacher_Screenshot\\' + sys._getframe().f_code.co_name[:7] + '.png')
        res = ImageHelper.getOverDraw('.\\teacher_Screenshot\\' + sys._getframe().f_code.co_name[:7] + '.png')
        assert res <= TolerableValue, 'Maybe OverDraw,Please check the options with OverDraw Value:' + str(res)

    def test_09_options(self):
        driver.find_element_by_id("com.yiqizuoye.teacher:id/teacher_common_header_left_button").click()
        time.sleep(2)
        driver.find_elements_by_id("com.yiqizuoye.teacher:id/grid_item_layout")[3].click()
        driver.get_screenshot_as_file('.\\teacher_Screenshot\\' + sys._getframe().f_code.co_name[:7] + '.png')
        res = ImageHelper.getOverDraw('.\\teacher_Screenshot\\' + sys._getframe().f_code.co_name[:7] + '.png')
        assert res <= TolerableValue, 'Maybe OverDraw,Please check the options with OverDraw Value:' + str(res)






