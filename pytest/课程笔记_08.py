'''
pytest 运行：
    -k 运行所有满足表达式的测试用例   例如：pytest -k 'add'
    collect 查询一共有多少条测试用例  例如：pytest --collect-only
    -m 加标签，执行需要价格-m参数，为用例加@pytest.mark.标签名
    --junit-xml 生成一个执行结果的xml文件
    测试用例执行顺序插件：pytest-ordering
        例如:@pytest.mark.run(order=1)
            @pytest.mark.run(order=-1)
            @pytest.mark.run(order=3)
    conftest.py 文件
        可以共享数据、方法，fixture方法放置在这个文件下fixture方法需要传入方法里执行，除非使用autoUse = ture
        添加一些方法，改写执行顺序
        添加方法，自动的添加标签
    pytest.ini 配置文件
        改变pytest运行的行为
        pytest改写 文件名、类名、方法 等
    导出依赖包：
        bash：
            $ env1/bin/pip freeze > requirements.txt
            $ env2/bin/pip install -r requirements.txt

数据驱动：
    测试数据的数据驱动
    测试步骤的数据驱动
'''
