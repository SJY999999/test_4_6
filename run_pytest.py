# -*- coding: utf-8 -*-
# Time : 2022/4/5 11:51
# Author : SJY
# File : run_pytest.py
# Desc :
import pytest
import subprocess    #打开报告，-h本地， shell指用终端打开

pytest.main()
subprocess.call('allure generate ./result/temp -o ./result./report --clean',shell=True)
#执行生成报告（allure）的命令，转化成html。temp指报告在temp中，report指转成html后放在report中，clear是放前清除一下，通过shell执行
subprocess.call('allure open -h 127.0.0.1 -p 8883 ./result/report',shell=True)
#执行生成报告（allure）的命令







