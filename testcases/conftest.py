# -*- coding: utf-8 -*-
# Time : 2022/4/5 15:23
# Author : SJY
# File : conftest.py
# Desc :公用的
import pytest
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from config.config import url,driver_path

@pytest.fixture(scope='session')    #传递公共数据用fixture(pytest中)
def login():
    e = Service(executable_path=driver_path)
    driver = webdriver.Edge(service=e)
    driver.maximize_window()
    driver.get(url)
    yield driver    #返回的是driver
    driver.quit()  #退出浏览器


