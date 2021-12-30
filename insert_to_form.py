import pyautogui as auto

# TO FIND THE CORRECT PIXELS
# print(auto.size())


def Insert(password):
    # MOVE TO THE PASSWORD FIELD
    auto.click(500, 500)

    # INSERT PASSWORD
    auto.typewrite(password)

    # MOVE DOWN TO CLOSE KEYBOARD
    auto.click(500, 550)

    # MOVE DOWN TO CLICK ON IMPORT
    auto.click(500, 800)