"""
__author__ = 'hogwarts_xixi'
"""
import logging

"""
练习题一：使用 Fixture
- 使用 fixture 提供 calc 对象
- 使用 fixture实现：用例执行之前打印【开始计算】，之后【结束计算】
- 当前模块所有用例执行完成之后，打印【测试结束】
- 每条用例添加测试日志，并将日志打印输出到logs/ <日期_时间>.log 文件中
"""

import pytest
import yaml
import sys
sys.path.append('..')

from pythoncode.Calculator import Calculator


# 使用with 读取yaml 文件
def get_data(level):
    with open("../datas/data.yml", encoding='utf-8') as f:
        # pip install pyyaml
        datas = yaml.safe_load(f)
        add_datas = datas.get("add")
        return (add_datas.get(level).get("datas"), add_datas.get(level).get("ids"))


class TestCalculator:
    add_P0_data, add_P0_ids = get_data("P0")
    add_P11_data, add_P11_ids = get_data("P1_1")
    add_P12_data, add_P12_ids = get_data("P1_2")
    add_P2_data, add_P2_ids = get_data("P2")

    @pytest.mark.P0
    @pytest.mark.parametrize("a,b,expect", add_P0_data, ids=add_P0_ids)
    def test_case_p0(self, a, b, expect, get_calc):
        print(a, b, expect)
        logging.info(f"输入数据：{a},{b} ，期望结果：{expect}")
        assert expect == get_calc.add(a, b)

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
