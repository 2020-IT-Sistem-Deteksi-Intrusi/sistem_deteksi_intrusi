import pyautogui
import time
import cv2


def screenshot():
    pyautogui.keyDown('shift')
    pyautogui.keyDown('winleft')
    pyautogui.keyDown('s')
    pyautogui.keyUp('shift')
    pyautogui.keyUp('winleft')
    pyautogui.keyUp('s')

def check_mouse():
    pyautogui.moveTo(844,15)
    time.sleep(1)
    pyautogui.click()

def copy_image():
    pyautogui.moveTo(1374,673)
    time.sleep(1)
    pyautogui.click()
    time.sleep(1)
    # pyautogui.keyDown('ctrl')
    # pyautogui.keyDown('c')
    # pyautogui.keyUp('ctrl')
    # pyautogui.keyUp('c')

# def save_image():


# def save_image():
#     pyautogui.keyDown('ctrl')
#     pyautogui.keyDown('s')
#     pyautogui.keyUp('ctrl')
#     pyautogui.keyUp('s')
#     time.sleep(1)
#     i = 1
#     pyautogui.typewrite('Log ke - ')
#     pyautogui.typewrite(i)
#     pyautogui.keyDown('enter')

if __name__ == "__main__":
    screenshot()
    check_mouse()
    time.sleep(1)
    copy_image()
    time.sleep(1)
    # save_image()