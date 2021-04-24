# encoding=utf-8
# @time   :2020/5/9 11:40
# @Author :liulaing.song
# @Email  :1056703204@qq.com
# @File   :login.py
# @explain:登录方法

from action.PageAction import PageAction
from util.ParseConfig import ParseConfig
from util.Log import Log


class Login(object):

    # 构造函数
    def __init__(self):
        self.pa = PageAction()
        self.pc = ParseConfig()
        self.log = Log()

    # 登录方法
    def loginMethod(self):
        # 打开浏览器
        self.pa.openBrowser(self.pc.getValue("addres", "url"))
        self.log.info("打开浏览器")
        # 输入用户名
        self.pa.pageMotion(motion="input", locatorExpression="//input[@placeholder='请输入账号']",
                           value=self.pc.getValue("login", "username"))
        self.log.info("输入用户名")
        # 输入密码
        self.pa.pageMotion(motion="input", locatorExpression="//input[@placeholder='请输入密码']",
                           value=self.pc.getValue("login", "password"))
        self.log.info("输入密码")
        # 点击登录
        self.pa.pageMotion(motion="click", locatorExpression="//button[@type='button']")
        self.log.info("点击登录")


if __name__ == "__main__":
    l = Login()
    l.loginMethod()
