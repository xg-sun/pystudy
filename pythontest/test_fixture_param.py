"""
__author__ = 'hogwarts_xixi'
"""
import pytest


@pytest.fixture(params=["hurry", "hogwarts", "aaaa"], ids=['user1', 'user2', 'user3'])
def login1(request):
    return request.param


def test_cart1(login1):
    print(login1)


@pytest.mark.parametrize("username", ["hurry", "hogwarts"])
def test_cart(username):
    print(f"username : {username}")
