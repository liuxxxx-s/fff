'''
    二次封装
    基类：工具类、将常用的 与项目适用的相关函数，进行二次封装，自定义，便于测试


    常用项：
        访问 url
        元素定位
        输入
        点击
        退出
        等待
        。。。。。。
'''
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
import ddddocr

class BasePage:

    def __init__(self, driver):
        self.driver = driver

    # 访问url
    def open_u(self):
        self.driver.get(self.url)
        self.driver.maximize_window()

    # 元素定位
    def locator(self, loc):

        return self.driver.find_element(*loc)

    # 多个元素定位
    def locators(self, loc):
        return self.driver.find_elements(*loc)


    def locator2(self, loc, m):
        '''
        二次定位
        :param loc: 二次定位方法
        :param m: 第一定位结果的对象
        :return:
        '''
        # print(m)
        # print(loc)
        return m.find_element(*loc)


    # 输入
    def input_(self, loc, txt):
        self.locator(loc).send_keys(txt)

    def d_input(self, loc, txt):
        # 当传入目标为 定位 好了的元素时， 用d_input和 input_()做区分
        loc.send_keys(txt)

    # 清除
    def ele_clear(self, loc):
        self.locator(loc).clear()

    # 等待
    def wait(self, time_):
        sleep(time_)

    # 关闭
    def quit(self):
        self.driver.quit()

    def jjs(self, js):
        self.driver.execute_script(js)

    def d_click(self, loc):
        # 当传入目标为 定位 好了的元素时， 用d_click  和click()做区分
        loc.click()

    # 点击
    def click(self, loc, i=None):
        if i:
            self.locators(loc)[1].click()
        else:
            self.locator(loc).click()

    def ac(self, loc):
        print(1)
        ActionChains(self.driver).move_to_element(self.locator(loc)).click(self.locator(loc)).perform()

    # 获取元素 文本
    def ele_txt(self, loc, i=None):
        if i:
            return self.locators(loc)[i].text
        else:
            print(self.locator(loc).text)
            return self.locator(loc).text

    def d_ele_txt(self,loc):
        # 调试方法
        print(loc.text)

    def get_all(self, loc, text, i=None):
        if i:
            return self.locators(loc)[i].get_attribute(text)
        else:
            print(self.locator(loc).get_attribute(text))
            return self.locator(loc).get_attribute(text)

    def is_four_digits(string):
        # 如果字符串为空或者长度不等于4，返回False
        if not string or len(string) != 4:
            return False
        # 如果字符串只包含数字，返回True
        if string.isdecimal():
            return True
        # 否则返回False
        else:
            return False


    def get_covde(self,loc):
        self.locator(loc).screenshot('ele.png')
        ocr = ddddocr.DdddOcr()

        with open('ele.png', 'rb') as f:
            img_bytes = f.read()

        res = ocr.classification(img_bytes)

        return  res


