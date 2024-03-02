# -*- coding: utf-8 -*-
"""
Created on Sat Jan 22 21:39:47 2022

@author: Kevin
"""


from pynput.mouse import Listener
import pyautogui

global c
c = 100

def on_click(x, y, button, pressed):
    if pressed:
        global c
        c+=1
        x, y = pyautogui.position()
        print(f'({x}, {y}),')

with Listener(on_click=on_click) as listener:
    listener.join()