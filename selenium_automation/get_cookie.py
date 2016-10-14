# -*- coding: utf-8 -*-
from selenium import webdriver
import time

#这个脚本用于获取Affiliate系统浏览器的cookie
#base_url="http://54.67.94.143:9091"#docker环境地址
base_url="http://aflt-frontend-pre-1017451597.us-west-1.elb.amazonaws.com/"#pre地址
#base_url="http://affiliates.appflood.com/"#正式服地址
driver=webdriver.Chrome('C:\Program Files (x86)\Google\Chrome\Application\chromedriver')

username="l@l.com"
password="123456"

driver.get(base_url)
driver.find_element_by_xpath('//*[@id="panelBody"]/table/tbody/tr[1]/td[2]/input').send_keys(username)
driver.find_element_by_xpath('//*[@id="panelBody"]/table/tbody/tr[2]/td[2]/input').send_keys(password)
driver.find_element_by_xpath('//*[@id="panelBody"]/table/tbody/tr[3]/td[2]/button').click()#login
time.sleep(2)
cookie=driver.get_cookies()
print cookie[2]#只需要PPY_AFFSESSID这个cookie