"""
    买家注册页面

"""
import time

from base.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium import webdriver
from faker import Faker


class Regist(BasePage):
    # 核心元素
    f = Faker(locale='zh_CN')
    url = 'https://b2b.sit.expowh.com/store/regist.htm'
    # 新增元素对象 用户名  10/20
    loginName=(By.NAME,'loginName')
    mobilePhone = (By.NAME, 'phoneNunmber')  # 手机号
    picCode_img=(By.ID,'cust_vcode_img')
    picCode = (By.NAME, 'picCode')  # 图像验证码
    smsCode = (By.NAME, 'smsCode')  # 短信验证码
    pwd = (By.NAME, 'loginPwd')  # 密码
    pwd2 = (By.NAME, 'loginPwd2')  # 确认密码
    cust_firm_name = (By.ID, 'cust_firm_name')  # 企业名称
    city_picker = (By.CLASS_NAME, 'm_citypicer')  # 企业所在地
    receive_address = (By.CLASS_NAME, 'm_citypicer2')  # 收货区域
    cust_receive_addr = (By.ID, 'cust_receive_addr') # 详细地址
    cust_receive_name = (By.ID, 'cust_receive_name') # 收件人
    cust_receive_tel = (By.ID, 'cust_receive_tel') #收件人电话

    cust_firm_person=(By.ID,'cust_firm_person') # 企业法人
    cust_firm_phone=(By.ID,'cust_firm_phone')#法人电话
    cust_firm_address=(By.ID,'cust_firm_address')# 详细地址
    buyers=(By.XPATH,'//li[(text()="买家注册")]')
    vendors=(By.ID,'storeSelector')

    def user_type_select(self,ty):
        if ty=="买家":
            self.click(self.buyers)
        if ty=="卖家":
            self.click(self.vendors)
    def click_register(self):
        #立即注册
        c=(By.ID,"register")
        self.click(c)
        time.sleep(3)

    def saveNextBut(self):
        saveb=(By.ID,"saveNextBut")
        self.click(saveb)

    def  rz(self):
        # 去认证
        self.click((By.XPATH,'//button[(text()="去认证")]'))
        time.sleep(2)

    # 返回 企业类型的 的对象
    def xp_st_type(self, st_type='连锁门店'):
        xp = '//div[(text()="%s")]' % st_type
        return (By.XPATH, xp)

    # 返回 省市区 的元素对象 （xpath 方式定位的）
    def __city_xp(self, s_s_c):
        xp = '//a[contains(text(),"%s")]' % s_s_c
        return (By.XPATH, xp)


    # 核心业务

    def __select_cit(self, city_list):
        """选中 企业所在地 """
        # 选中省市区
        self.click(self.city_picker)
        for i in city_list:
            self.click(self.__city_xp(i))

    def __select_receive(self, city_list):
        """选中 收货所在地"""
        # 选中省市区  湖北省 初始页面里 有2个。所以在选择 收货地址的时候（第二个湖北省，要单独判断一下）
        self.click(self.receive_address)
        for i in city_list:
            # if city_list.index(i) == 0:
            self.click(self.__city_xp(i), 1)
            # else:
            #     self.click(self.__city_xp(i))

    def __pws_errmsg(self):
        return (By.XPATH, '//input[@name="loginPwd2"]/following-sibling::div')

    def get_pws_errmsg(self):
        return self.ele_txt(self.__pws_errmsg())


    def mjregist(self,d):
        # 统合在一起的 一个 方法
        self.open_u()
        phone=self.f.phone_number()
        self.input_(self.loginName,"p"+phone)
        self.input_(self.mobilePhone, phone)
        # 处理验证码：
        int_code= self.get_covde(self.picCode_img)


        self.input_(self.picCode, int_code)
        time.sleep(5)
        self.input_(self.smsCode, '9527')
        self.input_(self.pwd, d["pws1"])
        self.input_(self.pwd2, d["pws2"])

        self.click_register()
        self.rz()
        self.click(self.xp_st_type(d["spye"]))
        self.__select_cit(d["公司地址"])
        self.__select_receive(d["收货地址"])
        self.input_(self.cust_firm_name,self.f.company())
        self.input_(self.cust_receive_name,'法外狂徒')
        self.input_(self.cust_receive_addr,'知音茶城')
        self.input_(self.cust_receive_tel,'13111101120')

        self.input_(self.cust_firm_person,'张三')
        self.input_(self.cust_firm_address,'九州通大厦')
        self.input_(self.cust_firm_phone,'18111101120')
        self.saveNextBut()
if __name__ == "__main__":
    D={"pws1": "Qq123456","pws2": "Qq123456","收货地址": ["湖北省","武汉市","武昌区"],"公司地址":["湖北省","武汉市","青山区"],"spye": "连锁门店"}
    driver = webdriver.Chrome()
    rg = Regist(driver)
    rg.open_u()
    rg.user_type_select('卖家')
    #rg.mjregist(D)
