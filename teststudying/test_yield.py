import pytest
import datetime
#
# @pytest.fixture(scope="session")
# def login():
#     print("登陆操作")
#     token = datetime.datetime.now()
#     yield token   #yield相当于return
#     print("登出操作")

def test_search(login):
    print("搜索")

def test_cart(login):
    print("购物")
