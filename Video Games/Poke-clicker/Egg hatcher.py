# -*- coding: utf-8 -*-
"""
Created on Fri Dec 31 13:22:13 2021

@author: Kevin
"""

import pyautogui
import time
import keyboard

pyautogui.FAILSAFE = True
'''
while True:
    print(pyautogui.position())
    time.sleep(1)
'''
time.sleep(5)
keep_going = True
moniter = True
route_complete = False
egg = True

hoenn = {"101":(614, 715, 18865),
        "102":(582, 702, 20006),
        "103":(636, 682, 11173),
        "104":(537, 684, 10001),
        "105":(540, 735, 10033),
        "106":(560, 772, 10584),
        "107":(632, 790, 10029),
        "108":(673, 797, 9300),
        "109":(690, 770, 7540),
        "110":(693, 686, 10012),
        "111":(686, 585, 78000),
        "112":(672, 588, 24000),
        "113":(658, 524, 12000),
        "114":(571, 535, 12000),
        "115":(540, 571, 9833),
        "116":(586, 611, 9990),
        "117":(640, 622, 12000),
        "118":(740, 627, 3258),
        "119":(741, 590, 9809),
        "120":(780, 548, 3350),
        "121":(812, 575, 10000),
        "122":(827, 602, 4860),
        "123":(813, 630, 5316),
        "124":(943, 581, 2667),
        "125":(988, 557, 2100),
        "126":(996, 652, 2426),
        "127":(961, 644, 2000),
        "128":(1008, 701, 9760),
        "129":(1007, 716, 1801),
        "130":(962, 718, 1902),
        "131":(912, 714, 1800),
        "132":(835, 717, 2000),
        "133":(795, 718, 1800),
        "134":(744, 717, 9378)
}
if moniter:
    if route_complete:
        for route in hoenn.keys():
            print(route)
            #close windows
            pyautogui.moveTo(x= 1377, y = 464, duration = .2)
            pyautogui.click()
            #select route
            pyautogui.moveTo(x = hoenn[route][0], y = hoenn[route][1], duration = .2)
            pyautogui.click()
            counter = hoenn[route][2]
            print(f"Route {route}")
            while counter <= 10000:
                pyautogui.moveTo(x= 1318, y = 210, duration = .2)
                pyautogui.click()
                pyautogui.moveTo(x = 740, y = 360, duration = .2)
                for i in range(20):
                    time.sleep(.02)
                    counter += .45
                    pyautogui.click()
                pyautogui.moveTo(x= 1377, y = 464, duration = .2)
                pyautogui.click()
                pyautogui.moveTo(x = 602, y = 360, duration = .2)
                for i in range(250):
                    if keyboard.is_pressed("ctrl+c"):
                        keep_going = False
                        break
                    time.sleep(0.01)
                    pyautogui.click()
                    counter += .45
                if not keep_going:
                    break
            if not keep_going:
                    break
    else:
        while keep_going:
            #pyautogui.moveTo(x= 1499, y = 525, duration = .2)
            pyautogui.moveTo(x= 1635, y = 750, duration = .5) #list
            pyautogui.click()
            pyautogui.moveTo(x = 1096, y = 359, duration = .2) #pokemon
            for i in range(10):
                time.sleep(.1)
                if keyboard.is_pressed("ctrl+c"):
                    keep_going = False
                    break
                pyautogui.click()
            pyautogui.moveTo(x= 1851, y = 634, duration = .2) #blank space
            pyautogui.click()
            pyautogui.moveTo(x = 775, y = 473, duration = .2) #champion
            for i in range(100):
                if keyboard.is_pressed("ctrl+c"):
                    keep_going = False
                    break
                time.sleep(0.1)
                pyautogui.click()
            #pyautogui.moveTo(x= 1499, y = 418, duration = .2)
            #pyautogui.click()
            #pyautogui.moveTo(x = 727, y = 479, duration = .2)
            #pyautogui.click()
else:
    if egg:
        while keep_going:
            #pyautogui.moveTo(x= 1499, y = 525, duration = .2)
            pyautogui.moveTo(x= -424, y = 593, duration = 1)
            pyautogui.click()
            pyautogui.moveTo(x = -867, y = 285, duration = .2)
            for i in range(10):
                time.sleep(.1)
                pyautogui.click()
            pyautogui.moveTo(x= -219, y = 522, duration = .2)
            pyautogui.click()
            
            #champion
            pyautogui.moveTo(x = -1147, y = 380, duration = .2)
            #battle frontier
            #pyautogui.moveTo(x = 800, y = 800, duration = .2)
            for i in range(100):
                if keyboard.is_pressed("ctrl+c"):
                    keep_going = False
                    break
                time.sleep(0.01)
                pyautogui.click()
    else:
        pyautogui.moveTo(x = 727, y = 230, duration = .2)
        while keep_going:
            if keyboard.is_pressed("ctrl+c"):
                keep_going = False
                break
            time.sleep(0.01)
            pyautogui.click()