import pyautogui
import cv2
import numpy as np
import time
from testtuple import compareImages
from PIL import Image

positions = [(637,226),(810,226),(983,226),(1156,226),\
             (637,466),(810,466),(983,466),(1156,466),\
             (637,706),(810,706),(983,706),(1156,706)]


def runThis():
    screenshots = []
    i = 0
    time.sleep(1)
    while i < 12:

        # Take 1st screen screenshot
        # check if array has any
        time.sleep(1.1)
        pyautogui.moveTo(positions[i][0], positions[i][1])
        pyautogui.click()
        time.sleep(.2)
        img = pyautogui.screenshot(region = (positions[i][0], positions[i][1], 121, 147))

        img_np = np.array(img)
        screenshots.append(img_np)
        if len(screenshots) > 1:
            j = 0
            while j < len(screenshots) - 1:
                #3969

                compare = screenshots[j]

                finalP = compareImages(img_np, compare)
                print("Percent at: " + str(finalP) + "%")
                if finalP > 30.0:
                    #print("Matched! at: " + str(finalP) + "%")
                    time.sleep(1.1)

                    pyautogui.moveTo(positions[j][0],positions[j][1])
                    pyautogui.click()
                    time.sleep(.2)
                    pyautogui.moveTo(positions[i][0], positions[i][1])
                    pyautogui.click()
                    break
                j+=1
        #increment variables
        i+=1
        #end while loop
k = 0
while k < 1000:
    runThis()
    time.sleep(5)
    pyautogui.moveTo(950, 450)
    pyautogui.click()
    time.sleep(1)
    pyautogui.moveTo(560, 500)
    pyautogui.click()
    time.sleep(1)
    k+=1
