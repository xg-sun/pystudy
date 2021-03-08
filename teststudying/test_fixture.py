# import pytest
# import datetime

def test_search():
    print("搜索")

# @pytest.mark.usefixtures("get_username")
# @pytest.mark.usefixtures("login")
def test_cart(get_username):
    print("购物")

# @pytest.mark.usefixtures("login")
def test_order():
    print("下单")

