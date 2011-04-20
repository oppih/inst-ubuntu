#! /usr/bin/env python
# coding:utf-8
# Filename:extd_pkg.py

import os
import time

def extd():

    flag = "-"
    width = 25
    print flag * width + "\n" + flag * width
    print "以下安装扩展软件"
    print flag * width + "\n" + flag * width
    time.sleep(2)

    """
    print "安装中文输入法ibus，并设置为默认输入法："
    os.system("sudo apt-get install ibus ibus-pinyin ibus-gtk")#中文输入法ibus
    os.system("im-switch -s ibus")

    flag = "-"
    width = 25
    print flag * width
    print "注销后重新登录。重新登录后可能需要修改ibus的配置，手动添加ibus-pingyin引擎"##这里还真是需要测试过才能知道结果呢
    time.sleep(2)
    """

    print "\n\n以下安装配置JAVA环境："#java环境部分需要重新评估
    os.system("sudo apt-get install sun-java6-jre")#JAVA环境,需要确认的是，不能屏蔽输出，因为要同意SUN许可证
    os.system("sudo update-alternatives --config java")#设置当前默认的java解释器
    os.system("sudo apt-get install vim-full")#安装VIM完整版，已知此软件安装命令在9.10中发生改变

if __name__ == '__main__':
    extd()
