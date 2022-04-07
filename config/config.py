# -*- coding: utf-8 -*-
# Time : 2022/4/2 13:13
# Author : SJY
# File : config.py
# Desc :配置信息/路径
import os
root_path=os.path.dirname(os.path.dirname(__file__))


url='http://139.224.113.59/zentao/user-login-L3plbnRhby8=.html'
driver_path=root_path+r'/driver/msedgedriver.exe'
case_path=root_path+r'/test_demo'
# report_path=root_path+r'/report'
file_path=root_path+r'/data/test.xlsx'
system_version='1.2'
log_file=root_path+r'/log/log.txt'