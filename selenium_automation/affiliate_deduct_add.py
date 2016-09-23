# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
import random
#driver=webdriver.Android()
driver = webdriver.Chrome('C:\Program Files (x86)\Google\Chrome\Application\chromedriver')
#driver.get("http://192.168.41.130:3211/")
driver.get("http://aflt-frontend-pre-1017451597.us-west-1.elb.amazonaws.com")
#鼠标不要放在浏览器窗口里!
driver.find_element_by_xpath('//*[@id="panelBody"]/table/tbody/tr[1]/td[2]/input').send_keys("l@l.com")
driver.find_element_by_xpath('//*[@id="panelBody"]/table/tbody/tr[2]/td[2]/input').send_keys("123456")
driver.find_element_by_xpath('//*[@id="panelBody"]/table/tbody/tr[3]/td[2]/button').click()#login
time.sleep(3)
driver.get("http://aflt-frontend-pre-1017451597.us-west-1.elb.amazonaws.com/admin/offer/deduct/112544")
for k in range(0,30):
    driver.find_element_by_xpath("//a[contains(.,'Add')]").click()
    driver.find_element_by_xpath("//select[@class='input-sm ma-rg']").click()
    driver.implicitly_wait(1)
    driver.find_element_by_xpath('//*[@id="content"]/div/form/ul/li[2]/select/option['+str(k+3)+']').click()
    driver.find_element_by_xpath("//input[@type='text']").send_keys(random.randint(2,10))
    driver.find_element_by_xpath("//button[@type='submit']").click()
    time.sleep(1)
    alert = driver.switch_to.alert
    alert.accept()
    driver.implicitly_wait(2)