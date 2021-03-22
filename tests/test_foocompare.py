#!/usr/bin/env python
# _*_coding:utf-8 _*_
# @Time :2021/3/13 17:35
# @Author :Coco
# @FileName: test_foocompare.py

# @Software: PyCharm

class Foo:
    def __init__(self, val):
        self.val = val

    def __eq__(self, other):
        return self.val == other.val


def test_compare():
    f1 = Foo(1)
    f2 = Foo(2)
    assert f1 == f2
