"""
__author__ = 'hogwarts_xixi'
"""
import logging
from time import sleep

import allure
import pytest
import yaml

"""
练习题二：
- 使用fixture实现参数化
- 定义执行顺序，顺序为
    先add方法 P1_1 和 P1_2级别的用例
    其次执行P0 级别
    然后执行 相除方法的用例
    最后执行add 方法P2）
    add 用例 （P1_1>P1_2>P0）> div 用例 >  add 用例（P2）
"""


# 使用with 读取yaml 文件
def get_data(level):
    # 路径 是相对于 测试用例所在的路径，IDE里联想不出来，
    with open("../datas/data.yml", encoding='utf-8') as f:
        # pip install pyyaml
        datas = yaml.safe_load(f)
        add_datas = datas.get("add")
        return (add_datas.get(level).get("datas"), add_datas.get(level).get("ids"))


@pytest.fixture(params=get_data("P0")[0], ids=get_data("P0")[1])
def get_addP0_data(request):
    # 固定写法，request
    return request.param


@allure.feature("测试计算器功能")
class TestCalculator:
    # add_P0_data, add_P0_ids = get_data("P0")
    # add_P11_data, add_P11_ids = get_data("P1_1")
    # add_P12_data, add_P12_ids = get_data("P1_2")
    # add_P2_data, add_P2_ids = get_data("P2")

    @pytest.mark.P0
    @pytest.mark.run(order=1)
    @allure.story("相加功能")
    # @pytest.mark.parametrize("a,b,expect", add_P0_data, ids=add_P0_ids)
    def test_case_p0(self, get_addP0_data, get_calc):
        sleep(1)
        print(get_addP0_data)
        a = get_addP0_data[0]
        b = get_addP0_data[1]
        expect = get_addP0_data[2]
        # print(a, b, expect)
        logging.info(f"输入数据：{a},{b} ，期望结果：{expect}")
        allure.attach.file("/Users/juanxu/Downloads/logo帽子.jpg",
                           name="图片",
                           attachment_type=allure.attachment_type.JPG,
                           extension=".jpg")
        assert expect == get_calc.add(a, b)

    @pytest.mark.second
    def test_case1_add(self, get_calc):
        assert 2 == get_calc.add(1, 1)

    @pytest.mark.run(order=-1)
    def test_case2_add(self, get_calc):
        assert 0.01 == get_calc.add(-0.01, 0.02)

    @pytest.mark.run(order=-2)
    def test_case3_add(self, get_calc):
        assert 10.02 == get_calc.add(10, 0.02)

#  @pytest.mark.parametrize("a,b,expect", add_P11_data, ids=add_P11_ids)
#  def test_case_p11(self, a, b, expect):
#      print(a, b, expect)
#      assert expect == self.calc.add(a, b)
#
#  @pytest.mark.P1
#  @pytest.mark.parametrize("a,b,expect", add_P12_data, ids=add_P12_ids)
#  def test_case_p12(self, a, b, expect):
#      with pytest.raises(eval(expect)) as e:
#          result = self.calc.div(a, b)
#      # 期望的异常与实际异常比对
#      assert expect == e.typename
#
#  @pytest.mark.P2
#  @pytest.mark.parametrize("a,b,expect", add_P2_data, ids=add_P2_ids)
#  def test_case_p2(self, a, b, expect):
#      with pytest.raises(eval(expect)) as e:
#          result = self.calc.div(a, b)
#
#      # 期望的异常与实际异常比对
#      assert expect == e.typename
#
