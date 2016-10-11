# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
#driver=webdriver.Android()
driver = webdriver.Chrome('C:\Program Files (x86)\Google\Chrome\Application\chromedriver')
#driver.get("http://192.168.41.130:3211/")
driver.get("http://54.67.94.143:9091")
#鼠标不要放在浏览器窗口里!
driver.find_element_by_xpath('//*[@id="panelBody"]/table/tbody/tr[1]/td[2]/input').send_keys("l@l.com")
driver.find_element_by_xpath('//*[@id="panelBody"]/table/tbody/tr[2]/td[2]/input').send_keys("123456")
driver.find_element_by_xpath('//*[@id="panelBody"]/table/tbody/tr[3]/td[2]/button').click()#login
time.sleep(2)
for cookie in driver.get_cookies():
    print "%s -> %s" % (cookie['name'], cookie['value'])
ActionChains(driver).move_to_element(driver.find_element_by_xpath('//*[@id="top"]/div/nav/ul/li[4]/a')).perform()
time.sleep(2)
driver.find_element_by_xpath('//*[@id="top"]/div/nav/ul/li[4]/ul/li[2]/a').click()
print driver.title

current_time=time.strftime('%Y%m%d_%H%M%S',time.localtime(time.time()))
driver.find_element_by_xpath("//input[@id='company']").send_keys("selenium_create_aff_"+current_time)
driver.find_element_by_xpath("//input[@id='first_name']").send_keys(current_time)
driver.find_element_by_xpath("//input[@id='last_name']").send_keys("Alberich Wang")
driver.find_element_by_xpath("//input[@id='email']").send_keys(current_time+"wyq@papaya.com")
driver.find_element_by_xpath("//input[@id='password']").send_keys("123456")
driver.find_element_by_xpath("//input[@id='confirm_pwd']").send_keys("123456")
driver.find_element_by_xpath("//button[@type='submit']").click()
time.sleep(5)
alert=driver.switch_to.alert
alert.accept()
driver.implicitly_wait(10)
driver.find_element_by_xpath("//input[@placeholder='Search']").send_keys("selenium")
driver.find_element_by_xpath("//button[@name='search']").click()
driver.maximize_window()


