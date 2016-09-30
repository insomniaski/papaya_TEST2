# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Chrome('C:\Program Files (x86)\Google\Chrome\Application\chromedriver')
#browser.get("http://192.168.41.130:3211/")
driver.get("http://54.67.94.143:9091/")
driver.find_element_by_xpath('//*[@id="panelBody"]/table/tbody/tr[1]/td[2]/input').send_keys("l@l.com")
driver.find_element_by_xpath('//*[@id="panelBody"]/table/tbody/tr[2]/td[2]/input').send_keys("123456")
driver.find_element_by_xpath('//*[@id="panelBody"]/table/tbody/tr[3]/td[2]/button').click()#login
time.sleep(3)
driver.get("http://54.67.94.143:9091/admin/offer/offer_groups/view/38")

def add_offer_to_group(offer_id):
    driver.find_element_by_xpath("//a[contains(.,'ADD OFFER')]").click()
    time.sleep(1)
    driver.find_element_by_xpath("//select[@data-bind='value: data.offer_id']").click()
    x_path="//option[@value='"+str(offer_id)+"']"
    driver.find_element_by_xpath(x_path).click()
    driver.find_element_by_xpath("//button[@class='btn btn-primary']").click()
    time.sleep(2)
    alert = driver.switch_to.alert
    alert.accept()

for i in range(85572,85581):
    add_offer_to_group(i)



