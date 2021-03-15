#!/usr/bin/env python
# _*_coding:utf-8 _*_
# @Time :2021/3/13 17:56
# @Author :Coco
# @FileName: test_smtpsimple.py

# @Software: PyCharm


import pytest


# @pytest.fixture(scope='moudle') 该设置 每个测试模块都会调用一次smtp_connection的fixture函数（默认情况下每个测试函数都调动一次）。因此，一个测试模块中的对个测试函数将使用同一个同样的smtp_connection实例，从而节省了反复创建的时间。scope可能的值为：function，class，module，package和session
# @pytest.fixture
# def smtp_connection():
#     import smtplib
#     return smtplib.SMTP("smtp.gmail.com", 587, timeout=5)


# 这里 test_ehlo需要smtp_connection 这个fixture的返回，pytest会在@pytest.fixture的fixture中查找调用名为smtp_connection的fixture
def test_ehlo(smtp_connection):
    response, msg = smtp_connection.ehlo()
    print('coco',response)
    assert response == 250
    assert 0 # 用于调试


'''
测试回显中可以看出测试函数调用了smtp_connection，这是由fixture函数创建的smtplib.SMTP()的一个实例。该函数在我们故意添加的assert0处失败

· pytest找到以test_作为前缀的测试用例test_ehlo 该测试函数有一个名为smtp_connection的入参。而在fixture函数中存在一个名为smtp_connection的fixture
· smtp_connection()被调用来创建一个实例
· test_ehlo(<smtp_connection实例>)被调用并在最有一行因为断言失败。
'''
