#!/usr/bin/env python
# _*_coding:utf-8 _*_
# @Time :2021/3/13 14:41
# @Author :Coco
# @FileName: test_class.py

# @Software: PyCharm

class TestClass:
    def test_one(self):
        x = 'this'
        assert 'h' in x

    def test_two(self):
        x = 'hello'
        assert hasattr(x, 'check')
