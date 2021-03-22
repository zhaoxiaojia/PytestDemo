#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/3/15 14:22
# @Author  : Coco
# @Site    : SH #5-389
# @File    : test_ids.py
# @Email   : chao.li@amlogic.com
# @Software: PyCharm

import pytest

# pytest 会创建一个基于参数名的字符串，可以通过ids关键字来自定义一个字符串来表示测试ID:
@pytest.fixture(params=[0, 1], ids=["spam", "ham"])
def a(request):
    return request.param


def test_a(a):
    pass


def idfn(fixture_value):
    if fixture_value == 0:
        return "eggs"
    else:
        return None


@pytest.fixture(params=[0, 1], ids=idfn)
def b(request):
    return request.param


def test_b(b):
    pass
