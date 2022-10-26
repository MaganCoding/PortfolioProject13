from PIL import ImageGrab
import pyautogui as pag
import time
import numpy as np


def jump():
    pag.press('up')


def get_image():
    gamebox = (615, 350, 750, 400)
    image = ImageGrab.grab(gamebox).convert('L')
    # image.show()

    array = np.array(image.getcolors())
    array_sum = array.sum()
    print(array_sum)
    return array_sum

time.sleep(1)
jump()

start = time.time()
pixels = get_image()
while True:
    new_pixels = get_image()
    if new_pixels - pixels != 0:
        jump()
        print("jumped!")
        pixels = new_pixels
