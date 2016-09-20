# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

browser = webdriver.Chrome('C:\Program Files (x86)\Google\Chrome\Application\chromedriver')
browser.get("http://192.168.41.130:3212/")
#鼠标不要放在浏览器窗口里!
#鼠标不要放在浏览器窗口里!!
#鼠标不要放在浏览器窗口里!!!
browser.find_element_by_xpath('//*[@id="panelBody"]/table/tbody/tr[1]/td[2]/input').send_keys("l@l.com")
browser.find_element_by_xpath('//*[@id="panelBody"]/table/tbody/tr[2]/td[2]/input').send_keys("123456")
browser.find_element_by_xpath('//*[@id="panelBody"]/table/tbody/tr[3]/td[2]/button').click()#login
time.sleep(5)
ActionChains(browser).move_to_element(browser.find_element_by_xpath('//*[@id="top"]/div/nav/ul/li[2]/a')).perform()
time.sleep(2)
browser.find_element_by_xpath('//*[@id="top"]/div/nav/ul/li[2]/ul/li[5]/a').click()
print browser.title
browser.find_element_by_id('file_upload').click()
time.sleep(7)
browser.find_element_by_xpath('//*[@id="btn"]').click()
browser.switch_to_alert().accept()
# js="$('file_upload').show()"
# browser.execute_script(js)
# browser.find_element_by_id('file_upload').send_keys(r"C:\Users\20160725\Desktop\batch_offer.xlsx")






