#! /usr/bin/env python
# coding:utf-8
# Filename:onekey_install_ubuntu.py

print "\nThis is oppih's first project based on Python!\
\n\nAnd it is desighed to make Ubuntu installations easier and faster!\
\n\nEnjoy && Happy Hacking!  :)\n"

import os
import sources_update,lang_install,pkg_install,extd_pkg

sources_update.source_update()
lang_install.lang()
pkg_install.pkg()
extd_pkg.extd()

os.system("sudo apt-get update && sudo apt-get dist-upgrade")
os.system("sudo apt-get clean")#执行清理

#从师父那里看来的关于前期配置的：
#sudo apt-get install ubuntu-minimal #会安装一些Python、认证之类的软件包
#sudo apt-get install language-pack-en #安装英文环境，这步会产生locale
#先更新语言环境然后在考虑full-upgrade？

