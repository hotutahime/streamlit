import pyautogui as pag
import time

# print(pag.size())

# scr_w, scr_h = pag.size()
# print("幅=", scr_w, "高さ=", scr_h)

# center_x = scr_w / 2
# center_y = scr_h / 2

# print("画面中央 x = ", center_x, "y = ", center_y)

# print(pag.position())

# m_posi_x, m_posi_y = pag.position()

#マウスの現在位置を1秒感覚で取得し、ctrl+cを押すと止まる
# try:
#     while True:
#         m_posi_x, m_posi_y = pag.position()
#         print("x", m_posi_x, "y", m_posi_y)
#         time.sleep(1)
# except KeyboardInterrupt:
#     print("\n")


pag.moveTo(200, 300, 1)