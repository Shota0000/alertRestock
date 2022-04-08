# coding:utf-8
# webdriverのインポート
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
import requests
# sleepメソッドのインポート
from time import sleep

# webdriver managerのインポート
from webdriver_manager.chrome import ChromeDriverManager

flags=[True]*5

def line(flag64,flag128):
    TOKEN = 'Qx1OO4Cm4jjPjkoV5Gw1dMnmW6vFtzuN9aDkPgJ8tlU'
    api_url = 'https://notify-api.line.me/api/notify'
    send_content_01 = 'iphone12 64GBが再入荷したよ。申込はこちら→https://item.rakuten.co.jp/rakutenmobile-store/iphone-12_64gb_shop-b/'
    send_content_02 = 'iphone12 128GBが再入荷したよ。申込はこちら→https://item.rakuten.co.jp/rakutenmobile-store/iphone-12_128gb_shop-b/'

    # 情報を辞書型にする
    TOKEN_dic = {'Authorization': 'Bearer' + ' ' + TOKEN}
    send_dic_01 = {'message': send_content_01}
    send_dic_02 = {'message': send_content_02}

    # LINEに通知を送る（200: 成功時、400: リクエストが不正、401: アクセストークンが無効：公式より）
    if flag64 == True and flag128==True:
        requests.post(api_url, headers=TOKEN_dic, data=send_dic_01)
        requests.post(api_url, headers=TOKEN_dic, data=send_dic_02)
    elif flag64 == True: 
        requests.post(api_url, headers=TOKEN_dic, data=send_dic_01)
    elif flag128 == True: 
        requests.post(api_url, headers=TOKEN_dic, data=send_dic_02)


# ブラウザーを起動(ブラウザは非表示にするヘッドレス)
options = Options()
options.add_argument('--headless')

url = ['https://item.rakuten.co.jp/rakutenmobile-store/iphone-12_64gb_shop-b/','https://item.rakuten.co.jp/rakutenmobile-store/iphone-12_128gb_shop-b/']
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
# BIGLOBE商品ページにアクセス

while True:
    sleep(10)
    for i in range(len(url)):
        driver.get(url[i])
        res=driver.find_elements_by_class_name("new-cart-button")
         # 入荷待ちのときの処理と在庫ありのときの処理
        if len(res) > 0 and i==0:
            print("64GB在庫あり")
            line(True,False)
        elif len(res) > 0 and i==1:
            print("128GB在庫あり")
            line(False,True)
        else:
            print(i,'入荷待ち')
        # line(False)
    # driver1.get('https://item.rakuten.co.jp/rakutenmobile-store/iphone-12_64gb_shop-b/')
    # driver2.get('https://item.rakuten.co.jp/rakutenmobile-store/iphone-12_128gb_shop-b/')
    
driver1.quit()
driver2.quit()
