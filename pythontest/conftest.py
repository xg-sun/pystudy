"""
__author__ = 'hogwarts_xixi'
"""

# 一个功能点封装成一个fixture
import time

import pytest
# 定义fixture,获取 calc对象
from pythoncode.Calculator import Calculator


# 打印想要的数据信息
@pytest.fixture(autouse=True)
def print_info():
    # 【开始计算】，之后【结束计算】
    print("开始计算")
    # yield 关键字关面相当于setup
    yield  # return
    # yield 关键字关面相当于 teardown
    print("结束计算")


# 获取 calc 实例
@pytest.fixture(scope="session", autouse=True)
def get_calc():
    calc = Calculator()
    yield calc
    print("测试结束")


# @pytest.fixture(scope="session", autouse=True)
# def finish():
#     yield
#     print("测试结束")


# @pytest.fixture(scope="session", autouse=True)
# def open_browser():
#     print("打开浏览器")
#     pass

@pytest.fixture(scope="session", autouse=True)
def manage_logs(request):
    """Set log file name same as test name"""

    now = time.strftime("%Y-%m-%d_%H-%M-%S")
    log_name = './logs/' + now + '.logs'

    request.config.pluginmanager.get_plugin("logging-plugin") \
        .set_log_path(log_name)


# @pytest.fixture()
# def connect_db():
#     print("连接数据库")
#     pass


# hook 函数，预加载
def pytest_collection_modifyitems(items):
    """
    测试用例收集完成时，将收集到的item的name和nodeid的中文显示
    :return:
    """
    for item in items:
        item.name = item.name.encode("utf-8").decode("unicode_escape")
        item._nodeid = item.nodeid.encode("utf-8").decode("unicode_escape")
