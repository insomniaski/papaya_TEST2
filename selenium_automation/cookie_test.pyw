# -*- coding: utf-8 -*-
from selenium import webdriver
import time
import os

#profile_dir = r"C:\Users\20160725\AppData\Local\Google\Chrome\User Data"  # 对应你的chrome的用户数据存放路径
#chrome_options = webdriver.ChromeOptions()
#chrome_options.add_argument("user-data-dir=" + os.path.abspath(profile_dir))
url="http://54.67.94.143:9091"
#url="http://aflt-frontend-pre-1017451597.us-west-1.elb.amazonaws.com/"
browser = webdriver.Chrome('C:\Program Files (x86)\Google\Chrome\Application\chromedriver')
#browser = webdriver.Firefox()
browser.maximize_window()
browser.get(url)
# browser.find_element_by_xpath('//*[@id="panelBody"]/table/tbody/tr[1]/td[2]/input').send_keys("l@l.com")
# browser.find_element_by_xpath('//*[@id="panelBody"]/table/tbody/tr[2]/td[2]/input').send_keys("123456")
# browser.find_element_by_xpath('//*[@id="panelBody"]/table/tbody/tr[3]/td[2]/button').click()#login
# time.sleep(3)
# cookie=browser.get_cookies()
# print cookie
browser.delete_all_cookies()#一定要先delete原来的cookie，否则没用
browser.add_cookie({u'domain': u'54.67.94.143', u'secure': False, u'value': u's%3ARiqnPN5iE0EEK3opP3O2R8Mm.tEZM3RPGVyhWJPZMPGJq9%2Ft5V8vH1Nj7ZnJ7Ms4r%2Bto', u'expiry': 1476760084.068569, u'path': u'/', u'httpOnly': True, u'name': u'PPY_AFFSESSID1'})
#  'value':'s%3ARiqnPN5iE0EEK3opP3O2R8Mm.tEZM3RPGVyhWJPZMPGJq9%2Ft5V8vH1Nj7ZnJ7Ms4r%2Bto',
#  'path' : '/'})
browser.get(url+"/admin/snapshot")
browser.close()
#browser.refresh()
#browser.get("http://54.67.94.143:9091")
