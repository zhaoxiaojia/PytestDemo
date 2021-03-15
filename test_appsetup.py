#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/3/15 15:28
# @Author  : Coco
# @Site    : SH #5-389
# @File    : test_appsetup.py
# @Email   : chao.li@amlogic.com
# @Software: PyCharm

import pytest


class App:
    def __init__(self, smtp_connection):
        self.smtp_connection = smtp_connection


# 注意：app fixture声明了作用域module，并使用了同样是module作用域的smtp_connection。如果smtp_connection是session的作用域，这个示例依然是有效的：fixture可以引用作用域更广泛的fixture，但是反过来不行，比如session作用域的fixture不能引用一个module作用域的fixture
@pytest.fixture(scope="module")
def app(smtp_connection):
    return App(smtp_connection)


def test_smtp_connection_exists(app):
    assert app.smtp_connection
