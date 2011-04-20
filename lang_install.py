#! /usr/bin/env python
# coding:utf-8
# Filename:lang_install.py

import os
import time

def lang():

    flag = "-"
    width = 20
    print flag * width + "\n" + flag * width
    print "以下安装中文语言支持"
    print flag * width + "\n" + flag * width
    time.sleep(2)

    os.system("sudo apt-get install language-pack-zh language-pack-gnome-zh language-support-input-zh language-support-fonts-zh language-support-translations-zh language-support-extra-zh")
    #os.system("sudo apt-get install language-pack-zh language-pack-zh-base language-pack-gnome-zh language-pack-gnome-zh-base")
    #os.system("sudo apt-get install language-pack-en language-pack-en-base language-pack-gnome-en language-pack-gnome-en-base")

    """
也许是下面这些个……上面的是我自己猜测的……
下面的是来自其他程序的，yegle说是自己解析language-support的依赖关系，
还有人说是9.10里面不再以依赖关系来处理语言包，这个就有赖于实际测试了
并且，这个语言包到底是哪些，必须要经过测试才好知道能否有用……
"language-pack-zh "
"language-pack-gnome-zh "
"language-support-input-zh "
此处的input使用的输入法是否会和iBus冲突？
"language-support-fonts-zh "
"language-support-translations-zh "
"language-support-extra-zh"
    """

if __name__ == '__main__':
    lang()

