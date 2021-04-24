#encoding=utf-8
#@time   :2020/5/9 10:26
#@Author :liulaing.song
#@Email  :1056703204@qq.com
#@File   :VarConfig.py
#@explain:文件的相对路径

import os

#获取当前文件所在目录的父目录的绝对路径
parentDirPath =os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

#接口case路径
casePath = parentDirPath + "\\testData\\case\\saasCase.xlsx"

#log存放地
logPath = parentDirPath + "\\log"

#配置文件存放地
configPath = parentDirPath + "\\config\\config.ini"

#体检号
workNoPath = parentDirPath + "\\config\\workNo.json"

#切换角色
rolePath = parentDirPath + "\\config\\role.json"

#方案id存放地
schemePath = parentDirPath + "\\config\\scheme.json"

#进度条接口数据
dataPath = parentDirPath + "\\config\\data.json"

#报告存放路径
report = parentDirPath + "\\report\\"