import time
import os
from base.base_page import BasePage
from base.t333 import CreditIdentifier
from selenium.webdriver.common.by import By
from selenium import webdriver
from faker import Faker


# 完善资料


class GoAuth4(BasePage):

    submitButton = (By.ID, 'submitButton')

    def buttom_click(self):
        self.click(self.submitButton)


    def  __get_flag_elem__(self, card_name):
        # 获取证照名称的父级元素，用于后面的方法

        str_1 = '//h2[contains(text(),"%s")]/..' % card_name
        return self.locator((By.XPATH, str_1))



    def inpt_card_no(self, card_name,card_data):
        '''
        输入证照的证件号
        {'药品经营许可证': {'calendar': '2024-12-31', 'img_ptah_card_name': '药品经营许可证'}}
        :param card_i: 需要处理的 证件的名称
        :return:
        '''

        # 二次定位
        f_elemd = self.__get_flag_elem__(card_name)
        licence_no = self.locator2((By.NAME, "title"), f_elemd)

        self.d_input(licence_no, card_data['licence_no'])



    def select_day(self, card_name,card_data):
        '''
        选择证照有效期
        :param card_i: 需要处理的 证件的名称
        :return:
        '''

        f_elemd = self.__get_flag_elem__(card_name)
        # 获取日历id
        rl = self.locator2((By.XPATH, ".//input[starts-with(@id,'mustDatepick')]"), f_elemd)
        rl_id = rl.get_attribute('id')

        # 去除日历 readonly 属性,并赋值
        js1 = "$('input[id=%s]').removeAttr('readonly').val('%s')" % (rl_id,card_data['calendar'])
        print(js1)
        self.jjs(js1)

    def select_day2(self, card_name,card_data):
        '''
        选择证照有效期(买家商品证照的日期)
        :param card_name: 需要处理的 证件的名称
        param  card_data 证照数据
        :return:
        '''
        print(card_name)
        print(card_data)
        f_elemd = self.__get_flag_elem__(card_name)
        # # 获取日历id
        rl = self.locator2((By.XPATH, ".//input[starts-with(@id,'myDatepick')]"), f_elemd)
        rl_id = rl.get_attribute('id')
        #
        # # 去除日历 readonly 属性,并赋值
        js1 = "$('input[id=%s]').removeAttr('readonly').val('%s')" % (rl_id, card_data['calendar'])
        print(js1)
        self.jjs(js1)

    def upload_an_image(self, card_name,card_data):
        '''
        上传图片
        :param card_i:
        :return:
        '''
        f_elemd = self.__get_flag_elem__(card_name)
        img = os.path.abspath("../zp/%s.jpg" % card_data["img_ptah_card_name"])
        licence_no = self.locator2((By.NAME, "file"), f_elemd)
        self.d_input(licence_no, img)

    def selet_scope(self, scope_n):
        '''
        选中经验范围（大类）
        :param scope_n: 经营范围的名称  成药、中药、食品、器械、其他类别、医疗器械
        :return:
        '''
        Xpath_str = '//span[contains(text(),"%s")]/../..' % scope_n
        print(Xpath_str)

        X = (By.XPATH, Xpath_str)

        self.click(X)


if __name__ == "__main__":
    # chrome.exe --remote-debugging-port=9222 --user-data-dir="C:\selenium_ui_auto"
    from selenium.webdriver.chrome.options import Options

    chrome_options = Options()
    chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
    chrome_driver = r"C:\Users\liu\AppData\Local\Programs\Python\Python37\chromedriver.exe"
    driver = webdriver.Chrome(chrome_driver, chrome_options=chrome_options)

    d = {
         '营业执照': {'licence_no': '91130230213384968F', 'calendar': '2024-12-30', 'img_ptah_card_name': "营业执照"},
         '开户许可证/开票信息': {'calendar': '2024-12-29', 'img_ptah_card_name': "开户证明"}
         }
    d2={ "药品经营许可证":{'calendar': '2024-12-31', 'img_ptah_card_name': "药品经营许可证"}}


    g = GoAuth4(driver)
    g.selet_scope('成药')
    time.sleep(2)
    for i in d2:
        g.select_day2(i,d2[i])
        g.upload_an_image(i,d2[i])

    for i in d:
        # 填写证照信息

        if d[i].get('licence_no'):
            print("有证照")
            g.inpt_card_no(i,d[i])
        else:
            print("无需要填写")

        # 选择日期
        if d[i].get('calendar'):
            g.select_day(i,d[i])

        # 上传照片
        g.upload_an_image(i,d[i])

   # g.buttom_click()