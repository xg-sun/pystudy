import pytest


@pytest.fixture()
def login(pytestconfig):
    result = pytestconfig.getini("log_cli")
    return result


def test_case(login):
    print(login)
