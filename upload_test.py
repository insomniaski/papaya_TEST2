# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

browser = webdriver.Chrome('C:\Program Files (x86)\Google\Chrome\Application\chromedriver')
#browser = webdriver.Firefox()
browser.get("http://192.168.41.130:3212/")
#鼠标不要放在浏览器窗口里!
#鼠标不要放在浏览器窗口里!!
#鼠标不要放在浏览器窗口里!!!
browser.find_element_by_xpath('//*[@id="panelBody"]/table/tbody/tr[1]/td[2]/input').send_keys("l@l.com")
browser.find_element_by_xpath('//*[@id="panelBody"]/table/tbody/tr[2]/td[2]/input').send_keys("123456")
browser.find_element_by_xpath('//*[@id="panelBody"]/table/tbody/tr[3]/td[2]/button').click()#login
time.sleep(2)
browser.get("http://192.168.41.130:3212/admin/offer/upload_icon/82080")
print browser.title
browser.find_element_by_xpath('//*[@id="file-upload"]/input').send_keys(r"C:\Users\20160725\Pictures\icons\174px-Secret_logo.png")
browser.find_element_by_xpath('//*[@id="OfferUploadIcon"]/button').click()



