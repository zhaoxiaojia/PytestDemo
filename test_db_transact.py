#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/3/15 17:10
# @Author  : Coco
# @Site    : SH #5-389
# @File    : test_db_transact.py
# @Email   : chao.li@amlogic.com
# @Software: PyCharm

import pytest


class DB(object):
    def __init__(self):
        self.intransaction = []

    def begin(self, name):
        self.intransaction.append(name)

    def rollback(self):
        self.intransaction.pop()


@pytest.fixture(scope="module")
def db():
    return DB()

'''
在class里定义的fixture transact标记了autouse为True，表示这个class里的所有测试函数无需任何其他声明就会自动的使用transact这个fixture。
'''
class TestClass(object):
    @pytest.fixture(autouse=True)
    def transact(self, request, db):
        db.begin(request.function.__name__)
        yield
        db.rollback()

    def test_method1(self, db):
        assert db.intransaction == ["test_method1"]

    def test_method2(self, db):
        assert db.intransaction == ["test_method2"]
