# conftest.py 文件名字固定，不能改
import datetime

import pytest


@pytest.fixture(scope="session")
def login():
    print("登陆操作>>>>")
    token = datetime.datetime.now()
    yield token   # yield 相当于return
    print(token)
    print("登出操作")

@pytest.fixture()
def get_username(login):
    name = 'sxg>>'
    print(name)
    return name
