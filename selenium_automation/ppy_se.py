# -*- coding: utf-8 -*-
# coding = utf-8
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
browser = webdriver.Chrome('C:\Program Files (x86)\Google\Chrome\Application\chromedriver')
browser.get("http://affiliate.appflood.com/")
#鼠标不要放在浏览器窗口里!
#鼠标不要放在浏览器窗口里!!
#鼠标不要放在浏览器窗口里!!!
browser.find_element_by_xpath('//*[@id="panelBody"]/table/tbody/tr[1]/td[2]/input').send_keys("adm_30@user.com")
browser.find_element_by_xpath('//*[@id="panelBody"]/table/tbody/tr[2]/td[2]/input').send_keys("741258")
browser.find_element_by_xpath('//*[@id="panelBody"]/table/tbody/tr[3]/td[2]/button').click()#login
time.sleep(3)
ActionChains(browser).move_to_element(browser.find_element_by_xpath('//*[@id="top"]/div/nav/ul/li[3]/a')).perform()

time.sleep(2)
browser.find_element_by_xpath('//*[@id="top"]/div/nav/ul/li[3]/ul/li[1]/a').click()
print browser.title
browser.find_element_by_xpath('//*[@id="group"]/div[1]/div[2]/div[1]/ul[2]/li[6]/label').click()#勾选sub6
browser.find_element_by_xpath('//*[@id="timeframe"]/div[2]/div/div[1]/select/option[2]').click()#时间选择last 6 month
#browser.find_element_by_xpath('//*[@id="timeframe"]/div[2]/div/div[1]/select').click()
browser.find_element_by_xpath('//*[@id="content"]/div/form/h2[2]/button').click()#run report
#browser.implicitly_wait(15)
time.sleep(15)
browser.find_element_by_xpath('//*[@id="content"]/div/div[2]/div[2]/div[2]/table/thead/tr/th[6]').click()
browser.implicitly_wait(15)
browser.find_element_by_xpath('//*[@id="content"]/div/div[2]/div[2]/div[1]/div[2]/ul/li[3]/a').click()
browser.implicitly_wait(15)
#js="var q=document.documentElement.scrollTop=10000"
js="$(window).scrollTop(10000)"
browser.execute_script(js)
#browser.quit()
js="alert('selenium complete')"
browser.execute_script(js)
