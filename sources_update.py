#! usr/bin/env python
# coding:utf-8
# Filename:sources_upate.py

import os
import time

def source_update():

    flag = "-"
    width = 25
    print flag * width + "\n" + flag * width
    print "以下更新源地址列表为教育网IPv6适用"
    print "默认将对系统自带源列表进行备份，如果修改源失败的话，使用以下命令恢复至默认的源地址文件：\nsudo cp /etc/apt/sources.list_backup /etc/apt/sources.list"
    print flag * width + "\n" + flag * width
    time.sleep(2)

    """
#备份源列表，已经测试通过，平时测试时不启用
#如果修改源失败的话，使用以下命令恢复至默认的源地址文件：
#sudo cp /etc/apt/sources.list_backup /etc/apt/sources.list
#os.system("cp /etc/apt/sources.list /etc/apt/sources.list_backup")
    """
#[!!!]用于编写导入自己需要用的源地址文件才好，需要做版本测试，参考其他；要不先做的简单一些，就针对单一版本，以后改进
    os.system("cp /etc/apt/sources.list /etc/apt/sources.list_backup")
    os.system("sudo cp ./sources_list/ipv6_edu /etc/apt/sources.list")#./test_envi/sources.list


if __name__ == '__main__':
    source_update()

