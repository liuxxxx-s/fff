import time
from page_obj.mj_regist import Regist
from page_obj.buyer_goAuth import GoAuth4
from selenium import webdriver
from base.t333 import CreditIdentifier

from base.base_page import BasePage

use = {"pws1": "Qq123456", "pws2": "Qq123456", "收货地址": ["湖北省", "武汉市", "武昌区"], "公司地址": ["湖北省", "武汉市", "青山区"],
     "spye": "生产企业"}

driver = webdriver.Chrome()

rg = Regist(driver)
rg.user_type_select("卖家")

rg.store_regist(use)
time.sleep(4)

yyzz = CreditIdentifier().get_c()
print(yyzz)
d = {
      '营业执照': {'licence_no': yyzz, 'calendar': '2024-12-30', 'img_ptah_card_name': "营业执照"},
      '开户许可证/开票信息': {'calendar': '2024-12-29', 'img_ptah_card_name': "开户证明"}
}

d2={"药品经营许可证":{'calendar': '2024-12-31', 'img_ptah_card_name': "药品经营许可证"}}




g = GoAuth4(driver)
g.selet_scope('成药')
for i in d:
    # 填写证照信息
    if d[i].get('licence_no'):
        print("有证照")
        g.inpt_card_no(i, d[i])
    else:
        print("无需要填写")

    # 选择日期
    if d[i].get('calendar'):
        g.select_day(i, d[i])

    # 上传照片
    g.upload_an_image(i, d[i])

for i in d2:
    g.select_day2(i, d2[i])
    g.upload_an_image(i, d2[i])