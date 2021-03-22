#!/usr/bin/env python
# _*_coding:utf-8 _*_
# @Time :2021/3/13 16:53
# @Author :Coco
# @FileName: test_assert1.py

# @Software: PyCharm
import pytest


def f():
    return 3


def test_function():
    assert f() == 4


def test_comment():
    assert 5 % 2 == 0, "Value was odd,should be even"


def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        1 / 0


def test_recusion_depth():
    # 访问异常的确切信息
    with pytest.raises(RuntimeError) as excinfo:
        def f():
            f()

        f()
    print('coco', excinfo.value)
    assert 'Maximum recursion' in str(excinfo.value)


def myfunc():
    raise ValueError('Exception 123 raised')


def test_match():
    with pytest.raises(ValueError, match=r'.* 123 .*'):
        myfunc()


# 使用pytest 更适合测试自己的代码故意引发的异常
def test_1():
    pytest.raises(ZeroDivisionError, lambda x: x / 0, 1)


@pytest.mark.xfail(raises=ZeroDivisionError)
def test_2():
    f()
