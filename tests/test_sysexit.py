#!/usr/bin/env python
# _*_coding:utf-8 _*_
# @Time :2021/3/13 14:39
# @Author :Coco
# @FileName: test_sysexit.py

# @Software: PyCharm

import pytest


def f():
    # 使用raise 可以用来判断代码是否抛出了异常
    raise SystemExit(1)


def test_mytest():
    with pytest.raises(SystemExit):
        f()
