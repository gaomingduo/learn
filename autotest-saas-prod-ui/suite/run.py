# encoding=utf-8
# @time   :2020/5/20 8:02
# @Author :liulaing.song
# @Email  :1056703204@qq.com
# @File   :run.py
# @explain:执行用例
import os, sys

current_directory = os.path.dirname(os.path.abspath(__file__))
root_path = os.path.abspath(os.path.dirname(current_directory) + os.path.sep + ".")
sys.path.append(root_path)

from testScript.testCase import TestCase
from htmlRunner.NewHtmlReport import NewHtmlReport
import requests

from util.ParseJson import ParseJson
from config.VarConfig import report
from util.Log import Log
from util.RequestMethod import RequestMethod


class Run():

    def __init__(self, area, branch):
        tCase = TestCase()
        self.startTime, self.endTime, self.caseNum, self.pass_count, self.fail_count, self.passingRate, \
        self.failureRate, self.id, self.step, self.motion, self.locatorExpression, \
        self.value, self.expect, self.getText, self.locatorExpressionResult, self.runResult, \
        self.message = tCase.ruCase(area, branch)
        self.systemName = "体检云--" + branch

    def runCase(self):
        htmlRunner = NewHtmlReport()
        htmlRunner.html(testSystem=self.systemName, caseSum=self.caseNum, testPass=self.passingRate,
                        testFail=self.failureRate,
                        start_time=self.startTime, end_time=self.endTime, caseFail=self.fail_count,
                        casePass=self.pass_count, id=self.id,
                        step=self.step, motion=self.motion, locatorExpression=self.locatorExpression,
                        value=self.value, expect=self.expect,
                        getText=self.getText, locatorExpressionResult=self.locatorExpressionResult,
                        runResult=self.runResult)

    def uploading(self):
        rm = RequestMethod()
        rm.uploading(caseCount=self.caseNum, endTime=self.endTime, failureRate=self.failureRate,
                     systemName=self.systemName,
                     passingRate=self.passingRate, startTime=self.startTime, message=self.message)

# runCase("浙江区域", "杭州文晖分院")
