#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/3/15 16:38
# @Author  : Coco
# @Site    : SH #5-389
# @File    : test_setenv.py
# @Email   : chao.li@amlogic.com
# @Software: PyCharm


import os
import pytest


# 因为使用了usefixtures, 所以cleandir会在每个测试用例之前被调用，就好像为这些测试指定了 "cleandir"入参一样
@pytest.mark.usefixtures("cleandir")
class TestDirectoryInit:
    def test_cwd_starts_empty(self):
        assert os.listdir(os.getcwd()) == []
        with open("myfile", "w") as f:
            f.write("hello")

    def test_cwd_again_starts_empty(self):
        assert os.listdir(os.getcwd()) == []
