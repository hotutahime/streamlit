import pyautogui as pag

#マウスの座標を取得
pag.position()
#（仮）x=500, y=1000

#マウスを指定地点まで移動
pag.moveTo(500, 1000)

#マウスを指定地点まで時間をかけて移動
pag.moveTo(500, 1000, duration=1)

#左クリック
pag.click()

#ダブルクリック
pag.doubleClick()

#右クリック
pag.rightClick()

#ショートカットキーはhotkeyコマンド
#全選択
pag.hotkey("ctrl", "a")
#コピー
pag.hotkey("ctrl", "c")
#貼り付け
pag.hotkey("ctrl", "v")

#特定のボタンはpressコマンド
pag.press("enter")
#回数指定
pag.press("enter", presses=2)
#間隔指定
pag.press("enter", presses=2, interval=0.5)

#入力する
pag.write("これはテストです")