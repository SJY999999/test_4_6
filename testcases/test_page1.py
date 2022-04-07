# -*- coding: utf-8 -*-
# Time : 2022/4/2 10:23
# Author : SJY
# File : test_page1.py
# Desc :
from time import sleep
from objectpage.login_page import LoginPage
from data.data import ReadWrite
from log.log import logger
#设置web_pytest_framework为根目录



class TestCases:
    def test_1(self,login):
        '''
        验证有效地用户名和密码成功登录系统
        '''
        print('登录的第一个测试用例')
        self.driver=login
        self.loginpage=LoginPage(self.driver)
        user_list=ReadWrite().excelread('users')
        username=user_list[0][0]
        password=user_list[0][1]
        self.loginpage.input_username(username)
        self.loginpage.input_password(password)
        self.loginpage.click_login()
        sleep(0.5)
        assert '我的地盘 - 禅道' in self.driver.title  #断言
        self.loginpage.click_logout()
        logger.info('有效的用户名和密码成功登录系统')  #日志格式

    # # @unittest.skip('不执行该测试用例')
    # @unittest.skipIf(system_version=='1.2',reason='只有版本号为1.2才执行')
    # def test_2(self):
    #     '''
    #     验证密码为空时登录失败
    #     '''
    #     print('登录的第二个测试用例')
    #     self.loginpage.input_username('shelly')
    #     self.loginpage.click_login()
    #     sleep(0.5)
    #     alert_login=self.driver.switch_to.alert    #浏览器驱动打开弹出框
    #     alert_login.accept()    #点击弹出框的是
    #
