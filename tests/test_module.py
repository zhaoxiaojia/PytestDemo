#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/3/15 10:06
# @Author  : Coco
# @Site    : SH #5-389
# @File    : test_module.py
# @Email   : chao.li@amlogic.com
# @Software: PyCharm
import pytest


# smtpserver = 'mail.python.org'


def test_ehlo(smtp_connection):
    response, msg = smtp_connection.ehlo()
    assert response == 250
    assert b"." in msg
    # assert 0


def test_noop(smtp_connection):
    response, msg = smtp_connection.noop()
    assert response == 250
    # assert 0


@pytest.fixture
def make_customer_record():
    create_records = []

    def _make_custoer_record(name):
        record = {'name': name, 'orders': []}
        create_records.append(record)
        return record

    yield _make_custoer_record
    for record in create_records:
        record.clear()


def test_customer_records(make_customer_record):
    customer_1 = make_customer_record('Lisa')
    customer_2 = make_customer_record('Mike')
    customer_3 = make_customer_record('Meredith')
    print(customer_1)
    print(customer_2)
    print(customer_3)


'''
测试过程中，pytest会保持激活的fixture的数目是最少的，如果有一个参数化的fixture，那么所有使用它的测试用例会首先使用一个实例来执行，直到它完成后才去调用下一个实例。这样做使得应用程序的测试中创建和使用全局状态更为简单
'''


@pytest.fixture(scope="module", params=["mod1", "mod2"])
def modarg(request):
    param = request.param
    print(" SETUP modarg %s" % param)
    yield param
    print(" TEARDOWN modarg %s" % param)


@pytest.fixture(scope="function", params=[1, 2])
def otherarg(request):
    param = request.param
    print(" SETUP otherarg %s" % param)
    yield param
    print(" TEARDOWN otherarg %s" % param)


def test_0(otherarg):
    print(" RUN test0 with otherarg %s" % otherarg)


def test_1(modarg):
    print(" RUN test1 with modarg %s" % modarg)


def test_2(otherarg, modarg):
    print(" RUN test2 with otherarg %s and modarg %s" % (otherarg, modarg))
