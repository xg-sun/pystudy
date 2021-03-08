import sys
import yaml

sys.path.append('..')
# print(sys.path)
import pytest
from pythoncode.Calculator import Calculator

def get_datas(name,type='int'):
    with open("./data/calcutor.yml") as f:
        all_datas = yaml.safe_load(f)
        # print(all_datas)
    datas = all_datas[name][type]['datas']
    ids = all_datas[name][type]['ids']
    return (datas,ids)

@pytest.fixture()
def get_instance():
    print("开始计算")
    calc:Calculator = Calculator()
    yield calc
    print("结束计算")

@pytest.fixture(params=get_datas('add','int')[0],ids=get_datas('add','int')[1])
def get_datas_with_fixture(request):
    return request.param

def test_param(get_datas_with_fixture):
    print(get_datas_with_fixture)

@pytest.fixture(params=get_datas('div','int')[0],ids=get_datas('div','int')[1])
def get_datas_with_fixture1(request):
    return request.param

def test_param1(get_datas_with_fixture1):
    print(get_datas_with_fixture1)


class TestCalc:
    # datas:list = get_datas()
    add_int_data = get_datas('add','int')
    div_int_data = get_datas('div','int')
    #
    # # 前置条件
    # def setup(self):
    #     print("开始计算")
    #     self.calc = Calculator()
    #
    # # 后置条件
    # def teardown(self):
    #     print("结束计算")

    # @pytest.mark.search
    # @pytest.mark.parametrize("a, b, result",add_int_data[0],ids=add_int_data[1])
    # def test_add(self,get_instance, a, b, result):
    #     print(f"a = {a}, b = {b}, result = {result}")
    #     assert result == round(get_instance.add(a, b),4)

    def test_add(self,get_instance, get_datas_with_fixture):
        f = get_datas_with_fixture
        assert f[2] == round(get_instance.add(f[0], f[1]),4)
    #
    # # @pytest.mark.login
    # @pytest.mark.parametrize("a,b,result",div_int_data[0],ids=div_int_data[1])
    # def test_div(self,get_instance, a, b, result):
    #     # calc = Calculator()
    #     # print(f"a = {a}, b = {b}, result = {result}")
    #     # assert result == self.calc.div(a, b)
    #     #
    #     # with pytest.raises(ZeroDivisionError):
    #     #     result == self.calc.div(a,b)
    #     try:
    #         assert result == get_instance.div(a,b)
    #     except ZeroDivisionError as erro:
    #         print(erro)
    #         pass

    def test_div(self,get_instance, get_datas_with_fixture1):

        f = get_datas_with_fixture1

        try:
            assert f[2] == get_instance.div(f[0],f[1])
        except ZeroDivisionError as erro:
            print(erro)
            pass

