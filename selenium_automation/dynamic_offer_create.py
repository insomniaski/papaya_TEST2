# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import time
#driver = webdriver.Chrome('C:\Program Files (x86)\Google\Chrome\Application\chromedriver')
driver=webdriver.Firefox()
driver.get("http://aflt-frontend-pre-1017451597.us-west-1.elb.amazonaws.com/")
driver.find_element_by_xpath('//*[@id="panelBody"]/table/tbody/tr[1]/td[2]/input').send_keys("l@l.com")
driver.find_element_by_xpath('//*[@id="panelBody"]/table/tbody/tr[2]/td[2]/input').send_keys("123456")
driver.find_element_by_xpath('//*[@id="panelBody"]/table/tbody/tr[3]/td[2]/button').click()#login
time.sleep(2)
ActionChains(driver).move_to_element(driver.find_element_by_xpath("//a[contains(.,'Offers')]")).perform()
time.sleep(1)
driver.find_element_by_xpath("//a[@href='/admin/offer/create_dynamic']").click()
print driver.title
time.sleep(1)
# driver.find_element_by_xpath("//select[@data-bind=' value:data.advertiser_id']").click()
# driver.find_element_by_xpath("//option[@value='134']").click()#广告主id视情况
current_time=time.strftime('%Y%m%d_%H%M%S',time.localtime(time.time()))
driver.find_element_by_xpath("//input[@data-bind='value:data.name']").send_keys('_dynamic_test_mainoffer '+current_time)
driver.find_element_by_xpath("//select[@data-bind=' value:data.offer_group_id']").click()
driver.find_element_by_xpath("//option[@value='35']").click()#group id视情况
driver.find_element_by_xpath("//select[@data-bind='value: data.status']").click()
driver.find_element_by_xpath("//option[contains(.,'Active')]").click()
driver.find_element_by_xpath("//option[@value='65']").click()#category id视情况
driver.find_element_by_xpath('//*[@id="offer_create_form"]/h4[4]/span').click()#展开settings
time.sleep(1)
Select(driver.find_element_by_name("private")).select_by_visible_text("Enabled")
Select(driver.find_element_by_name("require_approval")).select_by_visible_text("Disabled")
driver.find_element_by_css_selector("div.col-sm-offset-2.clearfix > input.form-control.input-sm").clear()
driver.find_element_by_css_selector("div.col-sm-offset-2.clearfix > input.form-control.input-sm").send_keys("5")
Select(driver.find_element_by_name("terms_and_conditions")).select_by_visible_text("Enabled")
driver.find_element_by_xpath("//ul[@id='settings_group']/li[5]/textarea").clear()
driver.find_element_by_xpath("//ul[@id='settings_group']/li[5]/textarea").send_keys("aaaaa")
Select(driver.find_element_by_xpath("//ul[@id='settings_group']/li[6]/div/select")).select_by_visible_text("UTC -05:00")
driver.find_element_by_xpath("(//input[@type='text'])[3]").clear()
driver.find_element_by_xpath("(//input[@type='text'])[3]").send_keys("4")
Select(driver.find_element_by_name("email_instructions")).select_by_visible_text("Enabled")
driver.find_element_by_xpath("//ul[@id='settings_group']/li[10]/textarea").clear()
driver.find_element_by_xpath("//ul[@id='settings_group']/li[10]/textarea").send_keys("1111111")
driver.find_element_by_xpath("//ul[@id='settings_group']/li[11]/textarea").clear()
driver.find_element_by_xpath("//ul[@id='settings_group']/li[11]/textarea").send_keys("22222222222")
driver.find_element_by_xpath("//form[@id='offer_create_form']/h4[5]/span").click()
Select(driver.find_element_by_name("click_session_lifespan")).select_by_visible_text("2 Weeks")
driver.find_element_by_xpath("//button[contains(.,'Add Offer and Define Targeting')]").click()
