
#機能を４つ準備
#import 機能名で準備が出来る
#requests = Webから情報一式を取得する機能
#pandas = 表計算機能
#BeautifulSoup = Webから取得した情報の中から、さらに選別する機能
#time = Webに負担をかけないため、処理ごとに待機する時間を設定する機能
import requests
import pandas as pd
from bs4 import BeautifulSoup
import time

#「◯◯ =」の◯◯を「変数」という。例えば「url = 」で設定したURLは、
#一々https://~と入力しなくても、urlと入力するだけでhttps://~と一緒の意味になる
#情報を取得するURLを設定
url = "https://jre-abc.com/wp/afactory/"

#responseという変数に、「requests」の「get機能」を使って、設定したurlから情報を一式取得する。
response = requests.get(url, verify=False)

#urlで一式取得した情報を、さらに選別する機能「BeautifulSoup」でも読み込む
soup = BeautifulSoup(response.text, "html.parser")

#変数だけを打ち込むと、中身を確認出来る
soup

#eventという変数に、classという部分が""内の部分を抜き出す
event = soup.find_all(class_ = "wp-block-latest-posts__post-title")

#抜き出した情報の確認
event

for i in soup.find_all(class_ = "wp-block-latest-posts__post-title"):
    print(i.string, end="\n")
    print(i["href"], end="\n\n")


title = []
add = []

for i in soup.find_all(class_ = "wp-block-latest-posts__post-title"):
    title.append(i.string)
    add.append(i["href"])


df = pd.DataFrame({
    "タイトル": title,
    "URL": add
})

df