#! /usr/bin/env python
# coding:utf-8
# Filename:singlefile_install_ubuntu.py

print "\nThis is oppih's first project based on Python!\
\n\nAnd it is desighed to make Ubuntu installations easier and faster!\
\n\nEnjoy && Happy Hacking!  :)\n"

import os
import time

#Configuration
os.system("sudo cp ./config/ipv6_hosts /etc/hosts")

flag = "-"
width = 50

print flag * width + "\n" + flag * width + "\n以下更新源地址列表为教育网IPv6适用\n默认将对系统自带源列表进行备份，如果修改源失败的话，使用以下命令恢复至默认的源地址文件：\nsudo cp /etc/apt/sources.list_backup /etc/apt/sources.list\n" + flag * width + "\n" + flag * width

time.sleep(2)

#更新软件源
os.system("sudo cp /etc/apt/sources.list /etc/apt/sources.list_backup")
os.system("sudo cp ./sources_list/ipv6_edu /etc/apt/sources.list")#./test_envi/sources.list

os.system("sudo apt-get update && sudo apt-get dist-upgrade -y --force-yes")

"""
#安装语言支持
os.system("sudo apt-get install language-pack-zh language-pack-gnome-zh language-support-input-zh language-support-fonts-zh language-support-translations-zh language-support-extra-zh")
#TODO语言包需要求证，中英文均有必要安装
#TODO修改HOME文件夹中的文件名称为英文，向tweak取经学习
"""

#安装一些常用软件
os.system("sudo apt-get install xpdf-chinese-simplified xpdf-chinese-traditional poppler-data \
nautilus-open-terminal nautilus-gksu \
unrar p7zip-rar p7zip-full cabextract \
build-essential autoconf automake1.9 cvs subversion")
#TODO多媒体是不是在tweak中安装mplayer、VLC等软件时能够搞定？或者直接采用复制方式搞定？

os.system("sudo dpkg -i ./debs/install_flash_player_10_linux.deb")

#启动图形工具来做设置，语言支持和硬件驱动
#language support:
os.system("/usr/bin/gnome-language-selector")
#hardware drivers:
os.system("/usr/bin/jockey-gtk")

#更新系统，执行清理
os.system("sudo apt-get update && sudo apt-get dist-upgrade")
os.system("sudo apt-get clean")
