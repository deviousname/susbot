#made by deviousname, someone better than me can clean this code up and improve upon it
#feel free to change it to suit your needs *you do not have permission to sell any code derived from this code: GNU Affero General Public License v3.0

#this first import is where you store your username and password to login to Reddit(required), found in: crewmate.py
from crewmate import username, password

import random
import time
from itertools import cycle

#Controll imports
import keyboard
import mouse
import pyautogui as autogui

#other
from selenium import webdriver
from selenium.webdriver.common.by import By

class Bot(): 
    def __init__ (self,username,password):
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome() #you need chromedriver.exe: https://chromedriver.chromium.org/downloads
        self.login()
        self.colors = self.get_colors()

    def login(self):
        #login sequence, using Reddit, set your username and pass for Reddit in crewmate.py's variables 'username' and 'password'
        print ('Logging in now through Reddit. If you get an error you may need to set your name and password in crewmate.py')
        self.driver.get("https://pixelplace.io/api/sso.php?type=2&action=login")
        self.driver.find_element_by_id('loginUsername').send_keys(self.username)
        self.driver.find_element_by_id('loginPassword').send_keys(self.password)
        self.driver.find_elements_by_xpath('/html/body/div/main/div[1]/div/div[2]/form/fieldset')[4].click()

        #Simon - I suggest waiting on the button that needs to be pressed to appear instead of waiting a fixed time
        
        time.sleep(7)#adjust this sleep in seconds if logging after sending name/pass is slow for you

        self.driver.find_elements_by_xpath('/html/body/div[3]/div/div[2]/form/div/input')[0].click()
        print ('All done logging in, ready to paint.')
        #end login

    #Simon - Refactored Colors into getting saved into a dictionary via a for loop. Also renamed cycles according to Keystrokes

    def get_colors(self): 
            #setting up the colors for fast color switching:
            self.color_dict = {}
            for color_name,x in zip(["white","grey1","grey2","grey3","grey4","black","green1","green2","green3","green5","yellow1","yellow2","yellow3","yellow4","brown1","brown2","brown3","red1","red2","red3","brown4","peach1","peach2","peach3","pink1","pink2","pink3","pink4","blue1","blue2","blue3","blue4","blue5","blue6","blue7"],range(0,34)):
                path = self.driver.find_elements_by_xpath('//*[@id="palette-buttons"]/a')[x]
                self.color_dict.update({f"{color_name}":path})
            self.Colors_W =  cycle([self.color_dict.get("grey4"), self.color_dict.get("grey3"), self.color_dict.get("grey2"), self.color_dict.get("grey1")])
            self.Colors_A =  cycle([self.color_dict.get("green1"), self.color_dict.get("green2"), self.color_dict.get("green3"), self.color_dict.get("green5")])
            self.Colors_S =  cycle([self.color_dict.get("red1"), self.color_dict.get("red2"), self.color_dict.get("red3")])
            self.Colors_D =  cycle([self.color_dict.get("brown1"), self.color_dict.get("brown2"), self.color_dict.get("brown3"), self.color_dict.get("brown4"), self.color_dict.get("grey4"), self.color_dict.get("peach3"), self.color_dict.get("white")])
            self.Colors_AW = cycle([self.color_dict.get("yellow1"), self.color_dict.get("yellow2"), self.color_dict.get("yellow3"), self.color_dict.get("yellow4")])
            self.Colors_WD = cycle([self.color_dict.get("brown1"), self.color_dict.get("brown2"), self.color_dict.get("brown3"), self.color_dict.get("brown4")])
            self.Colors_DS = cycle([self.color_dict.get("black"), self.color_dict.get("white")])
            self.Colors_SA = cycle([self.color_dict.get("blue1"),self.color_dict.get("blue2"),self.color_dict.get("blue3"),self.color_dict.get("blue4"),self.color_dict.get("blue5"),self.color_dict.get("blue6"),self.color_dict.get("blue7")])
            self.Colors_ALL = cycle([self.color_dict.get("white"),self.color_dict.get("grey1"),self.color_dict.get("grey2"),self.color_dict.get("grey3"),self.color_dict.get("grey4"),self.color_dict.get("black"),self.color_dict.get("green1"),self.color_dict.get("green2"),self.color_dict.get("green3"),self.color_dict.get("green5"),self.color_dict.get("yellow1"),self.color_dict.get("yellow2"),self.color_dict.get("yellow3"),self.color_dict.get("yellow4"),self.color_dict.get("brown1"),self.color_dict.get("brown2"),self.color_dict.get("brown3"),self.color_dict.get("red1"),self.color_dict.get("red2"),self.color_dict.get("red3"),self.color_dict.get("brown4"),self.color_dict.get("peach1"),self.color_dict.get("peach2"),self.color_dict.get("peach3"),self.color_dict.get("pink1"),self.color_dict.get("pink2"),self.color_dict.get("pink3"),self.color_dict.get("pink4"),self.color_dict.get("blue1"),self.color_dict.get("blue2"),self.color_dict.get("blue3"),self.color_dict.get("blue4"),self.color_dict.get("blue5"),self.color_dict.get("blue6"),self.color_dict.get("blue7")]
)




    #Simon - Adapted the new Color System and compacted it a bit

    #this is how the key combos work, for example if you press A and W it will run whichcolor2() aka the yellow colors
    def rainbowbrush(self): 
        if keyboard.is_pressed("s") or keyboard.is_pressed("a") or keyboard.is_pressed("w") == True or keyboard.is_pressed("d") == True:        
            #only A
            if keyboard.is_pressed("a") == True and keyboard.is_pressed("s") != True and keyboard.is_pressed("w") != True and keyboard.is_pressed("d") != True:
                next(self.Colors_A).click()
            #only S
            if keyboard.is_pressed("s") == True and keyboard.is_pressed("a") != True and keyboard.is_pressed("w") != True and keyboard.is_pressed("d") != True:
                next(self.Colors_S).click()
            #only AW
            if keyboard.is_pressed("a") == True and keyboard.is_pressed("w") == True and keyboard.is_pressed("d") != True and keyboard.is_pressed("s") != True:
                next(self.Colors_AW).click()
            #only W
            if keyboard.is_pressed("w") == True and keyboard.is_pressed("a") != True and keyboard.is_pressed("s") != True and keyboard.is_pressed("d") != True:
                next(self.Colors_W).click()
            #only WD
            if keyboard.is_pressed("w") == True and keyboard.is_pressed("d") == True and keyboard.is_pressed("s") != True and keyboard.is_pressed("a") != True:
                next(self.Colors_WD).click()
            #only D
            if keyboard.is_pressed("d") == True and keyboard.is_pressed("s") != True and keyboard.is_pressed("a") != True and keyboard.is_pressed("w") != True:
                next(self.Colors_D).click()
            #only DS
            if keyboard.is_pressed("d") == True and keyboard.is_pressed("s") == True and keyboard.is_pressed("a") != True and keyboard.is_pressed("w") != True:
                next(self.Colors_DS).click()
            #only SA
            if keyboard.is_pressed("s") == True and keyboard.is_pressed("a") == True and keyboard.is_pressed("d") != True and keyboard.is_pressed("w") != True:
                next(self.Colors_SA).click()

    # this function is still a work in progress and you can set it in the controls, tree leafs are a good use for this, it paints the next color on the list after checking which color is under your mouse cursor
    def colorshift(self): 
        x,y = autogui.position()
        pixy = autogui.pixel(x,y) #check nearby pixel color
        colorshift_dict = {(255,255,255):self.color_dict.get("grey1"),(196,196,196):self.color_dict.get("grey2"),(136,136,136):self.color_dict.get("grey3"),(85,85,85):self.color_dict.get("grey4"),(34,34,34):self.color_dict.get("black"),(0,0,0):self.color_dict.get("green1"),(0,102,0):self.color_dict.get("green2"),(34,177,76):self.color_dict.get("green3"),(81,225,25):self.color_dict.get("green5"),(148,224,68):self.color_dict.get("yellow1"),(251,255,91):self.color_dict.get("yellow2"),(229,217,0):self.color_dict.get("yellow3"),(230,190,12):self.color_dict.get("yellow4"),(229,149,0):self.color_dict.get("brown1"),(160,106,66):self.color_dict.get("brown2"),(153,90,26):self.color_dict.get("brown3"),(99,60,31):self.color_dict.get("red1"),(107,0,0):self.color_dict.get("red2"),(159,0,0):self.color_dict.get("red3"),(255,57,4):self.color_dict.get("brown4"),(187,79,0):self.color_dict.get("peach1"),(255,117,95):self.color_dict.get("peach2"),(255,196,159):self.color_dict.get("peach3"),(255,223,204):self.color_dict.get("pink1"),(255,167,209):self.color_dict.get("pink2"),(207,110,228):self.color_dict.get("pink3"),(236,8,236):self.color_dict.get("pink4"),(81,0,255):self.color_dict.get("blue1"),(2,7,99):self.color_dict.get("blue2"),(0,0,234):self.color_dict.get("blue3"),(4,75,255):self.color_dict.get("blue4"),(101,131,207):self.color_dict.get("blue5"),(54,186,255):self.color_dict.get("blue6"),(0,131,199):self.color_dict.get("blue7"),(69,255,200):self.color_dict.get("white")}
        try:
            colorshift_dict.get(pixy).click()
        except:
            pass

    def tree_2(self,side): #palm tree
        if self.lastside == side:
            side = -side
        x,y = autogui.position()
        #vector is value between 1 and 4
        self.color_dict.get("brown1").click()
        keyboard.press('space')
        #build the tree:
        variant = random.randint(1,4)
        if variant in range(1,2):
            #trunk start (2 x 3)
            for steps in range(3):
                for steps in range(2):
                    autogui.moveTo(x,y)
                    y -= 1
                x += side
            # trunk end
            y += 1
        else:
            #trunk start (3 x 2)
            for Steps in range(2):
                for _ in range(3):
                    autogui.moveTo(x,y)
                    y -= 1
                x += side
            y += 1            
            # trunk end

        #draw the leaves:
        autogui.moveTo(x+side,y)
        next(self.Colors_A).click()
        autogui.moveTo(x-side,y)
        autogui.moveTo(x+side+side+side,y)
        autogui.moveTo(x-side-side-side,y)
        autogui.moveTo(x,y-1)
        autogui.moveTo(x-side,y-1)
        autogui.moveTo(x+side,y-1)
        autogui.moveTo(x-side*2,y-1)
        autogui.moveTo(x+side*2,y-1)
        autogui.moveTo(x,y-2)
        autogui.moveTo(x-side,y-2)
        autogui.moveTo(x+side,y-2)
        keyboard.release('space')
        self.lastside = side #invert side so the next tree faces the opposite direction

    def tree_1(self,side): #normal style tree that using every color for the leaves based on colorshift()
        x,y = autogui.position()
        next(self.Colors_D).click()
        keyboard.press('space')
        for _ in range(3):
            autogui.moveTo(x,y)
            y-=1
        if side > 0:
            autogui.moveTo(x,y)
            y-=1
        autogui.moveTo(x, y)
        self.colorshift() #leaf color
        autogui.moveTo(x-side,y)
        autogui.moveTo(x+side,y)
        autogui.moveTo(x,y-1)
        y = y - 1
        autogui.moveTo(x-side,y)
        autogui.moveTo(x+side,y)
        autogui.moveTo(x,y-1)
        if side > 0:
            y -= 1
            autogui.moveTo(x-side,y)
            autogui.moveTo(x+side,y)
            autogui.moveTo(x,y-1)
        keyboard.release('space')    
    
    def mongus(self,side): #draw an among us character
        if self.lastside2 == side:
            side = -side
        next(self.Colors_ALL).click()
        x,y = autogui.position()
        keyboard.press('space')
        for _ in range(2):
            autogui.moveTo(x, y)
            autogui.moveTo(x+side+side, y)
            y -= 1
        for _ in range(2):
            autogui.moveTo(x, y)
            autogui.moveTo(x, y+1)
            x += side
        y += 2
        for _ in range(2):
            autogui.moveTo(x, y)
            autogui.moveTo(x+side, y-2)
            y -= 1
        for _ in range(2):
            autogui.moveTo(x, y)
            y -= 1
        for _ in range(3):
            autogui.moveTo(x, y)
            x -= side
        x += side*2
        y += 1
        autogui.moveTo(x,y)
        self.color_dict.get("blue7").click()
        autogui.moveTo(x-side,y)
        autogui.moveTo(x-side,y)
        keyboard.release('space')
        self.lastside2 = side

def print_Controls():
    print ("""
    -Controls-')
    Q: Cycle through all colors.
    WASD: cycles different color palletes depending on which combination you use, for example W + A is yellows.
    E: Draw an Among Us character, make sure your zoom level is 1 on pixelplace. Note: it only works when you are moving your mouse cursor slighty when you press it.
    For random drawing, press Y on the top left of your zone, and U on the bottom left then use either R to draw random trees or K to draw random Among Us characters.
    J: hold J to stop drawing random trees or Among Us characters.
    ESC: hold Escape to halt the script.
    """)
    

### Controls Section ###
def mouse_handler(Bot):
    x, y = autogui.position()
    if keyboard.is_pressed("q"):
        next(Bot.Colors_ALL).click
    if keyboard.is_pressed("e"):
        Bot.mongus()
    if keyboard.is_pressed("w") == True or keyboard.is_pressed("a") == True or keyboard.is_pressed("s") == True or keyboard.is_pressed("d") == True: #this activates on any combination of WASD and is how you change colors fast
        Bot.rainbowbrush()
    #these next two hotkeys are needed to set your square for random tree and among us drawing, first press Y for your top left corner, and then U for your bottom left corner
    #and then you can use R to draw random trees or K to draw random Among Us characters
    if keyboard.is_pressed("y"):
        tX, tY = autogui.position()
    if keyboard.is_pressed("u"):
        bX, bY = autogui.position()
    if keyboard.is_pressed("r"):#random tree, make sure your zoom is at 1 or won't scale correctly
        while True:
            side = int(random.choice(["-1","1"]))
            x = random.randrange(tX,bX)
            y = random.randrange(tY,bY)
            autogui.moveTo(x,y)
            pixx = autogui.pixel(x+side, y+side)
            pixx2 = autogui.pixel(x-side*4, y-5)
            if pixx != (204,204,204) and pixx2 != (204,204,204): #makes sure you aren't trying to start your drawing on the ocean
                if random.random() > 0.75:
                    Bot.tree_2()
                else:
                    Bot.tree_1()
            else:                
                pass                
            if keyboard.is_pressed("j"):#hold down on J to end the random drawing
                break        
    if keyboard.is_pressed("k"):#random amongus, make sure your zoom is at 1 or won't scale correctly
        while True:
            side = int(random.choice(["-1","1"]))
            x = random.randrange(tX,bX)
            y = random.randrange(tY,bY)
            autogui.moveTo(x,y)
            pixx = autogui.pixel(x+side, y+side)
            pixx2 = autogui.pixel(x-side*4, y-5)
            if pixx != (204,204,204) and pixx2 != (204,204,204): #makes sure you aren't trying to start your drawing on the ocean
                Bot.mongus()
            else:                
                pass                
            if keyboard.is_pressed("j"):#hold down on J to end the random drawing
                break
    if keyboard.is_pressed('esc'):#hold esc to halt the script in case of emergency, you will need to run the script again to use it again if you do this
        mouse.unhook(mouse_handler)
        quit()
### End Controls ##        

### program starting now ###
Thing = Bot()
print_Controls()
mouse.hook(mouse_handler(Thing))
