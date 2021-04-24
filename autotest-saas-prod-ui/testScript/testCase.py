# encoding=utf-8
# @time   :2020/5/9 15:36
# @Author :liulaing.song
# @Email  :1056703204@qq.com
# @File   :testCase.py
# @explain:测试用例

from util.SelectTheSorting import SelectTheSorting
from util.ParseExcel import ParseExcel
from util.Log import Log
from action.PageAction import PageAction
from util.ParseJson import ParseJson
import datetime
import time
from util.RequestMethod import RequestMethod


class TestCase(object):

    # 构造函数
    def __init__(self):
        self.parseExcel = ParseExcel()
        self.log = Log()
        self.select = SelectTheSorting()
        self.pa = PageAction()
        self.pj = ParseJson()
        self.rm = RequestMethod()

    # 加载测试用例
    # @app.task
    def ruCase(self, area, branch):
        '''

        :return: 运行测试用例
        '''
        # select = SelectTheSorting()
        self.select.selectSort(area, branch)
        startTime, excel_id, excel_step, excel_motion, excel_locatorExpression, \
        excel_hoverLocator, excel_value, excel_expect, excel_getText, \
        excel_locatorExpressionResult, excel_runResult = self.parseExcel.getCaseData()
        self.log.info("用例开始时间:" + startTime)
        # print(excel_id)
        # print(excel_step)
        # print(excel_motion)
        # print(len(excel_id))
        # print(excel_getText)
        caseNum = len(excel_id) - 1
        pass_count = []
        fail_count = []
        exception = []
        for i in range(len(excel_id)):
            # print(i)
            id = str(excel_id[i])
            step = excel_step[i]
            motion = excel_motion[i]
            # print(motion)
            locatorExpression = excel_locatorExpression[i]
            hoverLocator = excel_hoverLocator[i]
            value = excel_value[i]
            getText = excel_getText[i]
            # print(getText)
            expect = excel_expect[i]
            locatorExpressionResult = excel_locatorExpressionResult[i]
            # print(locatorExpressionResult)
            if motion == "click":
                self.pa.pageMotion(motion=motion, locatorExpression=locatorExpression)
                result = self.pa.pageMotion(motion=getText, locatorExpression=locatorExpressionResult)
                try:
                    if expect in result:
                        self.parseExcel.writeCell(i + 2, 10, "pass")
                        self.log.info("第" + id + "步：" + step + "-----pass")
                        pass_count.append(i)
                    else:
                        self.parseExcel.writeCell(i + 2, 10, "fail")
                        self.log.info("第" + id + "步：" + step + "-----fail")
                        fail_count.append(i)
                        self.pa.pageMotion(motion='quit')
                        break
                except:
                    self.parseExcel.writeCell(i + 2, 10, "fail")
                    self.log.info("第" + id + "步：" + step + "-----exception")
                    exception.append(i)
                    self.pa.pageMotion(motion='quit')
                    break

                self.rm.runMethod(caseCount=caseNum, startTime=startTime, casePresent=id)

            elif motion == "click_bottom":
                self.pa.pageMotion(motion=motion, locatorExpression=locatorExpression)
                result = self.pa.pageMotion(motion=getText, locatorExpression=locatorExpressionResult)
                try:
                    if expect in result:
                        self.parseExcel.writeCell(i + 2, 10, "pass")
                        self.log.info("第" + id + "步：" + step + "-----pass")
                        pass_count.append(i)
                    else:
                        self.parseExcel.writeCell(i + 2, 10, "fail")
                        self.log.info("第" + id + "步：" + step + "-----fail")
                        fail_count.append(i)
                        self.pa.pageMotion(motion='quit')
                        break
                except:
                    self.parseExcel.writeCell(i + 2, 10, "fail")
                    self.log.info("第" + id + "步：" + step + "-----exception")
                    exception.append(i)
                    self.pa.pageMotion(motion='quit')
                    break

                self.rm.runMethod(caseCount=caseNum, startTime=startTime, casePresent=id)

            elif motion == "click_top":
                self.pa.pageMotion(motion=motion, locatorExpression=locatorExpression)
                result = self.pa.pageMotion(motion=getText, locatorExpression=locatorExpressionResult)
                try:
                    if expect in result:
                        self.parseExcel.writeCell(i + 2, 10, "pass")
                        self.log.info("第" + id + "步：" + step + "-----pass")
                        pass_count.append(i)
                    else:
                        self.parseExcel.writeCell(i + 2, 10, "fail")
                        self.log.info("第" + id + "步：" + step + "-----fail")
                        fail_count.append(i)
                        self.pa.pageMotion(motion='quit')
                        break
                except:
                    self.parseExcel.writeCell(i + 2, 10, "fail")
                    self.log.info("第" + id + "步：" + step + "-----exception")
                    exception.append(i)
                    self.pa.pageMotion(motion='quit')
                    break

                self.rm.runMethod(caseCount=caseNum, startTime=startTime, casePresent=id)

            elif motion == "input":
                if value == 'number':
                    self.pa.pageMotion(motion=motion, locatorExpression=locatorExpression,
                                       value=self.pj.getJsonData(value))
                    result = self.pa.pageMotion(motion=getText, locatorExpression=locatorExpressionResult)
                    try:
                        if self.pj.getJsonData(value) in result:
                            self.parseExcel.writeCell(i + 2, 10, "pass")
                            self.log.info("第" + id + "步：" + step + "-----pass")
                            pass_count.append(i)
                        else:
                            self.parseExcel.writeCell(i + 2, 10, "fail")
                            self.log.info("第" + id + "步：" + step + "-----fail")
                            fail_count.append(i)
                            self.pa.pageMotion(motion='quit')
                            break
                    except:
                        self.parseExcel.writeCell(i + 2, 10, "fail")
                        self.log.info("第" + id + "步：" + step + "-----exception")
                        exception.append(i)
                        self.pa.pageMotion(motion='quit')
                        break
                    self.rm.runMethod(caseCount=caseNum, startTime=startTime, casePresent=id)
                else:
                    self.pa.pageMotion(motion=motion, locatorExpression=locatorExpression, value=value)
                    result = self.pa.pageMotion(motion=getText, locatorExpression=locatorExpressionResult)
                    if isinstance(expect, int):
                        expect = str(expect)
                        try:
                            if expect in result:
                                self.parseExcel.writeCell(i + 2, 10, "pass")
                                self.log.info("第" + id + "步：" + step + "-----pass")
                                pass_count.append(i)

                            else:
                                self.parseExcel.writeCell(i + 2, 10, "fail")
                                self.log.info("第" + id + "步：" + step + "-----fail")
                                fail_count.append(i)
                                self.pa.pageMotion(motion='quit')
                                break
                        except:
                            self.parseExcel.writeCell(i + 2, 10, "fail")
                            self.log.info("第" + id + "步：" + step + "-----exception")
                            exception.append(i)
                            self.pa.pageMotion(motion='quit')
                            break
                        self.rm.runMethod(caseCount=caseNum, startTime=startTime, casePresent=id)
                    else:
                        try:
                            if expect in result:
                                self.parseExcel.writeCell(i + 2, 10, "pass")
                                self.log.info("第" + id + "步：" + step + "-----pass")
                                pass_count.append(i)

                            else:
                                self.parseExcel.writeCell(i + 2, 10, "fail")
                                self.log.info("第" + id + "步：" + step + "-----fail")
                                fail_count.append(i)
                                self.pa.pageMotion(motion='quit')
                                break
                        except:
                            self.parseExcel.writeCell(i + 2, 10, "fail")
                            self.log.info("第" + id + "步：" + step + "-----exception")
                            exception.append(i)
                            self.pa.pageMotion(motion='quit')
                            break
                        self.rm.runMethod(caseCount=caseNum, startTime=startTime, casePresent=id)

            elif motion == "hover":
                self.pa.pageMotion(motion=motion, locatorExpression=locatorExpression)
                result = self.pa.pageMotion(motion=getText, locatorExpression=locatorExpressionResult)
                try:
                    if expect in result:
                        self.parseExcel.writeCell(i + 2, 10, "pass")
                        self.log.info("第" + id + "步：" + step + "-----pass")
                        pass_count.append(i)
                    else:
                        self.parseExcel.writeCell(i + 2, 10, "fail")
                        self.log.info("第" + id + "步：" + step + "-----fail")
                        fail_count.append(i)
                        self.pa.pageMotion(motion='quit')
                        break
                except:
                    self.parseExcel.writeCell(i + 2, 10, "fail")
                    self.log.info("第" + id + "步：" + step + "-----exception")
                    exception.append(i)
                    self.pa.pageMotion(motion='quit')
                    break

                self.rm.runMethod(caseCount=caseNum, startTime=startTime, casePresent=id)

            elif motion == "double_click":
                self.pa.pageMotion(motion=motion, locatorExpression=locatorExpression)
                result = self.pa.pageMotion(motion=getText, locatorExpression=locatorExpressionResult)
                try:
                    if expect in result:
                        self.parseExcel.writeCell(i + 2, 10, "pass")
                        self.log.info("第" + id + "步：" + step + "-----pass")
                        pass_count.append(i)
                    else:
                        self.parseExcel.writeCell(i + 2, 10, "fail")
                        self.log.info("第" + id + "步：" + step + "-----fail")
                        fail_count.append(i)
                        self.pa.pageMotion(motion='quit')
                        break

                except:
                    self.parseExcel.writeCell(i + 2, 10, "fail")
                    self.log.info("第" + id + "步：" + step + "-----exception")
                    exception.append(i)
                    self.pa.pageMotion(motion='quit')
                    break
                self.rm.runMethod(caseCount=caseNum, startTime=startTime, casePresent=id)

            elif motion == "double_click_esc":
                self.pa.pageMotion(motion=motion, locatorExpression=locatorExpression)
                result = self.pa.pageMotion(motion=getText, locatorExpression=locatorExpressionResult)
                try:
                    if expect in result:
                        self.parseExcel.writeCell(i + 2, 10, "pass")
                        self.log.info("第" + id + "步：" + step + "-----pass")
                        pass_count.append(i)
                    else:
                        self.parseExcel.writeCell(i + 2, 10, "fail")
                        self.log.info("第" + id + "步：" + step + "-----fail")
                        fail_count.append(i)
                        self.pa.pageMotion(motion='quit')
                        break
                except:
                    self.parseExcel.writeCell(i + 2, 10, "fail")
                    self.log.info("第" + id + "步：" + step + "-----exception")
                    exception.append(i)
                    self.pa.pageMotion(motion='quit')
                    break

                self.rm.runMethod(caseCount=caseNum, startTime=startTime, casePresent=id)

            elif motion == "enter":
                self.pa.pageMotion(motion=motion, locatorExpression=locatorExpression)
                result = self.pa.pageMotion(motion=getText, locatorExpression=locatorExpressionResult)
                try:
                    if expect in result:
                        self.parseExcel.writeCell(i + 2, 10, "pass")
                        self.log.info("第" + id + "步：" + step + "-----pass")
                        pass_count.append(i)
                    else:
                        self.parseExcel.writeCell(i + 2, 10, "fail")
                        self.log.info("第" + id + "步：" + step + "-----fail")
                        fail_count.append(i)
                        self.pa.pageMotion(motion='quit')
                        break
                except:
                    self.parseExcel.writeCell(i + 2, 10, "fail")
                    self.log.info("第" + id + "步：" + step + "-----exception")
                    exception.append(i)
                    self.pa.pageMotion(motion='quit')
                    break

                self.rm.runMethod(caseCount=caseNum, startTime=startTime, casePresent=id)

            elif motion == "top":
                self.pa.pageMotion(motion=motion)
                result = self.pa.pageMotion(motion=getText, locatorExpression=locatorExpressionResult)
                try:
                    if expect in result:
                        self.parseExcel.writeCell(i + 2, 10, "pass")
                        self.log.info("第" + id + "步：" + step + "-----pass")
                        pass_count.append(i)
                    else:
                        self.parseExcel.writeCell(i + 2, 10, "fail")
                        self.log.info("第" + id + "步：" + step + "-----fail")
                        fail_count.append(i)
                        self.pa.pageMotion(motion='quit')
                        break
                except:
                    self.parseExcel.writeCell(i + 2, 10, "fail")
                    self.log.info("第" + id + "步：" + step + "-----exception")
                    exception.append(i)
                    self.pa.pageMotion(motion='quit')
                    break

                self.rm.runMethod(caseCount=caseNum, startTime=startTime, casePresent=id)

            elif motion == "click_esc":
                self.pa.pageMotion(motion=motion, locatorExpression=locatorExpression)
                result = self.pa.pageMotion(motion=getText, locatorExpression=locatorExpressionResult)
                try:
                    if expect in result:
                        self.parseExcel.writeCell(i + 2, 10, "pass")
                        self.log.info("第" + id + "步：" + step + "-----pass")
                        pass_count.append(i)
                    else:
                        self.parseExcel.writeCell(i + 2, 10, "fail")
                        self.log.info("第" + id + "步：" + step + "-----fail")
                        fail_count.append(i)
                        self.pa.pageMotion(motion='quit')
                        break
                except:
                    self.parseExcel.writeCell(i + 2, 10, "fail")
                    self.log.info("第" + id + "步：" + step + "-----exception")
                    exception.append(i)
                    self.pa.pageMotion(motion='quit')
                    break

                self.rm.runMethod(caseCount=caseNum, startTime=startTime, casePresent=id)

            elif motion == "click_role":
                self.select.role()
                self.pa.pageMotion(motion=motion, locatorExpression=locatorExpression)
                result = self.pa.pageMotion(motion=getText, locatorExpression=locatorExpressionResult)
                try:
                    if expect in result:
                        self.parseExcel.writeCell(i + 2, 10, "pass")
                        self.log.info("第" + id + "步：" + step + "步" + "-----pass")
                        pass_count.append(i)
                    else:
                        self.parseExcel.writeCell(i + 2, 10, "fail")
                        self.log.info("第" + id + "步：" + step + "-----fail")
                        fail_count.append(i)
                        self.pa.pageMotion(motion='quit')
                        break
                except:
                    self.parseExcel.writeCell(i + 2, 10, "fail")
                    self.log.info("第" + id + "步：" + step + "-----exception")
                    exception.append(i)
                    self.pa.pageMotion(motion='quit')
                    break

                self.rm.runMethod(caseCount=caseNum, startTime=startTime, casePresent=id)

            elif motion == "click_sleep":
                self.pa.pageMotion(motion=motion, locatorExpression=locatorExpression)
                result = self.pa.pageMotion(motion=getText, locatorExpression=locatorExpressionResult)
                try:
                    if expect in result:
                        self.parseExcel.writeCell(i + 2, 10, "pass")
                        self.log.info("第" + id + "步：" + step + "-----pass")
                        pass_count.append(i)
                    else:
                        self.parseExcel.writeCell(i + 2, 10, "fail")
                        self.log.info("第" + id + "步：" + step + "-----fail")
                        fail_count.append(i)
                        self.pa.pageMotion(motion='quit')
                        break
                except:
                    self.parseExcel.writeCell(i + 2, 10, "fail")
                    self.log.info("第" + id + "步：" + step + "-----exception")
                    exception.append(i)
                    self.pa.pageMotion(motion='quit')
                    break

                self.rm.runMethod(caseCount=caseNum, startTime=startTime, casePresent=id)

            elif motion == "click_await":
                self.rm.runMethod(caseCount=caseNum, startTime=startTime, casePresent=id)
                self.pa.pageMotion(motion=motion, locatorExpression=locatorExpression)
                result = self.pa.pageMotion(motion=getText, locatorExpression=locatorExpressionResult)
                try:
                    if expect in result:
                        self.parseExcel.writeCell(i + 2, 10, "pass")
                        self.log.info("第" + id + "步：" + step + "-----pass")
                        pass_count.append(i)
                    else:
                        self.parseExcel.writeCell(i + 2, 10, "fail")
                        self.log.info("第" + id + "步：" + step + "-----fail")
                        fail_count.append(i)
                        self.pa.pageMotion(motion='quit')
                        break
                except:
                    self.parseExcel.writeCell(i + 2, 10, "fail")
                    self.log.info("第" + id + "步：" + step + "-----exception")
                    exception.append(i)
                    self.pa.pageMotion(motion='quit')
                    break

                self.rm.runMethod(caseCount=caseNum, startTime=startTime, casePresent=id)

            elif motion == "quit":
                self.parseExcel.writeCell(i + 2, 10, "pass")
                self.pa.pageMotion(motion=motion)

        excelstartTime, excelid, excelstep, excelmotion, excellocatorExpression, \
        excelhoverLocator, excelvalue, excelexpect, excelgetText, \
        excellocatorExpressionResult, runResult = self.parseExcel.getCaseData()

        # endTime = datetime.datetime.now()
        endTime = time.strftime('%Y-%m-%d %H:%M:%S')

        self.log.info("用例结束时间:" + endTime)
        # sumCase = len(pass_count) + len(fail_count)
        pr = len(pass_count) / caseNum
        # passingRate = '{:.0%}'.format(pr)
        passingRate = "%.2f" % pr
        fr = len(fail_count) / caseNum
        # failureRate = '{:.0%}'.format(fr)
        failureRate = "%.2f" % fr
        print(failureRate)
        self.log.info("用例通过条数" + str(len(pass_count)))
        self.log.info("用例失败条数：" + str(len(fail_count)))
        self.log.info("xpath定位失败：" + str(len(exception)))
        message = None
        if len(pass_count) == caseNum:
            message = 1  # 1代表成功

        if len(fail_count) > 0:
            message = 2  # 2代表失败

        if len(exception) > 0:
            message = 3  # 3代表未找到定位元素

        # print(message)
        return startTime, endTime, caseNum, len(pass_count), len(fail_count), passingRate, failureRate, \
               excel_id, excel_step, excel_motion, excel_locatorExpression, excel_value, excel_expect, excel_getText, \
               excel_locatorExpressionResult, runResult, message


if __name__ == '__main__':
    test = TestCase()

    # print(test.ruCase("浙江区域", "杭州文晖分院"))
    print(test.ruCase("成都区域", "爱康国宾成都茶店子分院"))
