from selenium import webdriver

driver_path='/usr/local/bin/chromedriver'

driver=webdriver.Chrome(executable_path=driver_path)
driver.get('http://www.baidu.com')

print(driver.page_source)