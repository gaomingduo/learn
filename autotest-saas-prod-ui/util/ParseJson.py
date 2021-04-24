# encoding=utf-8
import json
from config.VarConfig import workNoPath, rolePath, dataPath
import time


class ParseJson(object):
    '''def __init__(self, path):
        self.jsondata = self.readJson()
        self.path = path'''

    # 读取json
    def readJson(self):
        with open(workNoPath) as jp:
            jsonData = json.load(jp)
            return jsonData

    def readRole(self):
        with open(dataPath) as jp:
            jsonData = json.load(jp)
            return jsonData

    def role(self):
        with open(rolePath) as jp:
            jsonData = json.load(jp)
            return jsonData

    def getRoleData(self, data):
        return self.role()["autorityToLogin"][data]

    # 根据关键字获取数据
    def getJsonData(self, data):
        pj = ParseJson()
        return pj.readJson()[data]['workNo']

    # 获取角色
    def getbaseSchemeId(self, baseSchemeId):
        return self.readRole()[baseSchemeId]

    def gettestPlanId(self, testPlanId):
        return self.readRole()[testPlanId]


if __name__ == "__main__":
    pj = ParseJson()
    print(pj.getJsonData('number'))
