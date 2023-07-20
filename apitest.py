#「import ◯◯（機能名）」または「from ◯◯ import ◯◯（機能名）」で、◯◯の機能を使える
#「import ◯◯ as ××」は、◯◯という機能を、××という略称で使うという宣言
#「pandas」 = 表計算を行う
#「requests」 = Webから情報一式を取得する
#「pprint」 = 取得したデータを見やすくする
#「json」 = APIを使った時にサイトから返ってくるデータ形式
import pandas as pd
import requests
import pprint
import json

#urlという変数に、情報一式を取得するURLアドレスを入れる
url = "https://api.aoikujira.com/tenki/week.php?"

#パラメーターを設定
#パラメーターを設定しない場合は、api.aoikujira.com/tenki/week.php?fmt=◯◯&city=那覇 というURLになる
params = {
    "fmt": "json",
    "city": "那覇"
}

#requests機能で、urlから情報一式を取得し、それをresponseという変数に入れる
response = requests.get(url, params).json()

#キーの取得
print(response.keys())

#response変数に入れたAPIサイトから返ってきた情報を、見やすい形で表示する
pprint.pprint(response)


#繰り返し処理には、forという機能を使う
#for 変数 in 値 = 値が1,2,3だった時、変数に1,2,3が順番に代入される
test = [1, 2, 3]

for i in test:
    print(i)

#複数の都市の予報を取得するため、
city_list = ["青森", "仙台", "東京", "大阪", "那覇"]

#iに都市名が順番に入る。そして、URLアドレスのcity=部分に i を設定する事で、順番に５つのURLにアクセスする
for i in city_list:
    params = {
        "fmt": "json",
        "city": i
    }
    
    response = requests.get(url, params).json() 

    #表形式で表示する
    df = pd.json_normalize(response, record_path=i)
    print("\n\n")
    print("市町村名：", i)
    print(df)