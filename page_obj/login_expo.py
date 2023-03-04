'''


'''
from base.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium import webdriver


class LoginPag(BasePage):
    # 核心元素
    url = 'https://b2b.sit.expowh.com/user/login.htm'
    user = (By.NAME, 'loginName')
    password = (By.NAME, 'loginPwd')
    login_button = (By.ID, 'userForm')
    v_code = (By.NAME, 'validCode2')
    na = (By.XPATH, 'name')

    def  __err_msg1(self):
        return (By.XPATH, '//div[@class="username_box username_err"]')

    # 核心业务

    def login(self, d):
        self.open_u()
        self.input_(self.user, d['user_'])
        self.input_(self.password, d['password'])
        self.input_(self.v_code, '8888')
        self.click(self.login_button)

    # 获取错误信息
    def get_err_msg(self):
        return self.ele_txt(self.__err_msg1())

#
#     d={'user_':"13188888886","password":'123456'}
#     driver=webdriver.Chrome()
#     lp=LoginPag(driver)
#     lp.login(d)
#     lp.wait(3)
#     print(lp.get_err_msg())
