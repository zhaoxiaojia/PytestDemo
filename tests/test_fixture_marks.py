#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/3/15 14:45
# @Author  : Coco
# @Site    : SH #5-389
# @File    : test_fixture_marks.py
# @Email   : chao.li@amlogic.com
# @Software: PyCharm

import pytest

@pytest.fixture(params=[0,1,pytest.param(2,marks=pytest.mark.skip)])
def data_set(request):
    return request.param

def test_data(data_set):
    pass
