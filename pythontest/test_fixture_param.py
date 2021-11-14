import pytest


@pytest.fixture(params=["hurry", "hogwarts", "aaaa"], ids=['用户名1', '用户名2', '用户名3'])
def login1(request):
    return request.param


def test_cart1(login1):
    print(login1)


@pytest.mark.parametrize("username", ["hurry", "hogwarts"])
def test_cart(username):
    print(f"username : {username}")
