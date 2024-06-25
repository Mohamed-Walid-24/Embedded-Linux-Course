import pyautogui as pg
import webbrowser
import time

gmail = "https://mail.google.com/mail/u/0/#inbox"
webbrowser.open(gmail)

time.sleep(5)
c_1 = (474, 256)
time.sleep(1)
c_2 = (594, 294)

pg.click(c_1)
pg.click(c_2)