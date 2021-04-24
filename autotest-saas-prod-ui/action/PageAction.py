# encoding=utf-8
# @time   :2020/5/9 12:18
# @Author :liulaing.song
# @Email  :1056703204@qq.com
# @File   :PageAction.py
# @explain:页面动作

from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from util.Log import Log
from util.KeyBoardUtil import KeyboardKeys
from util.WebTable import Table
from util.ReplaceValue import ReplaceValue
from selenium.webdriver.common.keys import Keys

# 定义全局变量
driver = None


class PageAction(object):

    def __init__(self):
        self.log = Log()
        self.key = KeyboardKeys()
        self.rv = ReplaceValue()

    def openBrowser(self, url):
        '''

        :param url: 输入的地址
        :return: 打开浏览器
        '''
        global driver
        try:
            # option = webdriver.ChromeOptions()
            # option.add_argument('--headless')
            # driver = webdriver.Chrome(chrome_options=option)
            driver = webdriver.Chrome()
            driver.maximize_window()
        except Exception as e:
            raise e
        try:
            driver.get(url)
            driver.implicitly_wait(10)
        except Exception as e:
            raise e

    def pageMotion(self, motion=None, locatorExpression=None, hoverLocator=None, value=None, table=None):
        '''

        :param motion: 动作指令
        :param locatorExpression: 操作元素定位表达式
        :param hoverLocator:悬浮点击位置定位表达式
        :param value:
        :return:
        '''
        global driver
        if motion == "click":

            locator = (By.XPATH, locatorExpression)
            try:
                WebDriverWait(driver, 30).until(EC.presence_of_all_elements_located(locator))
            except:
                self.log.info('未找到"' + locatorExpression + '"点击事件的定位元素')
            try:
                # 点击事件
                driver.find_element_by_xpath(locatorExpression).click()
                time.sleep(4)
            except:
                # print("未找到" + locatorExpression + "点击事件的元素")
                self.log.info('未找到"' + locatorExpression + '"点击事件的定位元素')

        elif motion == "click_bottom":
            locator = (By.XPATH, locatorExpression)
            try:
                WebDriverWait(driver, 30).until(EC.presence_of_all_elements_located(locator))
            except:
                self.log.info('未找到"' + locatorExpression + '"点击事件的定位元素')
            try:
                # 点击事件
                js = "var q=getElementByXPath(//div[@class='slider-bar']).scrollTop=0"
                driver.execute_script(js)
                time.sleep(2)
                driver.find_element_by_xpath(locatorExpression).click()
                time.sleep(4)
            except:
                # print("未找到" + locatorExpression + "点击事件的元素")
                self.log.info('未找到"' + locatorExpression + '"点击事件的定位元素')



        elif motion == "click_top":
            locator = (By.XPATH, locatorExpression)
            try:
                WebDriverWait(driver, 30).until(EC.presence_of_all_elements_located(locator))
            except:
                self.log.info('未找到"' + locatorExpression + '"点击事件的定位元素')

            try:
                # 点击事件
                js = "var q=getElementByXPath('//div[@class='slider-bar']').scrollTop=100000"
                driver.execute_script(js)
                time.sleep(2)
                driver.find_element_by_xpath(locatorExpression).click()
                time.sleep(4)
            except:
                # print("未找到" + locatorExpression + "点击事件的元素")
                self.log.info('未找到"' + locatorExpression + '"点击事件的定位元素')

        elif motion == "input":

            locator = (By.XPATH, locatorExpression)
            try:
                WebDriverWait(driver, 30).until(EC.presence_of_all_elements_located(locator))
            except:
                self.log.info('未找到"' + locatorExpression + '"点击事件的定位元素')

            try:
                # 清除输入框
                driver.find_element_by_xpath(locatorExpression).clear()
                # 输入值
                driver.find_element_by_xpath(locatorExpression).send_keys(value)
                time.sleep(2)
            except:
                # print("未找到" + locatorExpression + "输入事件的元素")
                self.log.info('未找到"' + locatorExpression + '"输入事件的定位元素')

        elif motion == "double_click":

            locator = (By.XPATH, locatorExpression)
            try:
                WebDriverWait(driver, 30).until(EC.presence_of_all_elements_located(locator))
            except:
                self.log.info('未找到"' + locatorExpression + '"点击事件的定位元素')

            try:
                double = driver.find_element_by_xpath(locatorExpression)
                ActionChains(driver).double_click(double).perform()
                time.sleep(4)
            except:
                # print("未找到" + locatorExpression + "双击事件的元素")
                self.log.info('未找到' + locatorExpression + '双击事件的定位元素')


        elif motion == "double_click_esc":

            locator = (By.XPATH, locatorExpression)
            try:
                WebDriverWait(driver, 30).until(EC.presence_of_all_elements_located(locator))
            except:
                self.log.info('未找到"' + locatorExpression + '"点击事件的定位元素')
            try:
                double = driver.find_element_by_xpath(locatorExpression)
                ActionChains(driver).double_click(double).perform()
                time.sleep(4)
                ActionChains(driver).send_keys(Keys.ESCAPE).perform()
                time.sleep(2)
            except:
                # print("未找到" + locatorExpression + "双击事件的元素")
                self.log.info('未找到' + locatorExpression + '双击事件的定位元素')

        elif motion == "hover":

            locator = (By.XPATH, locatorExpression)
            try:
                WebDriverWait(driver, 30).until(EC.presence_of_all_elements_located(locator))
            except:
                self.log.info('未找到"' + locatorExpression + '"点击事件的定位元素')

            try:
                ydong = driver.find_element_by_xpath(locatorExpression)
                ActionChains(driver).move_to_element(ydong).perform()
                time.sleep(2)
            except:
                self.log.info('未找到"' + locatorExpression + '"鼠标悬浮事件的定位元素')

            # try:
            #     driver.find_element_by_xpath(hoverLocator).click()
            #     time.sleep(3)
            # except:
            #     self.log.info('未找到"' + hoverLocator + '"鼠标悬浮后点击事件的定位元素')

        # elif motion == "enter":
        #     try:
        #         self.key.oneKey("enter")
        #         time.sleep(8)
        #     except Exception as e:
        #         self.log.info("模拟enter报错: %s" %e)

        elif motion == "enter":

            locator = (By.XPATH, locatorExpression)
            try:
                WebDriverWait(driver, 30).until(EC.presence_of_all_elements_located(locator))
            except:
                self.log.info('未找到"' + locatorExpression + '"点击事件的定位元素')

            try:
                driver.find_element_by_xpath(locatorExpression).send_keys(Keys.ENTER)
                time.sleep(5)
            except:
                self.log.info('未找到"' + locatorExpression + '"回车键事件的定位元素')

        elif motion == "esc":
            try:
                self.key.oneKey("esc")
                time.sleep(2)
            except Exception as e:
                self.log.info("模拟esc报错: %s" % e)

        elif motion == "top":
            try:
                js = "var q=document.getElementById('main-scroll').scrollTop = 0"
                driver.execute_script(js)
                time.sleep(2)
            except Exception as e:
                self.log.info("页面置顶报错: %s" % e)

            # try:
            #     driver.find_element_by_xpath(locatorExpression).click()
            #     time.sleep(3)
            # except:
            #     self.log.info('未找到"' + locatorExpression + '"置顶后点击事件的定位元素')
        elif motion == "click_esc":

            locator = (By.XPATH, locatorExpression)
            try:
                WebDriverWait(driver, 30).until(EC.presence_of_all_elements_located(locator))
            except:
                self.log.info('未找到"' + locatorExpression + '"点击事件的定位元素')

            try:
                # 点击事件
                driver.find_element_by_xpath(locatorExpression).click()
                time.sleep(9)
                ActionChains(driver).send_keys(Keys.ESCAPE).perform()
                time.sleep(2)
            except:
                # print("未找到" + locatorExpression + "点击事件的元素")
                self.log.info('未找到"' + locatorExpression + '"点击事件的定位元素')

            # try:
            #     self.key.oneKey("esc")
            #     time.sleep(2)
            # except Exception as e:
            #     self.log.info("模拟esc报错: %s" %e)

        elif motion == "quit":

            try:
                driver.quit()
            except Exception as e:
                self.log.info("退出浏览器失败: %s" % e)

        elif motion == "text":

            locator = (By.XPATH, locatorExpression)
            try:
                WebDriverWait(driver, 30).until(EC.presence_of_all_elements_located(locator))
            except:
                self.log.info('未找到"' + locatorExpression + '"点击事件的定位元素')

            try:
                text = driver.find_element_by_xpath(locatorExpression).text
                time.sleep(2)
                # print(text)
                return text
            except:
                self.log.info('未找到"' + locatorExpression + '"定位的元素文本信息')
                # driver.quit()

        elif motion == "attribute":

            locator = (By.XPATH, locatorExpression)
            try:
                WebDriverWait(driver, 30).until(EC.presence_of_all_elements_located(locator))
            except:
                self.log.info('未找到"' + locatorExpression + '"点击事件的定位元素')

            try:
                text = driver.find_element_by_xpath(locatorExpression).get_attribute('value')
                time.sleep(2)
                # print(text)
                return text
            except:
                self.log.info('未找到"' + locatorExpression + '"定位的元素文本信息')

        elif motion == "table_cell":

            locator = (By.XPATH, locatorExpression)
            try:
                WebDriverWait(driver, 30).until(EC.presence_of_all_elements_located(locator))
            except:
                self.log.info('未找到"' + locatorExpression + '"点击事件的定位元素')

            try:
                webTable = driver.find_element_by_xpath(locatorExpression)
                # listData = webTable.text
                tableMessage = Table(webTable)
                text = tableMessage.getCell(0, 5).text
                workNo = tableMessage.getCell(0, 4).text
                self.rv.keepValue(workNo)
                time.sleep(2)
                return text
            except:
                self.log.info('未找到"' + locatorExpression + '"定位的元素table表格信息')

        elif motion == "click_role":

            locator = (By.XPATH, locatorExpression)
            try:
                WebDriverWait(driver, 30).until(EC.presence_of_all_elements_located(locator))
            except:
                self.log.info('未找到"' + locatorExpression + '"点击事件的定位元素')

            try:
                # 点击事件
                driver.find_element_by_xpath(locatorExpression).click()
                time.sleep(5)
            except:
                # print("未找到" + locatorExpression + "点击事件的元素")
                self.log.info('未找到"' + locatorExpression + '"点击事件的定位元素')

        elif motion == "click_sleep":

            locator = (By.XPATH, locatorExpression)
            try:
                WebDriverWait(driver, 30).until(EC.presence_of_all_elements_located(locator))
            except:
                self.log.info('未找到"' + locatorExpression + '"点击事件的定位元素')

            try:
                # 点击事件
                driver.find_element_by_xpath(locatorExpression).click()
                time.sleep(10)
            except:
                # print("未找到" + locatorExpression + "点击事件的元素")
                self.log.info('未找到"' + locatorExpression + '"点击事件的定位元素')

        elif motion == "click_await":

            locator = (By.XPATH, locatorExpression)
            try:
                WebDriverWait(driver, 30).until(EC.presence_of_all_elements_located(locator))
            except:
                self.log.info('未找到"' + locatorExpression + '"点击事件的定位元素')

            try:
                text = driver.find_element_by_xpath(locatorExpression).text
                if "等待汇总" not in text:
                    while True:
                        driver.refresh()
                        time.sleep(10)
                        text = driver.find_element_by_xpath(locatorExpression).text
                        if "等待汇总" in text:
                            locator = (By.XPATH, "//i[@class='icon ikcon ikcon-iconfont iconpick-up']")
                            WebDriverWait(driver, 15).until(EC.presence_of_all_elements_located(locator))
                            driver.find_element_by_xpath("//i[@class='icon ikcon ikcon-iconfont iconpick-up']").click()
                            time.sleep(3)
                            locator = (By.XPATH, "//i[@class='icon ikcon ikcon-iconfont iconexpand']")
                            WebDriverWait(driver, 15).until(EC.presence_of_all_elements_located(locator))
                            driver.find_element_by_xpath("//i[@class='icon ikcon ikcon-iconfont iconexpand']").click()
                            time.sleep(3)
                            break
            except:
                self.log.info('未找到"' + locatorExpression + '"定位的元素文本信息')





        else:
            driver.quit()
            self.log.info("请检查excel'动作'列是否书写正确")


if __name__ == "__main__":
    pa = PageAction()
    pa.openBrowser("http://uat.tijian.ikang.com")
    pa.pageMotion(motion="input", locatorExpression="//input[@placeholder='请输入账号']", value="liuliangsong")
    pa.pageMotion(motion="input", locatorExpression="//input[@placeholder='请输入密码']", value="123456")
    pa.pageMotion(motion="click", locatorExpression="//button[@type='button']")
    pa.pageMotion(motion="quit")
