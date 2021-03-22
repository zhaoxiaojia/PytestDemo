#!/usr/bin/env python
# _*_coding:utf-8 _*_
# @Time :2021/3/13 15:40
# @Author :Coco
# @FileName: test_example.py

# @Software: PyCharm

import pytest


@pytest.fixture
def error_fixture():
    assert 0


def test_ok():
    print('ok')


def test_fail():
    assert 0


def test_skip():
    pytest.skip('Skipping this test')


def test_xfail():
    pytest.xfail('xFailing this test')


@pytest.mark.xfail(reason="always xfail")
def test_xpass():
    pass


def test_function(record_xml_arrtibute):
    record_xml_arrtibute("assertions", "REQ-1234")
    record_xml_arrtibute("classname", "custom_classname")
    print("Hello World")
    assert True
