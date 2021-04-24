# encoding=utf-8
# @time   :2020/5/9 15:34
# @Author :liulaing.song
# @Email  :1056703204@qq.com
# @File   :AssertionResults.py
# @explain:断言结果

class AssertionResults(object):

    # 断言方法
    def assertMethod(self, expect, response):
        '''

        :param expect: 预期结果
        :param response: 实际结果
        :return: 断言一个字符串在另一个字符串中
        '''
        flag = None

        if expect in response:
            flag = True
        else:
            flag = False

        return flag
