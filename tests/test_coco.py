#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/3/16 14:21
# @Author  : Coco
# @Site    : SH #5-389
# @File    : test_coco.py
# @Email   : chao.li@amlogic.com
# @Software: PyCharm

import pytest
import random


@pytest.mark.flaky(reruns=5)
def test_coco():
    print(f'version : {pytest.__version__}')
    num = random.randrange(0, 5)
    print(num)
    assert num > 3
