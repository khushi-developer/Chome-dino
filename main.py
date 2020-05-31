import pyautogui
from PIL import Image, ImageGrab
# from numpy import asarray
import time

def hit(key):
    pyautogui.keyDown(key)

def isCollide(data):
    # for cactus
    for i in range(470,510):
        for j in range(240,290):
            if data[i,j] < 100:
                hit("up")
                return True
    # for bird
    for i in range(470,510):
        for j in range(180,240):
            if data[i,j] < 100:
                hit("down")
                return True

    return False

if __name__ == "__main__":
    print("game will start within 3 seconds")
    time.sleep(3)
    # hit("up")
    while True:
        image = ImageGrab.grab().convert('L') #take screenshot and convert into grace scale image
        data = image.load() 
        isCollide(data)
          
    
    '''
        # draw rectangle for cactus
        for i in range(470,510):
            for j in range(240,290):
                data[i,j] = 0
        
        # draw rectangle for birds
        for i in range(470,510):
            for j in range(180,240):
                data[i,j] = 171

        image.show()
        break
    '''