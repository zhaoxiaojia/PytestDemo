#!/usr/bin/env python
# _*_coding:utf-8 _*_
# @Time :2021/3/13 14:35
# @Author :Coco
# @FileName: test_simple.py

# @Software: PyCharm


def func(x):
    return x + 1


def test_answer():
    assert func(3) == 5
