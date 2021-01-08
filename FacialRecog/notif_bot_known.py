#Ini bot buat notifikasi

import os
import time
import pyautogui

# path = "C:\Users\chris\Dropbox\Machine Learning\home\FacialRecog\log"

def known():
    pyautogui.moveTo(166,751)
    pyautogui.click()
    time.sleep(1)
    pyautogui.moveTo(484,705)
    pyautogui.click()
    time.sleep(1)
    pyautogui.moveTo(483,636)
    pyautogui.click()
    time.sleep(1)
    pyautogui.moveTo(327,47)
    pyautogui.click()
    time.sleep(1)
    pyautogui.keyDown('ctrl')
    pyautogui.keyDown('v')
    pyautogui.keyUp('ctrl')
    pyautogui.keyUp('v')
    pyautogui.press('enter')
    time.sleep(2)
    pyautogui.moveTo(244,138)
    pyautogui.click()
    pyautogui.click()
    time.sleep(2)
    pyautogui.moveTo(225,175)
    pyautogui.click()
    pyautogui.click()
    time.sleep(2)
    pyautogui.moveTo(543,539)
    pyautogui.click()
    time.sleep(2)
    pyautogui.write('Andrew Detected', interval=0.25)
    time.sleep(2)
    pyautogui.moveTo(1289,602)
    pyautogui.click()
