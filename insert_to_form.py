import pyscreenshot as screen
import pyautogui as auto
import numpy as np
from PIL import Image

# TO FIND THE CORRECT PIXELS
# print(auto.size())


# PART OF SCREEN THAT CHANGES WHEN SIGN IN SUCCESSFULLY
x1, y1 = 300, 300
x2, y2 = 400, 400



def Insert(password):
    # MOVE TO THE PASSWORD FIELD
    auto.click(500, 500)

    # INSERT PASSWORD
    auto.typewrite(password)

    # MOVE DOWN TO CLOSE KEYBOARD
    auto.click(500, 550)

    # MOVE DOWN TO CLICK ON IMPORT
    auto.click(500, 800)



def shot_and_analyse(name):
   image = screen.grab(bbox=(x1, y1, x2, y2))
   image.save(name)

   # MAKE SURE IT IS IN RGB FORMAT
   image = Image.open(name).convert('RGB')

   # CONVERT TO NUMPY ARRAY
   na = np.array(image)

   # ARRANGE ALL PIXELS 
   colours, counts = np.unique(na.reshape(-1,3), axis=0, return_counts=1)

   # print(colours)
   # print(counts)
   return counts


def First_shot():
    print("######################################################\n")
    input("open your desktop and ENTER")

    main = shot_and_analyse("main.png")

    print("######################################################\n")
    input("now open trust wallet and ENTER")

    return main


def Check(main):
   now = shot_and_analyse("temp.png")
   return now==main

