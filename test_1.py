#!/usr/bin/env python
# _*_coding:utf-8 _*_
# @Time :2021/3/13 15:27
# @Author :Coco
# @FileName: test_1.py

# @Software: PyCharm


import pytest


@pytest.mark.me
def test_a():
    print('这是功能测试项a')


def test_b():
    print('这是功能测试项b')


def test_c():
    print('这是功能测试项c')
