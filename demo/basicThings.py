# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time
brower = webdriver.Chrome()
brower.get("http://www.example.com/login.html")
brower.find_element_by_id("userName").send_keys("admin")
brower.find_element_by_id("passWord").send_keys("123456")
brower.find_element_by_class_name("button-login").click()
time.sleep(2)
#run js
brower.execute_script('my_loadingUrl("/backend-credit/busine/credit/creditManager.html");');
brower.find_element_by_id("selectBtn").click()

#brower.quit()
