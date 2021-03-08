import pytest


@pytest.fixture(params=['Herry','Hali'],ids=[0,1])
def login(request):
    print("登陆操作")
    return request.param

def test_search(login):
    print(login)
    print("搜索")