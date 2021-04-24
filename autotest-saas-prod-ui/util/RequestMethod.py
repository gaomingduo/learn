# encoding=utf-8
# @time   :2020/5/20 17:59
# @Author :liulaing.song
# @Email  :1056703204@qq.com
# @File   :RequestMethod.py
# @explain:接口请求
import requests
from util.ParseJson import ParseJson
from util.Log import Log
from requests_toolbelt import MultipartEncoder
import json
from config.VarConfig import report
import time


class RequestMethod(object):

    def __init__(self):
        self.pj = ParseJson()
        self.log = Log()

    def runMethod(self, caseCount, startTime, casePresent):
        testPlanId = self.pj.gettestPlanId('testPlanId')
        if testPlanId == "0":

            header = {
                "Content-Type": "application/json"
            }
            data = {
                "baseSchemeId": self.pj.getbaseSchemeId('baseSchemeId'),
                "caseCount": caseCount,
                "startTime": startTime,
                "casePresent": casePresent,
                "testPlanId": ""
            }
            try:
                res = requests.post(url="http://uat.atp.ikang.com/atp-api/report/testing", data=json.dumps(data),
                                    headers=header).json()
                time.sleep(2)
                self.log.info("进度条接口返回：" + json.dumps(res, ensure_ascii=False))
            except Exception as e:
                self.log.info("接口请求失败： %s" % e)

        else:

            header = {
                "Content-Type": "application/json"
            }
            data = {
                "baseSchemeId": self.pj.getbaseSchemeId('baseSchemeId'),
                "caseCount": caseCount,
                "startTime": startTime,
                "casePresent": casePresent,
                "testPlanId": testPlanId
            }
            try:
                res = requests.post(url="http://uat.atp.ikang.com/atp-api/report/testing", data=json.dumps(data),
                                    headers=header).json()
                time.sleep(2)
                self.log.info("进度条接口返回：" + json.dumps(res, ensure_ascii=False))
            except Exception as e:
                self.log.info("接口请求失败： %s" % e)

    def uploading(self, caseCount, endTime, failureRate, systemName, passingRate, startTime, message):

        testPlanId = str(self.pj.gettestPlanId("testPlanId"))

        if testPlanId == "0":
            data = MultipartEncoder(
                {
                    "baseSchemeId": str(self.pj.getbaseSchemeId("baseSchemeId")),
                    "caseCount": str(caseCount),
                    "endTime": str(endTime),
                    "failRate": str(failureRate),
                    "file": (systemName,
                             open(report + systemName + "测试报告.html", 'rb'),
                             'text/plain'),
                    "passRate": str(passingRate),
                    "startTime": str(startTime),
                    "testResult": str(message),
                    "testPlanId": ""
                }
            )
            try:
                res = requests.post(url='http://uat.atp.ikang.com/atp-api/report/upload', data=data,
                                    headers={'Content-Type': data.content_type}).json()
                time.sleep(2)
                self.log.info("上传接口返回：" + json.dumps(res, ensure_ascii=False))
            except Exception as e:
                self.log.info("请求接口失败：%s" % e)

        else:
            data = MultipartEncoder(
                {
                    "baseSchemeId": str(self.pj.getbaseSchemeId("baseSchemeId")),
                    "caseCount": str(caseCount),
                    "endTime": str(endTime),
                    "failRate": str(failureRate),
                    "file": (systemName,
                             open(report + systemName + "测试报告.html", 'rb'),
                             'text/plain'),
                    "passRate": str(passingRate),
                    "startTime": str(startTime),
                    "testResult": str(message),
                    "testPlanId": ""
                }
            )
            try:
                res = requests.post(url='http://uat.atp.ikang.com/atp-api/report/upload', data=data,
                                    headers={'Content-Type': data.content_type}).json()
                time.sleep(2)
                self.log.info("上传接口返回：" + json.dumps(res, ensure_ascii=False))
            except Exception as e:
                self.log.info("请求接口失败：%s" % e)
