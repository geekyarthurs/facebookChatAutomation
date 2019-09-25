import time, pyautogui, clipboard, os,sys

pyautogui.PAUSE = 1
pyautogui.FAILSAFE = True

time.sleep(5)
print("Initiated Bot")
# x,y = pyautogui.position()

# for i in range(10):
#     pyautogui.moveTo(100, 100, duration=0.25)
#     pyautogui.moveTo(200, 100, duration=0.25)
#     pyautogui.moveTo(200, 200, duration=0.25)
#     pyautogui.moveTo(100, 200, duration=0.25)
normalGreeting = ["hi","hello","mahesh","dost","hi dost", "hello bro", "hi bro","hajur"]
foodGreeting = ["khana khayeu", "khana bhayo", "khayeu" , "khaja khayeu", "khaja bhayo"]
wydGreeting = ["k garira", "k gardai", "k gardai xau","k garira xau", "ah. tmle ni","tmle","tmle khayeu","ah tmle"]
i = 0

print("Lets open firefox and play music first..")
os.system("firefox youtube.com/watch\?v=yUxx1cIEoZg facebook.com &")
time.sleep(5)
pyautogui.moveTo(977,36)
pyautogui.click(977,36,button='left')
pyautogui.press("space")
time.sleep(1)
pyautogui.moveTo(336,105)
pyautogui.click(336,105,button='left')


while True:
    i = i + 1

    

    a = list(pyautogui.locateAllOnScreen("unseen_close_button.png"))

    if( a is None):
        continue
    print("Found {} unseen messages".format(len(a)))

    for foundCloseButton in a:

        # nameEndX = int(foundCloseButton.left) - 60
        # nameEndY = int(foundCloseButton.top) + 3

        time.sleep(4)
        chatX = int(foundCloseButton.left) - 172
        chatY = int(foundCloseButton.top) + 252

        # pyautogui.moveTo(nameEndX,nameEndY, duration=0.1)
        # pyautogui.dragTo(nameEndX - 20, nameEndY,duration=2.0, pause=3.0)

        pyautogui.moveTo(chatX,chatY,duration=0.3) #moving to chat box.
        pyautogui.tripleClick() # selecting text
        pyautogui.hotkey('ctrl','c')

        text = str(clipboard.paste()).strip()
        print("Received Message : {}".format(text))
        text = text.lower().replace("?","").strip()

        if text is None:
            continue
        if(text in normalGreeting):
            pyautogui.moveTo(y=chatY + 40)
            pyautogui.click(button='left')
            pyautogui.typewrite("Hajur")
            pyautogui.press('enter')
            print("Sending {}".format("hajur"))
            continue

        text = text.replace("bro", "").replace("dost", "").replace("mahesh","").strip() # removing names
        if(text in foodGreeting):
            pyautogui.moveTo(y=chatY + 40)
            pyautogui.click(button='left')
            pyautogui.typewrite("Ah khaye.. tapaile ni ?")
            print("Sending {}".format("Ah khaye.. tapaile ni ?"))
            pyautogui.press('enter')
            continue
        if(text in wydGreeting):
            pyautogui.moveTo(y=chatY + 40)
            pyautogui.click(button='left')
            pyautogui.typewrite("Yessai basira")
            print("Sending {}".format("Yessai basira"))
            
            pyautogui.press('enter')
            continue
        if(text == "bye"):
            pyautogui.moveTo(y=chatY + 40)
            pyautogui.click(button='left')
            pyautogui.typewrite("ok bye.")
            pyautogui.press('enter')
            continue


        
        time.sleep(3)
        
    # pyautogui.tripleClick(x=1147,y=990)

