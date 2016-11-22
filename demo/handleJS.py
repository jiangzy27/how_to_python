# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
brower = webdriver.Chrome()
#open a brower
brower.get("http://www.kypay.com/login.html")
#auto login
brower.find_element_by_id("userName").send_keys("admin")
brower.find_element_by_id("passWord").send_keys("che001")
brower.find_element_by_id("submitValideat").click()
time.sleep(5)
#run js and goto,but cannot get the permission.
brower.execute_script('loadingUrl("/backend-credit/busine/credit/creditManager.html");')
time.sleep(5)
#find element by class name
#input chinese characters and submit
brower.find_element_by_class_name("search_customerName").send_keys(unicode("用户名5b4578edbe10", "utf-8"))
brower.find_element_by_class_name("searchPersonalBtn").click()

#brower.quit()
