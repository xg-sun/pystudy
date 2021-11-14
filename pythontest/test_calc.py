# import sys
import yaml
# sys.path.append('..')
# print(sys.path)
import pytest
from pythoncode.Calculator import Calculator


def get_datas(name,level):
    with open("../data/calc.yml", encoding='utf-8') as f:
        all_datas = yaml.safe_load(f)
        datas = all_datas[name][level]['datas']
        ids = all_datas[name][level]['ids']
        return (datas, ids)


class TestCalc:
    add_P0_data = get_datas('add','P0')
    add_P11_data = get_datas('add','P1_1')
    add_P12_data = get_datas('add', 'P1_2')
    add_P2_data = get_datas('add', 'P2')

    div_P0_data = get_datas('div', 'P0')
    div_P1_data = get_datas('div', 'P1')

    def setup(self):
        print("开始计算")
        self.calc = Calculator()

    def teardown(self):
        print("结束计算")

    def teardown_class(self):
        with open("../data/calc.yml", encoding='utf-8') as f:
            f.close()

    # @pytest.mark.parametrize("a, b, result",[(1,1,2),(0.2,0.3,0.5),(0.02,0.01,0.03)])
    @pytest.mark.parametrize("a,b,result",add_P0_data[0],ids=add_P0_data[1])
    def test_add_P0(self, a, b, result):
        print(f"a = {a}, b = {b}, result = {result}")
        assert result == self.calc.add(a, b)

    @pytest.mark.parametrize("a,b,result", add_P11_data[0], ids=add_P11_data[1])
    def test_add_P11(self, a, b, result):
        print(f"a = {a}, b = {b}, result = {result}")
        assert result == self.calc.add(a, b)

    @pytest.mark.parametrize("a,b,result", add_P12_data[0], ids=add_P12_data[1])
    def test_add_p12(self, a, b, result):
        print(f"a = {a}, b = {b}, result = {result}")
        assert result == self.calc.add(a, b)

    @pytest.mark.parametrize("a,b,result", add_P2_data[0], ids=add_P2_data[1])
    def test_add_p2(self, a, b, result):
        print(f"a = {a}, b = {b}, result = {result}")
        assert result == self.calc.add(a, b)

    # @pytest.mark.parametrize("a,b,result",[("a",1,"TypeError"),(5,0,"ZeroDivisionError")])
    @pytest.mark.parametrize("a,b,result", div_P0_data[0], ids=div_P0_data[1])
    def test_div_P0(self, a, b, result):
        try:
            assert result == self.calc.div(a,b)
        except ZeroDivisionError as err1:
            print("除数0异常")
        except TypeError as err2:
            print("类型错误")

        # with pytest.raises(TypeError) as e:
        #    self.calc.div(a,b)

    @pytest.mark.parametrize("a,b,result", div_P1_data[0], ids=div_P1_data[1])
    def test_div_P0(self, a, b, result):
        try:
            assert result == self.calc.div(a,b)
        except ZeroDivisionError as err1:
            print("除数0异常")
        except TypeError as err2:
            print("类型错误")