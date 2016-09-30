# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
browser = webdriver.Chrome('C:\Program Files (x86)\Google\Chrome\Application\chromedriver')
#browser.get("http://192.168.41.130:3211/")
browser.get("http://54.67.94.143:9091/")
#browser.get("http://aflt-frontend-pre-1017451597.us-west-1.elb.amazonaws.com")
#鼠标不要放在浏览器窗口里!
#鼠标不要放在浏览器窗口里!!
#鼠标不要放在浏览器窗口里!!!
browser.find_element_by_xpath('//*[@id="panelBody"]/table/tbody/tr[1]/td[2]/input').send_keys("l@l.com")
browser.find_element_by_xpath('//*[@id="panelBody"]/table/tbody/tr[2]/td[2]/input').send_keys("123456")
browser.find_element_by_xpath('//*[@id="panelBody"]/table/tbody/tr[3]/td[2]/button').click()#login
time.sleep(2)
def unit_create(i):
    ActionChains(browser).move_to_element(browser.find_element_by_xpath('//*[@id="top"]/div/nav/ul/li[2]/a')).perform()
    time.sleep(1)
    browser.find_element_by_xpath('//*[@id="top"]/div/nav/ul/li[2]/ul/li[2]/a').click()
    print browser.title
    js="$(window).scrollTop(10000)"
    browser.execute_script(js)#下拉页面
    time.sleep(1)
    browser.find_element_by_xpath('//*[@id="offer_create_form"]/h4[2]/span').click()#点击revenue
    time.sleep(1)
    browser.find_element_by_xpath('//*[@id="offer_create_form"]/h4[3]/span').click()#点击payout
    time.sleep(1)
    browser.find_element_by_xpath('//*[@id="offer_create_form"]/h4[4]/span').click()#点击settings
    browser.find_element_by_xpath('//*[@id="details_group"]/li[1]/select').click()
    browser.find_element_by_xpath('//*[@id="details_group"]/li[1]/select/option[7]').click()#选择advertiser
    browser.find_element_by_xpath('//*[@id="details_group"]/li[2]/input').send_keys('_selenium create dynamic offer5_'+str(i))#offer name
    browser.find_element_by_xpath('//*[@id="details_group"]/li[3]/textarea').send_keys('test description')#description
    browser.find_element_by_xpath('//*[@id="details_group"]/li[4]/div/input').send_keys('www.baidu.com')#preview url
    browser.find_element_by_xpath('//*[@id="details_group"]/li[5]/div/input').send_keys('www.xiami4.com/transaction_id={transaction_id}')#click url
    browser.find_element_by_xpath("//select[@data-bind='value: data.status']").click()
    browser.find_element_by_xpath("//option[contains(.,'Active')]").click()#选择状态
    browser.find_element_by_xpath('//*[@id="revenue_group"]/li[3]/div/div[1]/input[1]').send_keys('.2')#输入价格
    browser.find_element_by_xpath('//*[@id="payout_group"]/li[3]/div/input').send_keys('.1')#输入价格
    browser.find_element_by_xpath('//*[@id="settings_group"]/li[2]/select').click()
    browser.find_element_by_xpath('//*[@id="settings_group"]/li[2]/select/option[2]').click()#require approval关闭
    browser.find_element_by_xpath("//button[@type='submit']").click()#add offer and define targeting
    time.sleep(5)
    alert=browser.switch_to.alert
    alert.accept()
    print browser.current_url
    browser.maximize_window()
    #browser.execute_script("alert('selenium complete')")
for i in range(30):
    unit_create(i)
