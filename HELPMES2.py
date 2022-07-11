import pyautogui as pt
import pyperclip as pp
from time import sleep
from time import time
from textos import embelezeTempo as eT

URL1 = "https://www.speedrun.com/infinite_arrow/run/new?level=Level_{0}#Any"
URL2 = "https://www.speedrun.com/infinite_arrow/run/new?level=Level_{0}#Perfect"

level = 140

a = 0

I = 0.5

link = ""

begin = time() #21:37

while True:
    a+=1
    input()
    pt.click(1270,10)
    if a%2:
        level += 1
        end = time()
        duration = end-begin
        begin = time()
        print(f"falta : {eT(duration * (201-level))}")
        pp.copy(URL1.format(level))
    else:
        pp.copy(URL2.format(level))
    pt.click(300,65)
    sleep(I)
    pt.hotkey("ctrl","v")
    sleep(I)
    pt.press("enter")
    sleep(15*I)
    for b in range(10):
        pt.click(665,715)
    if a%2:
        pt.rightClick(1000,200)
        sleep(I)
        pt.click(1100,300)
        link = pp.paste()
        pp.copy(link)
    else:
        pp.copy(link)
    pt.click(300,550)
    pt.hotkey("ctrl","v")
    if a%2:
        pt.click(200,750)
        pt.click(700,550)
        
