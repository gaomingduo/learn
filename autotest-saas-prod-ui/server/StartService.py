# encoding=utf-8
# @time   :2020/5/11 17:40
# @Author :liulaing.song
# @Email  :1056703204@qq.com
# @File   :StartService.py
# @explain:启动服务入口
from flask import Flask, request
import os, sys

current_directory = os.path.dirname(os.path.abspath(__file__))

root_path = os.path.abspath(os.path.dirname(current_directory) + os.path.sep + ".")
sys.path.append(root_path)
import json, threading
from concurrent.futures import ThreadPoolExecutor
from util.ReplaceValue import ReplaceValue

excutor = ThreadPoolExecutor(10)
app = Flask(__name__)
lock = threading.Lock()


@app.route("/api/runCase", methods=['POST'])
def server():
    # return_dict = {'return_code': '200', 'return_info': '处理成功', 'result': False}
    return_dict = {'code': '200', 'msg': '脚本执行中'}

    if request.get_data() is None:
        return_dict['code'] = '1'
        return_dict['area'] = '选择区域为空'
        return json.dumps(return_dict, ensure_ascii=False)
    else:
        rv = ReplaceValue()
        getData = request.get_data()
        try:
            # 传入的参数为bytes类型，需要转化成json
            getData = json.loads(getData)
        except:
            return_dict['code'] = '500'
            return_dict['area'] = '请检查请求参数类型是否正确'
            return json.dumps(return_dict, ensure_ascii=False)
        area = getData.get('area')
        branch = getData.get('branch')
        baseSchemeId = getData.get('baseSchemeId')
        testPlanId = getData.get('testPlanId')
        # print(area)
        rv.scheme(baseSchemeId=baseSchemeId, testPlanId=testPlanId)
        rv.autorityToLogin(area=area, branch=branch)
        excutor.submit(run, area, branch)

        # thread = threading.Thread(target=run, args=(area, branch,))
        # thread.start()
        # return_dict['result'] = "ok"

    return json.dumps(return_dict, ensure_ascii=False)
    # return {}


def run(area, branch):
    # from testScript.testCase import TestCase
    from suite.run import Run
    lock.acquire()
    try:
        run = Run(area, branch)
        run.runCase()
        run.uploading()
        result_str = "{}".format(area)
        return result_str
    finally:
        lock.release()


@app.route("/api/heartbeat", methods=['GET'])
def heartbeat():
    try:
        return_dict = {'return_info': 'success'}
        return json.dumps(return_dict, ensure_ascii=False)
    except:
        return_dict = {'return_info': 'Service not started！！！'}
        return json.dumps(return_dict, ensure_ascii=False)


if __name__ == "__main__":
    app.run(host='10.105.19.29', port=7873, debug=True, threaded=True)
