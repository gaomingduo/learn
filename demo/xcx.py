import unittest
import traceback
from appium import webdriver
import time
import subprocess

from appium.webdriver.common.touch_action import TouchAction


class MyTestCase(unittest.TestCase):
    def setUp(self):
        print('定义初始化属性信息')
        # APP结构类型
        self.app_types = []
        # 定义初始化的属性信息
        self.desired_caps = {}
        self.desired_caps['platformName'] = 'Android'
        self.desired_caps['platformVersion'] = '10.0.0'
        self.desired_caps['deviceName'] = '5GK4C19B29005305'
        # self.desired_caps['udid'] = '69T7N16223005600'
        self.desired_caps['appPackage'] = 'com.tencent.mm'
        # self.desired_caps['appActivity'] = 'com.tencent.mm.plugin.appbrand.ui.AppBrandLauncherUI'
        self.desired_caps['appActivity'] = 'com.tencent.mm.ui.LauncherUI'
        self.desired_caps["unicodeKeyboard"] = "True"
        self.desired_caps["resetKeyboard"] = "True"
        self.desired_caps["noReset"] = "True"  # 不退出
        self.desired_caps["recreateChromeDriverSessions"] = "True"
        self.desired_caps["chromeOptions"] = {"androidProcess": "com.tencent.mm:toolsmp"}
        # self.desired_caps["browserName"]="Chrome"
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', self.desired_caps)
        self.driver.implicitly_wait(6)

    def test_111(self):
        print('开始测试')
        time.sleep(2)
        # Switch 切换当前的上下文
        print("当前页面类型%s" % self.driver.contexts)
        print(self.driver.get_window_size())
        # TouchAction().press(x=375, y=267).move_to(x=375, y=1016).release().perform()
        # self.driver.find_element_by_id('b6ee891d-cc38-4284-9f71-4648164ff329').click()
        # self.driver.find_element_by_id('screenshotContainer').click()
        time.sleep(15)
        # self.driver.find_element_by_xpath('//android.widget.FrameLayout[@content-desc="当前所在页面,小程序"]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.FrameLayout[2]/android.support.v7.widget.RecyclerView/android.widget.RelativeLayout[2]/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.TextView')

        print("当前页面类型%s" % self.driver.contexts)
    #
    #
    # def test_something(self):
    #     print('开始测试')
    #     time.sleep(2)
    #     # Switch 切换当前的上下文
    #     print("当前页面类型%s" % self.driver.contexts)
    #     print(self.driver.get_window_size())
    #     TouchAction().press(x=375, y=267).move_to(x=375, y=1016).release().perform()
    #     self.driver.find_element_by_id('358c0f38-8fcd-4c7d-954c-4538258852a5').click()
    #     # self.driver.find_element_by_id('com.syqy.wecash:id/tv_shop').click()
    #     time.sleep(25)
    #     try:
    #         print("当前页面类型%s" % self.driver.contexts)
    #         self.app_types = self.driver.contexts
    #         self.driver.switch_to.context('WEBVIEW_com.syqy.wecash')
    #         self.driver.find_element_by_xpath(
    #             ' //*[@id="app"]/div[1]/div[1]/div/div[1]/div[2]/div[4]/div/div/div[1]/div[1]/div/div[1]/img').click()
    #         time.sleep(10)
    #         '''
    #         页面出现切换时，先切换回NATIVE_APP，杀掉chromedriver进程，然后再切换回webview亲测可以
    #         功能：杀死进程名称中包含qemu的所有进程
    #         ps aux|grep qemu|awk '{print $2}'|xargs kill -9
    #
    #         '''
    #         self.driver.switch_to.context('NATIVE_APP')
    #         kill = "ps aux|grep chromedriver|awk '{print $2}'|xargs kill -9"
    #         subprocess.getoutput(kill)
    #         self.driver.switch_to.context('WEBVIEW_com.syqy.wecash')
    #         print(self.driver.page_source)
    #         self.driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[2]/div[1]/div[1]/img').click()
    #
    #         time.sleep(10)
    #
    #
    #
    #     except Exception as e:
    #         print(traceback.format_exc())
    #     # self.assertEqual(True, False)
    #
    # def tearDown(self):
    #     print('退出')
    #     try:
    #         self.driver.switch_to.context("NATIVE_APP")  # 切换回原生APP下
    #         self.driver.quit()
    #     except Exception as e:
    #         print(traceback.format_exc())
    #

if __name__ == '__main__':
    unittest.main()