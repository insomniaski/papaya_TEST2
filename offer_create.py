# -*- coding: utf-8 -*-
import os
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
browser = webdriver.Chrome('C:\Program Files (x86)\Google\Chrome\Application\chromedriver')
browser.get("http://aflt-frontend-pre-1017451597.us-west-1.elb.amazonaws.com/admin/offer/view/19/")
#鼠标不要放在浏览器窗口里!
#鼠标不要放在浏览器窗口里!!
#鼠标不要放在浏览器窗口里!!!
browser.find_element_by_xpath('//*[@id="panelBody"]/table/tbody/tr[1]/td[2]/input').send_keys("l@l.com")
browser.find_element_by_xpath('//*[@id="panelBody"]/table/tbody/tr[2]/td[2]/input').send_keys("123456")
browser.find_element_by_xpath('//*[@id="panelBody"]/table/tbody/tr[3]/td[2]/button').click()#login
time.sleep(5)
ActionChains(browser).move_to_element(browser.find_element_by_xpath('//*[@id="top"]/div/nav/ul/li[2]/a')).perform()
time.sleep(2)
browser.find_element_by_xpath('//*[@id="top"]/div/nav/ul/li[2]/ul/li[2]/a').click()
print browser.title
js="$(window).scrollTop(10000)"
browser.execute_script(js)#下拉页面
time.sleep(1)
browser.find_element_by_xpath('//*[@id="offer_create_form"]/h4[2]/span').click()#点击revenue
time.sleep(1)
browser.find_element_by_xpath('//*[@id="offer_create_form"]/h4[3]/span').click()#点击payout
browser.find_element_by_xpath('//*[@id="details_group"]/li[1]/select').click()
browser.find_element_by_xpath('//*[@id="details_group"]/li[1]/select/option[6]').click()#选择advertiser
browser.find_element_by_xpath('//*[@id="details_group"]/li[2]/input').send_keys('selenium create offer')#offer name
browser.find_element_by_xpath('//*[@id="details_group"]/li[3]/textarea').send_keys('test description')#description
browser.find_element_by_xpath('//*[@id="details_group"]/li[4]/div/input').send_keys('www.baidu.com')#preview url
browser.find_element_by_xpath('//*[@id="details_group"]/li[5]/div/input').send_keys('www.xiami.com/transaction_id={transaction_id}')#click url
browser.find_element_by_xpath('//*[@id="revenue_group"]/li[3]/div/div[1]/input[1]').send_keys('.1')#输入价格
browser.find_element_by_xpath('//*[@id="payout_group"]/li[3]/div/input').send_keys('.2')#输入价格

browser.find_element_by_xpath('//*[@id="offer_create_form"]/button[2]').click()#add offer and define targeting
time.sleep(10)
alert=browser.switch_to.alert
alert.accept()
print browser.current_url
browser.find_element_by_xpath('//*[@id="content"]/div/button').click()
browser.maximize_window()
offer_id=browser.find_element_by_xpath('//*[@id="panel_body_details"]/div/div[1]/p[1]').text#获取offer_id
browser.find_element_by_xpath('//*[@id="content"]/div/div/div[1]/div[1]/div[1]/span[2]/a[1]').click()#点击edit
time.sleep(3)
#browser.find_element_by_xpath('//*[@id="offer_create_form"]/ul/li[2]/input').clear()
browser.find_element_by_xpath('//*[@id="offer_create_form"]/ul/li[2]/input').send_keys(offer_id[4:])#修改offer name
browser.find_element_by_xpath('//*[@id="offer_create_form"]/button').click()
time.sleep(5)
alert=browser.switch_to.alert
alert.accept()
time.sleep(3)
browser.execute_script("alert('selenium complete')")