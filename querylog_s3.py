from selenium import webdriver

driver = webdriver.PhantomJS(r"E:\phantomjs-2.1.1-windows\bin\phantomjs.exe")
driver.get("http://duckduckgo.com/")
driver.find_element_by_id('search_form_input_homepage').send_keys("Nirvana")
driver.find_element_by_id("search_button_homepage").click()
print driver.current_url
driver.u
driver.quit()
