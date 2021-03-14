#!/usr/bin/env python
# _*_coding:utf-8 _*_
# @Time :2021/3/13 17:37
# @Author :Coco
# @FileName: conftest.py

# @Software: PyCharm


from test_foocompare import Foo


# 钩子名称固定
def pytest_assertrepr_compare(op, left, right):
    if isinstance(left, Foo) and isinstance(right, Foo) and op == '==':
        return ['Compare Foo isinstance', ' val {} != {}'.format(left.val, right.val), 'coco is handsome ']
