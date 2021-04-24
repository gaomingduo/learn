# encoding=utf-8
# @time   :2020/5/14 20:38
# @Author :liulaing.song
# @Email  :1056703204@qq.com
# @File   :ReplaceValue.py
# @explain:替换json中的值

import json
from config.VarConfig import workNoPath, rolePath, schemePath, dataPath
import time


class ReplaceValue(object):

    def keepValue(self, workNo):
        with open(workNoPath, "r") as jp:
            data = json.load(jp)
            data["number"]["workNo"] = workNo
        with open(workNoPath, "w+") as fp:
            json.dump(data, fp, ensure_ascii=False, indent=4)

    def autorityToLogin(self, area=None, branch=None):
        with open(rolePath, "r", encoding="gbk") as jp:
            data = json.load(jp)
            data["autorityToLogin"]["area"] = area
            data["autorityToLogin"]["branch"] = branch
        with open(rolePath, "w+") as fp:
            json.dump(data, fp, ensure_ascii=False, indent=4)

    def scheme(self, baseSchemeId, testPlanId):
        with open(dataPath, "r") as jp:
            data = json.load(jp)
            data["baseSchemeId"] = baseSchemeId
            data["testPlanId"] = testPlanId
        with open(dataPath, "w+") as fp:
            json.dump(data, fp, ensure_ascii=False, indent=4)

    def data(self, caseCount, startTime, casePresent):
        with open(dataPath, "r") as jp:
            data = json.load(jp)
            data["caseCount"] = caseCount
            data["startTime"] = startTime
            data["casePresent"] = casePresent
        with open(dataPath, "w+") as fp:
            json.dump(data, fp, ensure_ascii=False, indent=4)


if __name__ == "__main__":
    sv = ReplaceValue()
    sv.data("123", "123", "123")
