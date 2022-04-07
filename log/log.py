# -*- coding: utf-8 -*-
# Time : 2022/4/4 8:34
# Author : SJY
# File : log.py
# Desc :日志
import logging
from config.config import log_file


#创建日志器
logger=logging.getLogger()
#定义日志器的级别
logger.setLevel(logging.INFO)
#定义处理器的格式
format=logging.Formatter('%(asctime)s %(filename)s[line:%(lineno)d]%(levelname)s %(message)s')
logFile=log_file
#创建处理器
fh=logging.FileHandler(logFile,mode='a',encoding='utf-8')
#设置处理器的级别
fh.setLevel(logging.INFO)
#设置处理器的格式
fh.setFormatter(format)
#把处理器添加到日志器
logger.addHandler(fh)
