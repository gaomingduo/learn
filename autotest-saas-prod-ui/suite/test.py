# encoding=utf-8
# @time   :2020/5/21 10:22
# @Author :liulaing.song
# @Email  :1056703204@qq.com
# @File   :test.py
# @explain:
import requests
from requests_toolbelt import MultipartEncoder
from config.VarConfig import report

data = MultipartEncoder(
    {
        "baseSchemeId": "35",
        "caseCount": "10",
        "endTime": "2020-05-21 09:58:15",
        "failRate": "0",
        "file": ("体检云--杭州文晖分院测试报告",
                 open("E:\\file\\python code\\python\\autotest-saas-prod-ui\\report\\体检云--杭州文晖分院测试报告.html", 'rb'),
                 'text/plain'),
        "passRate": "10",
        "startTime": "2020-05-21 09:58:15",
        "testResult": "1",
        "testPlanId": ""
    }
)
res = requests.post(url='http://uat.atp.ikang.com/atp-api/report/upload', data=data,
                    headers={'Content-Type': data.content_type}).json()
print(res)
