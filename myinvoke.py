#!/usr/bin/env python
# _*_coding:utf-8 _*_
# @Time :2021/3/13 16:13
# @Author :Coco
# @FileName: myinvoke.py

# @Software: PyCharm

'''
调用pytest.main() 会导入你的测试用例以及所使用的模块，因为Python存在模块导入的缓存机制，如果多次调动pytest.main()，后续的调动也不会在刷新这些导入的资源。因此，不建议在同进程中多次调用pytest.main()(比如重新运行测试)
'''
import pytest


class MyPlguin(object):
    def pytest_sessionfinish(self):
        print('*** test run reporting finishing ***')


pytest.main(["-x", "test_1.py"], plugins=[MyPlguin()])
