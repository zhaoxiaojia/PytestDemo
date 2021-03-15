#!/usr/bin/env python
# _*_coding:utf-8 _*_
# @Time :2021/3/13 17:37
# @Author :Coco
# @FileName: conftest.py

# @Software: PyCharm

import pytest
import smtplib
import os
from test_foocompare import Foo


# 钩子名称固定
def pytest_assertrepr_compare(op, left, right):
    if isinstance(left, Foo) and isinstance(right, Foo) and op == '==':
        return ['Compare Foo isinstance', ' val {} != {}'.format(left.val, right.val), 'coco is handsome']


# @pytest.fixture(scope='module')
# def smtp_connection():
#     smtp_connection = smtplib.SMTP("smtp.gmail.com", 587, timeout=5)
#     yield smtp_connection
#     # 另一种写法
#     # with smtplib.SMTP("smtp.gmail.com") as smtp_connection:
#     #     yield smtp_connection
#     print('teardown smtp')
#     smtp_connection.close()


# 另一种处理teardown的方法
# @pytest.fixture(scope='module')
# def smtp_connection(request):
#     '''
#     可以注册多个完成函数
#     无论fixture的代码是否存在异常，addfinalizer注册的函数都会被调用，这样即使出现了异常，也可以正确的关闭那些在fixture中创建的资源
#     :param request:
#     :return:
#     '''
#     smtp_connection = smtplib.SMTP("smtp.gmail.com", 587, timeout=5)
#
#     def fin():
#         print('teardown smtp_connection')
#         smtp_connection.close()
#
#     request.addfinalizer(fin)
#     return smtp_connection

# 使用fixture获取测试对象的上下文
# @pytest.fixture(scope='module')
# def smtp_connection(request):
#     server = getattr(request.module, "smtpserver", "smtp.gmail.com")
#     smtp_connection = smtplib.SMTP(server, 587, timeout=5)
#     yield smtp_connection
#     print("finalizing %s (%s)" % (smtp_connection, server))
#     smtp_connection.close()


# fixture 参数化 替代上下文获取
@pytest.fixture(scope='module', params=['smtp.gmail.com', 'mail.python.org'])
def smtp_connection(request):
    smtp_connection = smtplib.SMTP(request.param, 587, timeout=5)
    yield smtp_connection
    print("finalizing %s" % smtp_connection)
    smtp_connection.close()


@pytest.fixture
def cleandir():
    newpath = tempfile.mkdtemp()
    os.chdir(newpath)  # 用于改变当前工作目录到指定的路径。
