#! /usr/bin/env python
# coding:utf-8
# Filename:pkg_install.py

import os
import time

def pkg():

    flag = "-"
    width = 70
    print flag * width + "\n" + flag * width
    print "以下安装常用软件，包括文档查看、端管理设置、压缩解压工具、基础编译程序及版本工具"
    print flag * width + "\n" + flag * width
    time.sleep(2)

    os.system("sudo apt-get install xpdf-chinese-simplified xpdf-chinese-traditional poppler-data \
nautilus-open-terminal nautilus-gksu \
unrar p7zip-rar p7zip-full cabextract \
build-essential autoconf automake1.9 cvs subversion")



    """
大面积注释………………
    os.system("sudo apt-get install xpdf-chinese-simplified xpdf-chinese-traditional poppler-data")#中文文档查看
    os.system("sudo apt-get install nautilus-open-terminal nautilus-gksu")#终端管理设置
    os.system("sudo apt-get install unrar p7zip-rar p7zip-full cabextract")#压缩解压工具
    os.system("sudo apt-get install build-essential autoconf automake1.9 cvs subversion")#安装基础编译程序及版本工具


下面提供的是目前教育网内还不是良好支持的多媒体功能，需要重新评估

    os.system("sudo wget http://www.medibuntu.org/sources.list.d/lucid.list -O /etc/apt/sources.list.d/medibuntu.list")
    os.system("wget -q http://packages.medibuntu.org/medibuntu-key.gpg -O- | sudo apt-key add -")
    os.system("sudo apt-get update && sudo apt-get install medibuntu-keyring && sudo apt-get update")

    os.system("sudo wget http://ubuntu:ubuntuftp@ftp.ubuntu.org.cn/home/dbzhang800/wiki/install_flash_player_10_linux.deb")
    os.system("sudo dpkg -i install_flash_player_10_linux.deb")
    """
    os.system("sudo apt-get install libxine1-ffmpeg libxine1-all-plugins libxine1-plugins w32codecs libstdc++5")
    os.system("sudo apt-get install mplayer mplayer-fonts mozilla-mplayer")

if __name__ == '__main__':
    pkg()
