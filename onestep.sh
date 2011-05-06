#!/usr/bin/bash

echo "\nThis is oppih's first project based on Python!\
\n\nAnd it is desighed to make Ubuntu installations easier and faster!\
\n\nEnjoy && Happy Hacking!  :)\n"


#Configuration
#TODO check if the network supports IPv6
sudo cp ./config/ipv6_hosts /etc/hosts

#更新软件源
sudo cp /etc/apt/sources.list /etc/apt/sources.list_backup
sudo cp ./sources_list/ipv6_edu /etc/apt/sources.list
#./test_envi/sources.list

sudo apt-get update

#安装语言支持
#TODO语言包需要求证，中英文均有必要安装
#TODO修改HOME文件夹中的文件名称为英文，向tweak取经学习

#安装一些常用软件
sudo apt-get install xpdf-chinese-simplified xpdf-chinese-traditional poppler-data \
nautilus-open-terminal nautilus-gksu \
unrar p7zip-rar p7zip-full cabextract \
build-essential autoconf automake1.9 cvs subversion
#TODO多媒体是不是在tweak中安装mplayer、VLC等软件时能够搞定？或者直接采用复制方式搞定？

sudo dpkg -i ./debs/install_flash_player_10_linux.deb
# Need more packakes

#启动图形工具来做设置，语言支持和硬件驱动
#language support:
/usr/bin/gnome-language-selector
#hardware drivers:
/usr/bin/jockey-gtk

#更新系统，执行清理
sudo apt-get update && sudo apt-get dist-upgrade
sudo apt-get clean

echo "It's Done! :)"
