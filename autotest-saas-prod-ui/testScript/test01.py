# encoding=utf-8
# @time   :2020/5/26 12:20
# @Author :liulaing.song
# @Email  :1056703204@qq.com
# @File   :test01.py
# @explain:
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://tijian.ikang.com")
driver.implicitly_wait(10)
driver.find_element_by_xpath("//input[@placeholder='请输入账号']").send_keys("zdtest1")
sleep(2)
driver.find_element_by_xpath("//input[@placeholder='请输入密码']").send_keys("123456")
sleep(2)
driver.find_element_by_xpath("//button[@type='button']").click()
sleep(6)
driver.find_element_by_xpath("//button[@type='button']").click()
sleep(6)
driver.find_element_by_xpath("//i[@class='icon ikcon ikcon-iconfont iconpick-up']").click()
sleep(2)
driver.find_element_by_xpath("//i[@class='icon ikcon ikcon-iconfont iconexpand']").click()
sleep(2)
driver.find_element_by_xpath("//div[@class='el-submenu__title']//span[contains(text(),'报告管理')]").click()
sleep(2)
driver.find_element_by_xpath("//div[contains(text(),'打印管理')]").click()
sleep(2)
driver.find_element_by_xpath("//li[contains(text(),'打印列表')]").click()
sleep(5)
driver.find_element_by_xpath("//input[@placeholder='请输入体检号']").send_keys("5052005260016")
sleep(2)
driver.find_element_by_xpath("//button[@class='el-button el-button--primary el-button--medium']").click()
sleep(3)
double = driver.find_element_by_xpath("//body//td[6]")
ActionChains(driver).double_click(double).perform()
sleep(5)
ActionChains(driver).send_keys(Keys.ESCAPE).perform()
sleep(10)
driver.quit()
