from datetime import datetime

import pytest


@pytest.fixture(scope="session")
def login():
    print("登陆操作>>>>")
    name = "哈利波特"
    yield name   # yield 相当于return
    print(name)
    print("登出操作")