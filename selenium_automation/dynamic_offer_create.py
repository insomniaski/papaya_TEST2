# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Chrome('C:\Program Files (x86)\Google\Chrome\Application\chromedriver')
driver.get("http://54.67.94.143:9091/")
driver.find_element_by_xpath('//*[@id="panelBody"]/table/tbody/tr[1]/td[2]/input').send_keys("l@l.com")
driver.find_element_by_xpath('//*[@id="panelBody"]/table/tbody/tr[2]/td[2]/input').send_keys("123456")
driver.find_element_by_xpath('//*[@id="panelBody"]/table/tbody/tr[3]/td[2]/button').click()#login
time.sleep(2)
ActionChains(driver).move_to_element(driver.find_element_by_xpath("//a[contains(.,'Offers')]")).perform()
time.sleep(1)
driver.find_element_by_xpath("//a[@href='/admin/offer/create_dynamic']").click()
print driver.title
time.sleep(1)
driver.find_element_by_xpath("//select[@data-bind=' value:data.advertiser_id']").click()
driver.find_element_by_xpath("//option[@value='134']").click()#广告主id视情况
current_time=time.strftime('%Y%m%d_%H%M%S',time.localtime(time.time()))
driver.find_element_by_xpath("//input[@data-bind='value:data.name']").send_keys('_dynamic_test_mainoffer '+current_time)
driver.find_element_by_xpath("//select[@data-bind=' value:data.offer_group_id']").click()
driver.find_element_by_xpath("//option[@value='38']").click()#group id视情况
driver.find_element_by_xpath("//select[@data-bind='value: data.status']").click()
driver.find_element_by_xpath("//option[contains(.,'Active')]").click()
driver.find_element_by_xpath("//option[@value='60']").click()#category id视情况
driver.find_element_by_xpath('//*[@id="offer_create_form"]/h4[4]/span').click()
time.sleep(1)
driver.find_element_by_xpath("//select[@name='require_approval']").click()
driver.find_element_by_xpath('//*[@id="settings_group"]/li[2]/select/option[2]').click()
driver.find_element_by_xpath("//button[@type='submit']").click()
