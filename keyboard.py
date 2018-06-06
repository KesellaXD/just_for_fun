#coding:utf-8
from pynput.keyboard import Key, Controller
import time
keyboard=Controller()
time.sleep(5)
for i in range(1,1000):
    keyboard.type('祥锅吃不吃')
    with keyboard.pressed(Key.ctrl):
        keyboard.press(Key.enter)
    #time.sleep(0.5)
