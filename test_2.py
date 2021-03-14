#!/usr/bin/env python
# _*_coding:utf-8 _*_
# @Time :2021/3/13 15:29
# @Author :Coco
# @FileName: test_2.py

# @Software: PyCharm

import pytest


def test_aa():
    print('这是煲机测试项aa')


def test_bb():
    print('这是煲机测试项bb')


@pytest.mark.you
def test_cc():
    print('这是煲机测试项cc')
