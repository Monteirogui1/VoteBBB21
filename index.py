import pyautogui
import time

time.sleep(2)
print("Votando....")

while True:
    time.sleep(2)
    name_vote = pyautogui.locateOnScreen('nome.png', grayscale=True, region=(628, 821, 646, 120))
    if name_vote:
      point = pyautogui.center(name_vote)
      pyautogui.click(point)
      pyautogui.press('end')

    checkpoint = pyautogui.locateOnScreen('checkpoint.png', grayscale=True, region=(303, 78, 800, 1001))
    if checkpoint:
        pointCheck = pyautogui.center(checkpoint)
        pyautogui.click(pointCheck)

    back = pyautogui.locateOnScreen('back.png',  grayscale=True)
    if back:
        pback = pyautogui.center(back)
        pyautogui.click(pback)

        time.sleep(15)

        pass
