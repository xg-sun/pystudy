from decimal import Decimal, ROUND_HALF_UP

import allure
import pytest
import yaml

from pythoncode.Calculator import Calculator


# 使用with 读取yaml 文件
def get_data(level):
    with open("./datas/data.yml", encoding='utf-8') as f:
        # pip install pyyaml
        datas = yaml.safe_load(f)
        add_datas = datas.get("add")
        return (add_datas.get(level).get("datas"), add_datas.get(level).get("ids"))


# def test_getdata():
#     print(get_data("P0"))
#     print(get_data("P1_1"))
#     print(get_data("P1_2"))
#     print(get_data("P2"))


class TestCalculator:
    add_P0_data, add_P0_ids = get_data("P0")
    add_P11_data, add_P11_ids = get_data("P1_1")
    add_P12_data, add_P12_ids = get_data("P1_2")
    add_P2_data, add_P2_ids = get_data("P2")

    def setup_class(self):
        self.calc = Calculator()

    def setup(self):
        print("开始计算")

    def teardown(self):
        print("结束计算")

    def teardown_class(self):
        print("结束测试")

    @pytest.mark.P0
    @pytest.mark.parametrize("a,b,expect", add_P0_data, ids=add_P0_ids)
    def test_case_p0(self, a, b, expect):
        print(a, b, expect)
        assert expect == self.calc.add(a, b)

    @pytest.mark.parametrize("a,b,expect", add_P11_data, ids=add_P11_ids)
    def test_case_p11(self, a, b, expect):
        print(a, b, expect)
        assert expect == self.calc.add(a, b)

    @pytest.mark.P1
    @pytest.mark.parametrize("a,b,expect", add_P12_data, ids=add_P12_ids)
    def test_case_p12(self, a, b, expect):
        with pytest.raises(eval(expect)) as e:
            result = self.calc.div(a, b)
        # 期望的异常与实际异常比对
        assert expect == e.typename

    @pytest.mark.P2
    @pytest.mark.parametrize("a,b,expect", add_P2_data, ids=add_P2_ids)
    def test_case_p2(self, a, b, expect):
        with pytest.raises(eval(expect)) as e:
            result = self.calc.div(a, b)

        # 期望的异常与实际异常比对
        assert expect == e.typename
    #
    # def test_case1_add(self):
    #     assert 2 == self.calc.add(1, 1)
    #
    # def test_case2_add(self):
    #     assert 0.01 == self.calc.add(-0.01, 0.02)
    #
    # def test_case3_add(self):
    #     assert 10.02 == self.calc.add(10, 0.02)
    #
    # def change_to_decimal(self, num):
    #     # 四舍五入的运算模式
    #     return Decimal(f"{num}").quantize(Decimal('0.0000'), rounding=ROUND_HALF_UP)
    #
    # # 浮点数计算 Decimal 类型
    # def test_case4_float1(self):
    #     result = self.calc.add(Decimal("0.1"), Decimal("0.2"))
    #     r = self.change_to_decimal(result)
    #     assert r == self.change_to_decimal(0.3)
    #
    # def test_case5_float(self):
    #     result = self.calc.add(0.1, 0.2)
    #     assert 0.3 == round(result, 4)
    #
    # @pytest.mark.parametrize('a,b,errortype', [
    #     ("*&", 0.2, "TypeError"), (1, 0, "ZeroDivisionError")])
    # def test_case6_specl(self, a, b, errortype):
    #     # try:
    #     #     # assert result_expect == self.calc.add(a, b)
    #     #     1/0
    #     # except (TypeError,ZeroDivisionError):
    #     #     print("类型错误")
    #     with pytest.raises(eval(errortype)) as e:
    #         result = self.calc.div(a, b)
    #
    #     # 期望的异常与实际异常比对
    #     assert errortype == e.typename
