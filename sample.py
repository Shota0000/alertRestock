# coding:utf-8
# webdriverのインポート
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
import requests
from time import sleep

# webdriver managerのインポート
from webdriver_manager.chrome import ChromeDriverManager

url = ['https://item.rakuten.co.jp/rakutenmobile-store/iphone-12_64gb_shop-b/',
'https://item.rakuten.co.jp/rakutenmobile-store/iphone-12_128gb_shop-b/',
'https://item.rakuten.co.jp/rakutenmobile-store/iphone-13_128gb_bundle_2/',
'https://item.rakuten.co.jp/rakutenmobile-store/iphone-13-pro-max_128gb_bundle_2/',
'https://item.rakuten.co.jp/rakutenmobile-store/iphone-13-pro_128gb_bundle_2/'
]

def line(i):
    TOKEN = 'dummy'
    api_url = 'https://notify-api.line.me/api/notify'
    send_content_01 = "iphoneが 再入荷したよ。申込はこちら→%s"%(url[i])
    #send_content_02 = 'iphone12 128GBが再入荷したよ。申込はこちら→https://item.rakuten.co.jp/rakutenmobile-store/iphone-12_128gb_shop-b/'

    # 情報を辞書型にする
    TOKEN_dic = {'Authorization': 'Bearer' + ' ' + TOKEN}
    send_dic_01 = {'message': send_content_01}
    requests.post(api_url, headers=TOKEN_dic, data=send_dic_01)
      

# ブラウザーを起動(ブラウザは非表示にするヘッドレス)
options = Options()
options.add_argument('--headless')

driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

while True:
    sleep(60)
    for i in range(len(url)):
        driver.get(url[i])
        res=driver.find_elements_by_class_name("new-cart-button")
         # 入荷待ちのときの処理と在庫ありのときの処理
        if len(res) > 0:
            print(i,"在庫あり")
            line(i)
        else:
            print(i,'入荷待ち')
