import pyautogui
import time


while True:
    x,y = pyautogui.position()
    positionStr = 'X: ' + str(x) + ' Y : ' + str(y)
    print(positionStr)
    time.sleep(2)
        

