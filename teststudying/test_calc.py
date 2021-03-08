import sys
import yaml

sys.path.append('..')
# print(sys.path)
import pytest
from pythoncode.Calculator import Calculator

def get_datas():
    with open("./data/calc.yml") as f:
        datas = yaml.safe_load(f)
        # print(datas)
    return (datas['add']['datas'], datas['add']['ids'], datas['div']['datas'], datas['div']['ids'])


class TestCalc:
    datas:list = get_datas()

    # 前置条件
    def setup(self):
        print("开始计算")
        self.calc = Calculator()

    # 后置条件
    def teardown(self):
        print("结束计算")

    # @pytest.mark.search
    @pytest.mark.parametrize("a, b, result",datas[0],ids=datas[1])
    def test_add(self, a, b, result):
        print(f"a = {a}, b = {b}, result = {result}")
        assert result == round(self.calc.add(a, b),4)

    # @pytest.mark.login
    @pytest.mark.parametrize("a,b,result",datas[2],ids=datas[3])
    def test_div(self, a, b, result):
        # calc = Calculator()
        # print(f"a = {a}, b = {b}, result = {result}")
        # assert result == self.calc.div(a, b)
        #
        # with pytest.raises(ZeroDivisionError):
        #     result == self.calc.div(a,b)
        try:
            assert result == self.calc.div(a,b)
        except ZeroDivisionError as erro:
            print(erro)
            pass

