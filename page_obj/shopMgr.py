# 店铺管理
import time
from base.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium import webdriver
from faker import Faker


class Mgr(BasePage):
    # 核心元素
    f = Faker(locale='zh_CN')
    basic_configuration=(By.XPATH,'//a[(text()="基础配置")]')

    def __get_flag_elem__(self, K):
        # 获取证照名称的父级元素，用于后面的方法

        str_1 = '//label[contains(text(),"%s")]/../..' % K
        return self.locator((By.XPATH, str_1))

    def AAAAA(self,K,V):
        "订单备注"

        """    
         建采设置有问题
        """
        f_elemd = self.__get_flag_elem__(K)
        str_2='.//span[text()="%s"]'%V
        butto = self.locator2((By.XPATH, str_2), f_elemd)
        print(butto.text)
        self.d_click(butto)


    def khsm(self):
        u=(By.XPATH,'//input [@placeholder="50个字以内"] ')
        self.input_(u,'dftygueuhjwklssp')
    def click_b_c(self):
        self.click(self.basic_configuration)

if __name__ == "__main__":
    #chrome.exe --remote-debugging-port=9222 --user-data-dir="C:\selenium_ui_auto"
    from selenium.webdriver.chrome.options import Options

    chrome_options = Options()
    chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
    chrome_driver = r"C:\Users\liu\AppData\Local\Programs\Python\Python37\chromedriver.exe"
    driver = webdriver.Chrome(chrome_driver, chrome_options=chrome_options)
    # #
    # mg=Mgr(driver)
    # mg.AAAAA('订单备注','关闭')
    # mg.AAAAA('建议零售价', '隐藏')
    # mg.AAAAA('商品效期', '显示')

    # mg.khsm()
    driver.find_element_by_xpath('//span[text()="电票"]/../span[1]').click()
