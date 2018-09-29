from selenium import webdriver
import time

driver=webdriver.Chrome()
driver.get("https://kyfw.12306.cn/otn/index/initn")
time.sleep(100)
driver.find_element_by_xpath('//tr[@class="bgc"][1]/td[@align="center"]/a').click()
driver.find_element_by_xpath("//ul[@id='normal_passenger_id']/li[1]/input").click()

#处理学生票
driver.find_element_by_xpath('//*[@id="qd_closeDefaultWarningWindowDialog_id"]').click()
#//*[@id="qd_closeDefaultWarningWindowDialog_id"]
#//div[@class="up-box w600"]/div[2]/div[2]/a

#点击提交
driver.find_element_by_xpath('//a[@id="submitOrder_id"]').click()

#最后确认
driver.find_element_by_xpath('//a[@id="qr_submit_id"]').click()

#抢票成功处理

if driver.find_element_by_xpath('//a[@id="payButton"]/text').text=="网上支付":
    print("抢票成功")

