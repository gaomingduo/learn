# encoding=utf-8
# @time   :2020/5/9 15:43
# @Author :liulaing.song
# @Email  :1056703204@qq.com
# @File   :SelectTheSorting.py
# @explain:选择分院

from util.login import Login
from action.PageAction import PageAction
from util.ParseJson import ParseJson
# from wsgiref.simple_server import make_server
from util.Log import Log


class SelectTheSorting(object):

    # 构造函数
    def __init__(self):
        self.login = Login()
        self.pa = PageAction()
        self.pj = ParseJson()
        self.log = Log()

    def selectSort(self, area, branch):
        # 登录
        self.login.loginMethod()
        # 选择区域
        # if area == "北京区域":
        # 选择区域
        self.pa.pageMotion(motion='click', locatorExpression="//input[@placeholder='请选择二级组织']")

        self.pa.pageMotion(motion='click', locatorExpression="//span[contains(text()," + "'" + area + "' " + ")]")
        self.log.info("选择" + area)
        if branch != None:
            self.pa.pageMotion(motion='click', locatorExpression="//input[@placeholder='请选择三级组织']")
            self.pa.pageMotion(motion='click', locatorExpression="//span[contains(text()," + "'" + branch + "' " + ")]")
            self.log.info("选择" + branch)
        else:
            pass
        # print("//span[contains(text(),"+"'"+area+"' " +")]")
        # 选择角色
        self.pa.pageMotion(motion='click', locatorExpression="//input[@placeholder='请选择角色']")
        self.pa.pageMotion(motion='click', locatorExpression="//span[contains(text(), '分院IT')]")
        self.log.info("选择分院IT角色")
        self.pa.pageMotion(motion='click_sleep', locatorExpression="//button[@type='button']")
        self.log.info("点击进入")

    def role(self):
        # print(self.pj.getRoleData("area"))
        # print()
        self.pa.pageMotion(motion='click', locatorExpression="//input[@placeholder='请选择二级组织']")
        self.pa.pageMotion(motion='click', locatorExpression="//span[contains(text()," + "'" + self.pj.getRoleData(
            "area") + "' " + ")]")
        self.pa.pageMotion(motion='click', locatorExpression="//input[@placeholder='请选择三级组织']")
        self.pa.pageMotion(motion='click', locatorExpression="//span[contains(text()," + "'" + self.pj.getRoleData(
            "branch") + "' " + ")]")


if __name__ == "__main__":
    ss = SelectTheSorting()
    ss.selectSort("德阳区域")
