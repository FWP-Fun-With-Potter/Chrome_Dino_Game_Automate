import time
import pyautogui
#pip install pyautogui
from PIL import Image, ImageGrab
#pip install pillow

def jump():
    for x in range(255, 275):
        for y in range(490, 510):
            if number[x, y] > 150:
                pyautogui.press('space')
                return

if __name__ == '__main__':
    print("Running")
    time.sleep(2)

    while True:
        pic = ImageGrab.grab().convert('L')
        number = pic.load()
        jump()

    ''' For Checking the coordinates of the cactus
    for x in range(255, 275):
        for y in range(490, 510):
            number[x, y] = 0s

    pic.show()'''
