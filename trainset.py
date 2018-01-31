from appium import webdriver
import sys
import re
import time
import pytesseract
import ImageHelper
import unittest
from PIL import Image
import HtmlTestRunner

#手动截取各种数字进行训练,练完了就没用了
desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '4.4'
desired_caps['deviceName'] = 'S8S4NNC6OJVSORKR'
desired_caps['appPackage'] = 'com.yiqizuoye.teacher'
desired_caps['appActivity'] = '.login.TeacherWelcomeActivity'
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

time.sleep(40)
driver.get_screenshot_as_file(".\\teacher_Screenshot\\incl7.png")
res = ImageHelper.getOverDraw(".\\teacher_Screenshot\\incl7.png")