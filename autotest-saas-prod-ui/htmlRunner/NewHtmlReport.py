# encoding=utf-8
'''
    _Function:
    _Author:liuliang.song
    _CreateTime:
'''

html_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>自动化测试报告</title>
    <link href="https://cdn.bootcss.com/bootstrap/3.3.5/css/bootstrap.min.css" rel="stylesheet">
    <link href="https://cdn.bootcss.com/font-awesome/4.4.0/css/font-awesome.min.css" rel="stylesheet">
    <link href="https://cdn.bootcss.com/animate.css/3.5.2/animate.min.css" rel="stylesheet">
    <link href="https://cdn.bootcss.com/chosen/1.8.2/chosen.css" rel="stylesheet">
    <!-- 引入 echarts.js -->
    <script type="text/javascript" src="https://cdn.bootcss.com/echarts/3.8.5/echarts.min.js"></script>
    <style>
        body{
            margin: 0;
            font-family: "Arial", "Microsoft YaHei", "黑体", "宋体", sans-serif;
            font-size: 18px;
            line-height: 1.5;
            color: #333333;
        }
h5 {
	font-size: 25px;
    margin-top: 5px;
	font-weight: 600
}
.table {margin-bottom: 2px;
    width: 100%%;
    height:100px
}

.hiddenRow {
    display: none;
}

.container-fluid {
    padding-right: 120px;
    padding-left: 120px;
}

.nav-tabs li {
    width: 186px;
    text-align: center;

}
    </style>
</head>
<body>
<script type="text/javascript">
    function showClassDetail(detail_id, hiddenRow_id, class_type) {
        console.log(document.getElementById(hiddenRow_id).className);
    
        if ('详细' ==  document.getElementById(detail_id).innerText) {
            if ('all' == class_type) {
                document.getElementById(hiddenRow_id).className = 'all';
            }
            else if ('success' == class_type) {
                document.getElementById(hiddenRow_id).className = 'success';
            }
            else if ('error' == class_type) {
                document.getElementById(hiddenRow_id).className = 'error';
            }
            else{
                document.getElementById(hiddenRow_id).className = 'untreaded';
            }
            document.getElementById(detail_id).innerText = "收起"
        }
        else {
            document.getElementById(detail_id).innerText = "详细";
            document.getElementById(hiddenRow_id).className = 'hiddenRow';
        }
    }
</script>
<div class="container-fluid">
    <div class="page-header" style="text-align:center;">
        <span style=" color: #1ab394; font-size: 35px; font-weight: 700; line-height:10px;">自动化测试报告</span>
    </div>
    <div class="col-md-12">
        <h5 style="line-height:25px">测试基本信息</h5><br>
        <div class="col-md-12">
            <div class="col-md-4" style="Background-Color:#FFFFFF; height:310px;width:500px;">
                <table class="table table-hover table-bordered" style="width:650px; height:70px">
                    <tbody>
                    <tr class="info">
                        <td class="text-center" style="Background-Color:#FFFFFF;color: #5E5E5E;font-weight: 600;">测试系统</td>
                        <td class="text-center" style="Background-Color:#FFFFFF;color: #5E5E5E;font-weight: 600;">%(testSystem)s</td>
                    </tr>
                    <tr class="info">
                        <td class="text-center" style="Background-Color:#FFFFFF;color: #5E5E5E;font-weight: 600;">用例总数</td>
                        <td class="text-center" style="Background-Color:#FFFFFF;color: #5E5E5E;font-weight: 600;">%(caseSum)s</td>
                    </tr>
                    <tr class="info">
                        <td class="text-center" style="Background-Color:#FFFFFF;color: #1ab394;font-weight: 600;">用例通过数</td>
                        <td class="text-center" style="Background-Color:#FFFFFF;color: #1ab394;font-weight: 600;">%(testPass)s</td>
                    </tr>
                    <tr class="info">
                        <td class="text-center" style="Background-Color:#FFFFFF;color: #d9534f;font-weight: 600;">用例失败数</td>
                        <td class="text-center" style="Background-Color:#FFFFFF;color: #d9534f;font-weight: 600;">%(testFail)s</td>
                    </tr>
                    <tr class="info">
                        <td class="text-center" style="Background-Color:#FFFFFF;color: #5E5E5E;font-weight: 600;">开始时间</td>
                        <td class="text-center" style="Background-Color:#FFFFFF;color: #5E5E5E;font-weight: 600;">%(start_time)s</td>
                    </tr>
                    <tr class="info">
                        <td class="text-center" style="Background-Color:#FFFFFF;color: #5E5E5E;font-weight: 600;">结束时间</td>
                        <td class="text-center" style="Background-Color:#FFFFFF;color: #5E5E5E;font-weight: 600;">%(end_time)s</td>
                    </tr>
                    </tbody>
                </table>
            </div>
            <div class="col-md-8">
            <div id="main" style="height:300px;width: 1000px;position:absolute; left:250px; top:10px;"></div>
            <script type="text/javascript">
                var myChart = echarts.init(document.getElementById('main'));
                var option = {
                    backgroundColor: '#FFFFFF', //背景色
                    title: {
                        text: '测试用例运行结果',
                        x: 'center'
                    },
                    legend: {
                        orient: 'vertical',
                        x: 'left',
                        data: ['成功', '失败']
                    },
                    color: ['#1ab394', '#d9534f'],
                    calculable: true,
                    series:[
                        {
                            name: '运行结果',
                            type: 'pie',
                            radius: '55%%',
                            center: ['50%%', '60%%'],
                            startAngle: 135,
                            data:[{
                                value:%(casePass)s,
                                name:'成功',
                                itemStyle:{
                                    normal:{
                                        label:{
                                            formatter:'{b} : {c} ({d}%%)',
                                            textStyle:{
                                                align:'left',
                                                fontSize:15,
                                            }
                                        },
                                        labelLine:{
                                            length:40,
                                        }
                                    }
                                }
                            },{
                                value:%(caseFail)s,
                                name: '失败',
                                itemStyle:{
                                    normal:{
                                        label:{
                                            formatter: '{b} : {c} ({d}%%)',
                                            textStyle:{
                                                align: 'right',
                                                fontSize: 15,
                                            }
                                        },
                                        labelLine:{
                                            length:40,
                                        }
                                    }
                                }
                            }],
                        }
                    ]
                };
                // 为echarts对象加载数据
                myChart.setOption(option);
            </script>
            </div>
        </div>
        <br>
        <div class="col-md-12">
            <div class="tabbable" id="tabs-957640">
                <ul class="nav nav-tabs">
                    <li class="active">
                        <a data-toggle="tab" style="Background-Color: #428bca; color: #fff;"><button onclick="select('all')" style="width: 100%%; Background-Color: #428bca; color: #fff; border: none; outline: none;">全  部 (%(caseSum)s)</button></a>
                    </li>
                    <li>
                        <a data-toggle="tab" style="Background-Color: #1ab394; color: #fff;"><button onclick="select('pass')" style="width: 100%%; Background-Color: #1ab394; color: #fff; border: none; outline: none;">成  功 (%(casePass)s)</button></a>
                    </li>
                    <li>
                        <a data-toggle="tab" style="Background-Color: #d9534f; color: #fff;"><button onclick="select('fail')" style="width: 100%%; Background-Color: #d9534f; color: #fff; border: none; outline: none;">失  败 (%(caseFail)s)</button></a>
                    </li>
                </ul>
            </div>
            <div class="tab-content">
                <div class="tab-pane active" id="panel-0">
                    <table class="table table-hover table-bordered">
                        <tr class="header">
                            <th class="text-center" style="Background-Color:#CDC5BF" width="10%%">ID</th>
                            <th class="text-center" style="Background-Color:#CDC5BF" width="10%%">测试步骤</th>
                            <th class="text-center" style="Background-Color:#CDC5BF" width="10%%">动作</th>
                            <th class="text-center" style="Background-Color:#CDC5BF" >操作元素定位表达式</th>
                            <th class="text-center" style="Background-Color:#CDC5BF" width="10%%">操作值</th>
                            <th class="text-center" style="Background-Color:#CDC5BF" width="10%%">预期结果</th>
                            <th class="text-center" style="Background-Color:#CDC5BF" width="10%%">获取文本</th>
                            <th class="text-center" style="Background-Color:#CDC5BF" >实际结果元素定位表达式</th>
                            <th class="text-center" style="Background-Color:#CDC5BF" width="10%%">实际结果</th>
                            <th class="text-center" style="Background-Color:#CDC5BF" width="10%%">详细信息</th>
                        </tr>
                        %(table_try)s
                    </table>
                    <script type="text/javascript">
                        //change color
                        //取都用demo的多组
                        var eles = document.getElementsByClassName('demo');
                        var alleles = document.getElementsByClassName('all');
                        console.log(eles);
                        var x=document.getElementById("demo").innerText;
                        console.log("the value is :"+x);
                        //每组都应用样式
                        for(var i = 0; i < eles.length; i++){
                            if(eles[i].innerText == 'pass'){
                                eles[i].style.color = 'green';
                            }else{
                                eles[i].style.color = 'red';
                            }
                        }
                        function select(type) {
							for(var i = 0; i < eles.length; i++){
							if(type=='all'){    // 选中all时，数据全部显示
								alleles[i].style.display = "";
							}else{                   // 选中其他的值时，进一步判断
								if(eles[i].innerText != type){
								// 列中的值和选中值一致
									alleles[i].style.display = "none";  // 该行显示
								}else{
									alleles[i].style.display = "";
								}
							}
						}
						}
                    </script>
                </div>
            </div>
        </div>
    </div>
</div>
</body>
</html>
"""
# variables: testSystem, caseSum, testPass, testFail, start_time, end_time, casePass, caseFail, caseSkip

# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
# Report
REPORT_TMPL_CASE = """
    <tr class="all" style="font-size: 15px;">
        <td class="text-center" style="font-weight: bold;font-size: 16px;">%(id)s</td>
        <td class="text-center">%(step)s</td>
        <td class="text-center">%(motion)s</td>
        <td class="text-center" style="font-weight: bold;font-size: 16px;">%(locatorExpression)s</td>
        <td class="text-center">%(value)s</td>
        <td class="text-center">%(expect)s</td>
        <td class="text-center" style="font-weight: bold;font-size: 16px;">%(getText)s</td>
        <td class="text-center">%(locatorExpressionResult)s</td>
        <td class="demo text-center" id="demo" style="font-weight: bold;font-size: 16px;">%(runResult)s</td>
        <td class="text-center" style="font-weight: bold;font-size: 16px;">
            <a href="javascript:showClassDetail('q%(detail_id)s', 'p%(detail_id)s', 'success')" class="detail" id = "q%(detail_id)s">详细</a>
        </td>
    </tr>
    <tr class='hiddenRow' id="p%(detail_id)s" style="Background-Color:#FFFFFF">
        <td colspan='9'>
            <pre class="text-left" style="Background-Color:#FFFFFF; overflow-y: scroll;height: 200px; width: 1000px;font-weight: bold;font-size: 14px;">%(step)s</pre>
        </td>
    </tr>
"""

import os
from util.Log import Log


class NewHtmlReport(object):

    def __init__(self):
        self.log = Log()

    def html(self, testSystem, caseSum, testPass, testFail, start_time, end_time, casePass, caseFail,
             id, step, motion, locatorExpression, value, expect, getText, locatorExpressionResult, runResult):
        table_tr2 = ""
        a = ["id", "step", "motion", "locatorExpression", "value", "expect", "getText", "locatorExpressionResult",
             "runResult"]
        if type(id) == list:
            for i in range(len(id)):
                results = []
                results += [id[i], step[i], motion[i], locatorExpression[i], value[i], expect[i], getText[i],
                            locatorExpressionResult[i], runResult[i]]
                b = results
                c = zip(a, b)
                d = dict(c)
                table_td_case = REPORT_TMPL_CASE % dict(id=d["id"], step=d["step"], motion=d["motion"],
                                                        locatorExpression=d["locatorExpression"], value=d["value"],
                                                        expect=d["expect"], getText=d["getText"],
                                                        locatorExpressionResult=d["locatorExpressionResult"],
                                                        runResult=d["runResult"], detail_id=d["id"],
                                                        hiddenRow_id=d["id"])
                table_tr2 += table_td_case

        table_td = html_template % dict(testSystem=testSystem, caseSum=caseSum, testPass=testPass,
                                        testFail=testFail, start_time=start_time, end_time=end_time,
                                        casePass=casePass, caseFail=caseFail, table_try=table_tr2)
        filename = '{name}测试报告.html'.format(name=testSystem)
        dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'report')
        filename = os.path.join(dir, filename)
        # print(filename)
        self.log.info("用例执行完成请查看测试报告：" + filename)
        with open(filename, 'wb') as f:
            f.write(table_td.encode('utf8'))


if __name__ == "__main__":
    testSystem = "体检云"
    caseSum = 9
    testPass = 9
    testFail = 9
    start_time = 9
    end_time = 9
    casePass = 9
    caseFail = 9
    id = ["1", "2", "3"]
    step = ['点击登记', '点击展开客户类型点击展开客户类型点击展开客户类型点击展开客户类型点击展开客户类型点击展开客户类型', '选择散客登记']

    motion = ['click', 'click', 'click']
    locatorExpression = ["//span[text()='登记']", "//div[@class='el-select el-tooltip']//div[1]//input",
                         "//div[@class='el-scrollbar']//div[1]//ul[1]//li[2]//span[text()='散客']"]
    value = ['自动化测试', '自动化测试', '自动化测试']
    expect = ["客户信息", '散客', "散客"]
    getText = ['text', 'text', 'text']
    locatorExpressionResult = ["//div[@class='title']//h3",
                               "//div[@class='el-scrollbar']//div[1]//ul[1]//li[2]//span[text()='散客']//div[@class='el-scrollbar']//div[1]//ul[1]//li[2]//span[text()='散客']",
                               "//div[@class='el-select el-tooltip']//div[1]//input"]
    runResult = ["pass", "fail", "pass"]

    nhr = NewHtmlReport()
    nhr.html(testSystem=testSystem, caseSum=caseSum, testPass=testPass, testFail=testFail, start_time=start_time,
             end_time=end_time, caseFail=caseFail, casePass=casePass,
             id=id, step=step, motion=motion, locatorExpression=locatorExpression, value=value, expect=expect,
             getText=getText, locatorExpressionResult=locatorExpressionResult, runResult=runResult)
