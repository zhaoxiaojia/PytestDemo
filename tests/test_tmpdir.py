#!/usr/bin/env python
# _*_coding:utf-8 _*_
# @Time :2021/3/13 14:47
# @Author :Coco
# @FileName: test_tmpdir.py

# @Software: PyCharm
import time

'''
pytest提供Builtin fixtures/function arguments 来创建任意的资源，比如一个具有唯一的临时文件

如果函数的签名中（函数签名包括函数的参数和返回值，以及参数的封送顺序等等）包含参数tempdir，pytest就会在执行测试用例之前查找并调用特定的fixture所需的资源,。在本例中，pytest会创建一个unique-per-test-invocation临时文件夹
'''


def test_needsfiles(tmpdir):
    print('coco',tmpdir)
    assert 0
