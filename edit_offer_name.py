# -*- coding: utf-8 -*-
import os
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
#profile_dir=r"C:\Users\20160725\AppData\Local\Google\Chrome\User Data"    # 对应你的chrome的用户数据存放路径

#chrome_optionss=webdriver.ChromeOptions()
#chrome_optionss.add_argument("user-data-dir="+os.path.abspath(profile_dir))
browser = webdriver.Chrome('C:\Program Files (x86)\Google\Chrome\Application\chromedriver')
#browser = webdriver.Chrome(chrome_options=chrome_options)
# browser.maximize_window()
print 1
browser.get("http://aflt-frontend-pre-1017451597.us-west-1.elb.amazonaws.com/admin/offer/view/19/")
#鼠标不要放在浏览器窗口里!
#鼠标不要放在浏览器窗口里!!
#鼠标不要放在浏览器窗口里!!!
browser.find_element_by_xpath('//*[@id="panelBody"]/table/tbody/tr[1]/td[2]/input').send_keys("wangyiqian@papayamobile.cn")
browser.find_element_by_xpath('//*[@id="panelBody"]/table/tbody/tr[2]/td[2]/input').send_keys("123456")
browser.find_element_by_xpath('//*[@id="panelBody"]/table/tbody/tr[3]/td[2]/button').click()#login
time.sleep(3)
browser.get("http://aflt-frontend-pre-1017451597.us-west-1.elb.amazonaws.com/admin/offer/view/19/")
browser.find_element_by_xpath('//*[@id="content"]/div/div/div[1]/div[1]/div[1]/span[2]/a[1]').click()
time.sleep(3)
browser.find_element_by_xpath('//*[@id="offer_create_form"]/ul/li[2]/input').clear()
browser.find_element_by_xpath('//*[@id="offer_create_form"]/ul/li[2]/input').send_keys("offer_19")
browser.find_element_by_xpath('//*[@id="offer_create_form"]/button').click()
browser.switch_to().alert().accept()
