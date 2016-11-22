# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
import time
brower = webdriver.Chrome()
#open a brower
brower.get("http://www.kypay.com/login.html")
#auto login
brower.find_element_by_id("userName").send_keys("admin")
brower.find_element_by_id("passWord").send_keys("che001")
brower.find_element_by_id("submitValideat").click()
time.sleep(2)
#how to handle ajax?
#now it's the element work!!
element=WebDriverWait(brower, 10).until(lambda driver : driver.find_element_by_class_name("select_menu"))
element.find_element_by_xpath("//option[@value='fffe987d-db14-42e2-3331-5d4e386ec002']").click()
element.find_element_by_xpath("//div[3]/ul/li[2]").click()
element.find_element_by_xpath('//*[@id="ffbtgbf-197c-4948-8436-62dzgsglf9188"]').click()
time.sleep(2)
element.find_element_by_xpath('//div[4]/div[2]/div/div/div[2]/form/div[1]/div/div[1]/input[2]').send_keys("1")
element.find_element_by_xpath('//div[4]/div[2]/div/div/div[2]/form/div[1]/div/div[3]/input[1]').click()
time.sleep(2)
element.find_element_by_xpath('//div[4]/div[2]/div/div/div[3]/table/tbody/tr[1]/td[7]/a[2]').click()

#brower.quit()
