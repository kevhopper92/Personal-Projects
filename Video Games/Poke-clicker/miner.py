# -*- coding: utf-8 -*-
"""
Created on Thu Feb 10 20:11:35 2022

@author: Kevin
"""

import pyautogui
import time
import keyboard

pyautogui.FAILSAFE = True

time.sleep(5)
keep_going = True
moniter = True
route_complete = False

potion = (566, 157)

digs = [(442, 240),
                (443, 336),
                (439, 444),
                (443, 529),
                (537, 241),
                (533, 342),
                (541, 437),
                (535, 532),
                (633, 240),
                (634, 340),
                (629, 432),
                (625, 534),
                (729, 236),
                (729, 341),
                (734, 428),
                (725, 533),
                (828, 532),
                (828, 433),
                (822, 335),
                (822, 252),
                (925, 244),
                (918, 343),
                (921, 432),
                (916, 530),
                (1017, 527),
                (1013, 432),
                (1010, 341),
                (1011, 254),
                (1103, 247),
                (1118, 343),
                (1109, 441),
                (1107, 535),
                (1148, 244),
                (1143, 336),
                (1147, 447),
                (1149, 531)]

potion_restock = [(1488, 401),
                (1273, 625),
                (685, 501),
                (1067, 627),
                (1156, 630),
                (1414, 632),
                (1282, 557)]

energy = 0
timing =  .01
potion_timing = 0.5

potion_stock = 0

def move_and_click(x1, y1, t):
    pyautogui.moveTo(x = x1, y = y1, duration = t)
    pyautogui.click()

def energy_click(x1, y1):
    global energy
    global potion_stock
    if potion_stock < 2:
        for step in potion_restock:
            move_and_click(step[0], step[1], potion_timing)
        potion_stock+=800
    if energy < 3:
        move_and_click(potion[0], potion[1], timing)
        time.sleep(timing)
        for j in range(10):    
            pyautogui.click()
            time.sleep(timing)
        energy = 120
        potion_stock-=10
        move_and_click(x1, y1, timing)
        energy -= 3
    else:
        move_and_click(x1, y1, timing)
        energy -= 3

while keep_going:
    for i in digs:
        for j in range(5):
            energy_click(i[0], i[1])
            if keyboard.is_pressed("ctrl+c"):
                keep_going = False
                break
        if keyboard.is_pressed("ctrl+c"):
            keep_going = False
            break