import pyautogui as pg
import time
time.sleep(10)
txt = open('animals.txt', 'r')
a = "Irfan is a"
for i in txt:
    pg.write(a+' '+i)
    pg.press('Enter')

# a = "Mashaal is a"
# for i in range(50):
#     pg.write(a+' Badtmez larki')
#     pg.press('Enter')
