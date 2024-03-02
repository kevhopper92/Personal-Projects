# -*- coding: utf-8 -*-
"""
Created on Fri Jan 28 13:08:20 2022

@author: Kevin
"""
import pyautogui
import time
import keyboard

pyautogui.FAILSAFE = True


keep_going = True
time.sleep(5)
pyautogui.moveTo(x = 740, y = 360, duration = .2)
while keep_going:
    time.sleep(.02)
    if keyboard.is_pressed("ctrl+c"):
        keep_going = False
        break
    pyautogui.click()