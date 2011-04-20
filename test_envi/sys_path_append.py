#! /usr/bin/env python
# coding:utf-8
# Filename:sys_path_append.py

import os,sys

def path_add():
    sys.path.append("./funcfiles")
    import test
    test.prints()

if __name__ == '___main__':
    path_add()

