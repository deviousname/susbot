#made by deviousname, someone better than me can clean this code up and improve upon it
#feel free to change it to suit your needs *you do not have permission to sell any code derived from this code: GNU Affero General Public License v3.0
import crewmate #this first import is where you store your username and password to login to Reddit(required), found in: crewmate.py
import pyautogui as p
import keyboard as k
import time as t
import random as r
import mouse as m
from selenium import webdriver
from selenium.webdriver.common.by import By
from itertools import cycle
#some vars for later:
cv0, cv1, cv2, cv3, cv4, cv5, cv6, cv7, cv8, z, vector, X, Y, thecolor, a1, a2, b1, b2, handler = 0,0,0,0,0,0,0,0,0,1,0,0,0,None, None, None, None, None, None
def reload_colors(): #in order for you to switch colors easily, these needed to be loaded properly
    global white,grey1,grey2,grey3,grey4,black,green1,green2,green3,green5,yellow1,yellow2,yellow3,yellow4,brown1,brown2,brown3,red1,red2,red3,brown4,peach1,peach2,peach3,pink1,pink2,pink3,pink4,blue1,blue2,blue3,blue4,blue5,blue6,blue7
    white = driver.find_elements_by_xpath('//*[@id="palette-buttons"]/a')[0]
    grey1 = driver.find_elements_by_xpath('//*[@id="palette-buttons"]/a')[1]
    grey2 = driver.find_elements_by_xpath('//*[@id="palette-buttons"]/a')[2]
    grey3 = driver.find_elements_by_xpath('//*[@id="palette-buttons"]/a')[3]
    grey4 = driver.find_elements_by_xpath('//*[@id="palette-buttons"]/a')[4]
    black = driver.find_elements_by_xpath('//*[@id="palette-buttons"]/a')[5]
    green1 = driver.find_elements_by_xpath('//*[@id="palette-buttons"]/a')[6]
    green2 = driver.find_elements_by_xpath('//*[@id="palette-buttons"]/a')[7]
    green3 = driver.find_elements_by_xpath('//*[@id="palette-buttons"]/a')[8]
    green5 = driver.find_elements_by_xpath('//*[@id="palette-buttons"]/a')[10]
    yellow1 = driver.find_elements_by_xpath('//*[@id="palette-buttons"]/a')[11]
    yellow2 = driver.find_elements_by_xpath('//*[@id="palette-buttons"]/a')[12]
    yellow3 = driver.find_elements_by_xpath('//*[@id="palette-buttons"]/a')[13]
    yellow4 = driver.find_elements_by_xpath('//*[@id="palette-buttons"]/a')[14]
    brown1 = driver.find_elements_by_xpath('//*[@id="palette-buttons"]/a')[15]
    brown2 = driver.find_elements_by_xpath('//*[@id="palette-buttons"]/a')[16]
    brown3 = driver.find_elements_by_xpath('//*[@id="palette-buttons"]/a')[17]
    red1 = driver.find_elements_by_xpath('//*[@id="palette-buttons"]/a')[18] 
    red2 = driver.find_elements_by_xpath('//*[@id="palette-buttons"]/a')[19]
    red3 = driver.find_elements_by_xpath('//*[@id="palette-buttons"]/a')[20]
    brown4 = driver.find_elements_by_xpath('//*[@id="palette-buttons"]/a')[22]
    peach1 = driver.find_elements_by_xpath('//*[@id="palette-buttons"]/a')[23]
    peach2 = driver.find_elements_by_xpath('//*[@id="palette-buttons"]/a')[24]
    peach3 = driver.find_elements_by_xpath('//*[@id="palette-buttons"]/a')[25]
    pink1 = driver.find_elements_by_xpath('//*[@id="palette-buttons"]/a')[26]
    pink2 = driver.find_elements_by_xpath('//*[@id="palette-buttons"]/a')[27]
    pink3 = driver.find_elements_by_xpath('//*[@id="palette-buttons"]/a')[28]
    pink4 = driver.find_elements_by_xpath('//*[@id="palette-buttons"]/a')[29]
    blue1 = driver.find_elements_by_xpath('//*[@id="palette-buttons"]/a')[31]
    blue2 = driver.find_elements_by_xpath('//*[@id="palette-buttons"]/a')[32]
    blue3 = driver.find_elements_by_xpath('//*[@id="palette-buttons"]/a')[33]
    blue4 = driver.find_elements_by_xpath('//*[@id="palette-buttons"]/a')[34]
    blue5 = driver.find_elements_by_xpath('//*[@id="palette-buttons"]/a')[35]
    blue6 = driver.find_elements_by_xpath('//*[@id="palette-buttons"]/a')[36]
    blue7 = driver.find_elements_by_xpath('//*[@id="palette-buttons"]/a')[37]    
#if you don't use Chrome and you use Firefox instead, change this to "driver = webdriver.Firefox()" You will also need to download firefox webdriver and keep in same folder as this script
driver = webdriver.Chrome() #you need chromedriver.exe in same folder and it needs to match the version of you Chrome you use: https://chromedriver.chromium.org/downloads
#login sequence, using Reddit, set your username and pass for Reddit in crewmate.py's variables 'username' and 'password'
print ('Logging in now through Reddit. If you get an error you may need to set your name and password in crewmate.py')
driver.get("https://www.reddit.com/login/?dest=https%3A%2F%2Fssl.reddit.com%2Fapi%2Fv1%2Fauthorize%3Fclient_id%3D5QBfS3MRclJUGQ%26redirect_uri%3Dhttps%253A%252F%252Fpixelplace.io%252Fapi%252Fsso.php%253Ftype%253D2%26response_type%3Dcode%26scope%3Didentity%26state%3Do8xod0a799lzqp9n80u8zdevoxuslyzc%26duration%3Dtemporary")
r0 = driver.find_element_by_id('loginUsername');r0.send_keys(crewmate.username)
r1 = driver.find_element_by_id('loginPassword');r1.send_keys(crewmate.password)
r3 = driver.find_elements_by_xpath('/html/body/div/main/div[1]/div/div[2]/form/fieldset')[4];r3.click();t.sleep(3)#change delay "t.sleep(3)" to suit your computer load speed
r4 = driver.find_elements_by_xpath('/html/body/div[3]/div/div[2]/form/div/input')[0];r4.click();t.sleep(2)#change delay "t.sleep(2)" to suit your computer load speed
#end login
print ('All done logging in, ready to paint.')
print ('-Controls-')
print ('Q: Cycle through all colors.')
print ('WASD: cycles different color palletes depending on which combination you use, for example W + A is yellows.')
print ('E: Draw an Among Us character, make sure your zoom level is 1 on pixelplace. Note: it only works when you are moving your mouse cursor slighty when you press it.')
print ('For random drawing, press Y on the top left of your zone, and U on the bottom left then use either R to draw random trees or K to draw random Among Us characters.')
print ('J: hold J to stop drawing random trees or Among Us characters.')
print ('ESC: hold Escape to halt the script.')
#setting up the colors for fast color switching:
reload_colors();colors = [white,grey1,grey2,grey3,grey4,black,green1,green2,
    green3,green5,yellow1,yellow2,yellow3,yellow4,
    brown1,brown2,brown3,red1,red2,red3,brown4,peach1,
    peach2,peach3,pink1,pink2,pink3,pink4,
    blue1,blue2,blue3,blue4,blue5,blue6,blue7];colors_cycle = cycle(colors)
def next_color(): #fast color switching
    global thecolor
    thecolor = next(colors_cycle)
    thecolor.click()        
def whichcolor8(): #all colors
    global cv8, thecolor
    if cv8 > 38:
        cv8 = 0
    if cv8 == 1:
        thecolor = white
    elif cv8 == 2:
        thecolor = grey1
    elif cv8 == 3:
        thecolor = grey2
    elif cv8 == 4:
        thecolor = grey3
    elif cv8 == 5:
        thecolor = grey4
    elif cv8 == 6:
        thecolor = black
    elif cv8 == 7:
        thecolor = green1
    elif cv8 == 8:
        thecolor = green2
    elif cv8 == 9:
        thecolor = green3
    elif cv8 == 10:
        thecolor = green5
    elif cv8 == 11:
        thecolor = yellow1
    elif cv8 == 12:
        thecolor = yellow2
    elif cv8 == 13:
        thecolor = yellow3
    elif cv8 == 14:
        thecolor = yellow4
    elif cv8 == 15:
        thecolor = brown1
    elif cv8 == 16:
        thecolor = brown2
    elif cv8 == 17:
        thecolor = brown3
    elif cv8 == 18:
        thecolor = red1
    elif cv8 == 19:
        thecolor = red2
    elif cv8 == 20:
        thecolor = red3
    elif cv8 == 21:
        thecolor = brown4
    elif cv8 == 22:
        thecolor = peach1
    elif cv8 == 23:
        thecolor = peach2
    elif cv8 == 24:
        thecolor = peach3
    elif cv8 == 25:
        thecolor = pink1
    elif cv8 == 26:
        thecolor = pink2
    elif cv8 == 27:
        thecolor = pink3
    elif cv8 == 28:
        thecolor = pink4
    elif cv8 == 29:
        thecolor = blue1
    elif cv8 == 30:
        thecolor = blue2
    elif cv8 == 31:
        thecolor = blue3
    elif cv8 == 32:
        thecolor = blue4
    elif cv8 == 33:
        thecolor = blue5
    elif cv8 == 34:
        thecolor = blue6
    elif cv8 == 35:
        thecolor = blue7
    cv8 += 1
    thecolor.click()
#these palettes are just smaller versions of whichcolor8(), feel free to change the colors to suit your needs, make sure to use the correct names though, example: thecolor = pink3
def whichcolor7(): # Blue colors, normally bound to S + A, rebind in control section further down
    global thecolor, cv7
    if cv7 > 7:
        cv7 = 0
    cv7 += 1
    if cv7 <= 1:
        thecolor = blue1
    elif cv7 == 2:
        thecolor = blue2
    elif cv7 == 3:
        thecolor = blue3
    elif cv7 == 4:
        thecolor = blue4
    elif cv7 == 5:
        thecolor = blue5
    elif cv7 == 6:
        thecolor = blue6
    elif cv7 == 7:
        thecolor = blue7
    thecolor.click()
def whichcolor6(): # black and white, S + D, rebind in control section further down
    global thecolor, cv6
    if cv6 > 2:
        cv6 = 0
    cv6 += 1
    if cv6 <= 1:
        thecolor = black
    elif cv6 == 2:
        thecolor = white
    thecolor.click()
def whichcolor5(): # tree trunk colors; D, rebind in control section further down
    global thecolor, cv5
    if cv5 > 7:
        cv5 = 0
    cv5 += 1
    if cv5 <= 1:
        thecolor = brown1
    elif cv5 == 2:
        thecolor = brown2
    elif cv5 == 3:
        thecolor = brown3
    elif cv5 == 4:
        thecolor = brown4
    elif cv5 == 5:
        thecolor = grey4
    elif cv5 == 6:
        thecolor = peach3
    elif cv5 == 7:
        thecolor = white
    thecolor.click()
def whichcolor4(): # dirt colors, W + D, rebind in control section further down
    global thecolor, cv4
    if cv4 > 4:
        cv4 = 0
    cv4 += 1
    if cv4 <= 1:
        thecolor = brown1
    elif cv4 == 2:
        thecolor = brown2
    elif cv4 == 3:
        thecolor = brown3
    elif cv4 == 4:
        thecolor = brown4
    thecolor.click()         
def whichcolor3(): # grey colors, W, rebind in control section further down
    global thecolor, cv3
    if cv3 > 4:
        cv3 = 0
    cv3 += 1
    if cv3 == 1:
        thecolor = grey4
    elif cv3 == 2:
        thecolor = grey3
    elif cv7 == 3:
        thecolor = grey2
    elif cv3 == 4:
        thecolor = grey1
    thecolor.click()
def whichcolor2(): # yellow colors, A + W, rebind in control section further down
    global thecolor, cv2
    if cv2 > 4:
        cv2 = 0
    cv2 += 1
    if cv2 <= 1:
        thecolor = yellow1
    elif cv2 == 2:
        thecolor = yellow2
    elif cv2 == 3:
        thecolor = yellow3
    elif cv2 == 4:
        thecolor = yellow4
    thecolor.click()
def whichcolor1(): # green colors, S + A, rebind in control section further down
    global thecolor, cv1
    if cv1 > 4:
        cv1 = 0
    cv1 += 1
    if cv1 <= 1:
        thecolor = green1
    elif cv1 == 2:
        thecolor = green2
    elif cv1 == 3:
        thecolor = green3
    elif cv1 == 4:
        thecolor = green5
    thecolor.click()
def whichcolor0(): # red colors, S, rebind in control section further down    
    global thecolor, cv0
    if cv0 > 3:
        cv0 = 0
    cv0 += 1
    if cv0 <= 1:
        thecolor = red1
    elif cv0 == 2:
        thecolor = red2
    elif cv0 == 3:
        thecolor = red3
    thecolor.click()
def rainbowbrush(): #this is how the keycombos work, for example if you press A and W it will run whichcolor2() aka the yellow colors
    global colorvector
    if k.is_pressed("s") == True or k.is_pressed("a") == True or k.is_pressed("w") == True or k.is_pressed("d") == True:        
        #only A
        if k.is_pressed("a") == True and k.is_pressed("s") != True and k.is_pressed("w") != True and k.is_pressed("d") != True:
            whichcolor1()
        #only S
        if k.is_pressed("s") == True and k.is_pressed("a") != True and k.is_pressed("w") != True and k.is_pressed("d") != True:
            whichcolor0()    
        #only AW
        if k.is_pressed("a") == True and k.is_pressed("w") == True and k.is_pressed("d") != True and k.is_pressed("s") != True:
            whichcolor2()
        #only W
        if k.is_pressed("w") == True and k.is_pressed("a") != True and k.is_pressed("s") != True and k.is_pressed("d") != True:
            whichcolor3()
        #only WD
        if k.is_pressed("w") == True and k.is_pressed("d") == True and k.is_pressed("s") != True and k.is_pressed("a") != True:
            whichcolor4()
        #only D
        if k.is_pressed("d") == True and k.is_pressed("s") != True and k.is_pressed("a") != True and k.is_pressed("w") != True:
            whichcolor5()
        #only DS
        if k.is_pressed("d") == True and k.is_pressed("s") == True and k.is_pressed("a") != True and k.is_pressed("w") != True:
            whichcolor6()
        #only SA
        if k.is_pressed("s") == True and k.is_pressed("a") == True and k.is_pressed("d") != True and k.is_pressed("w") != True:
            whichcolor7()            
def vectoring(): #for us in direction of trees and among us characters, among other things
    global X, Y, vector #note: not using small xy; using big XY
    vector += 1
    if vector >= 4:
        vector = 0        
def colorshift(): # this function is still a work in progress and you can set it in the controls, tree leafs are a good use for this, it paints the next color on the list after checking which color is under your mouse cursor
    global thecolor, pixy, z, x, y, vector    
    pixy = p.pixel(x + z, y - z) #check nearby pixel color    
    if pixy == (255,255,255):
        thecolor = grey1        
    elif pixy == (196,196,196):
        thecolor = grey2        
    elif pixy == (136,136,136):
        thecolor = grey3        
    elif pixy == (85,85,85):
        thecolor = grey4        
    elif pixy == (34,34,34):
        thecolor = black        
    elif pixy == (0,0,0):
        thecolor = green1        
    elif pixy == (0,102,0):
        thecolor = green2        
    elif pixy == (34,177,76):
        thecolor = green3    
    elif pixy == (81,225,25):
        thecolor = green5        
    elif pixy == (148,224,68):
        thecolor = yellow1        
    elif pixy == (251,255,91):
        thecolor = yellow2        
    elif pixy == (229,217,0):
        thecolor = yellow3        
    elif pixy == (230,190,12):
        thecolor = yellow4        
    elif pixy == (229,149,0):
        thecolor = brown1        
    elif pixy == (160,106,66):
        thecolor = brown2        
    elif pixy == (153,90,26):
        thecolor = brown3        
    elif pixy == (99,60,31):
        thecolor = red1        
    elif pixy == (107,0,0):
        thecolor = red2        
    elif pixy == (159,0,0):
        thecolor = red3        
    elif pixy == (255,57,4):
        thecolor = brown4        
    elif pixy == (187,79,0):
        thecolor = peach1        
    elif pixy == (255,117,95):
        thecolor = peach2        
    elif pixy == (255,196,159):
        thecolor = peach3        
    elif pixy == (255,223,204):
        thecolor = pink1        
    elif pixy == (255,167,209):
        thecolor = pink2        
    elif pixy == (207,110,228):
        thecolor = pink3        
    elif pixy == (236,8,236):
        thecolor = pink4        
    elif pixy == (81,0,255):
        thecolor = blue1        
    elif pixy == (2,7,99):
        thecolor = blue2        
    elif pixy == (0,0,234):
        thecolor = blue3        
    elif pixy == (4,75,255):
        thecolor = blue4        
    elif pixy == (101,131,207):
        thecolor = blue5        
    elif pixy == (54,186,255):
        thecolor = blue6        
    elif pixy == (0,131,199):
        thecolor = blue7        
    elif pixy == (69,255,200):
        thecolor = white
    else:
        pass        
    thecolor.click() #once it knows what color to click, clicks it     
def tree_2(): #palm tree
    global z, x, y, vector, thecolor # x, y for coords, z is for facing direction
    #lets get a vector variable for later
    vectoring() #returns 1, 2, 3, or 4
    brown1.click()
    k.press('space')
    #build the tree:
    if vector == 1 or vector == 2:
        #trunk start (2 x 3)
        for _ in range(2):
            p.moveTo(x,y)
            y -= 1
        x += z
        for _ in range(2):
            p.moveTo(x,y)
            y -= 1
        x += z
        for _ in range(2):
            p.moveTo(x,y)
            y -= 1
        y += 1
        # trunk end
    else:
        #trunk start (3 x 2)
        for _ in range(3):
            p.moveTo(x,y)
            y -= 1
        x += z
        for _ in range(3):
            p.moveTo(x,y)
            y -= 1
        y += 1            
        # trunk end        
    #draw the leaves:
    p.moveTo(x+z,y)
    whichcolor1()
    thecolor.click()
    p.moveTo(x-z,y)
    p.moveTo(x+z+z+z,y)
    p.moveTo(x-z-z-z,y)
    p.moveTo(x,y-1)
    p.moveTo(x-z,y-1)
    p.moveTo(x+z,y-1)
    p.moveTo(x-z*2,y-1)
    p.moveTo(x+z*2,y-1)
    p.moveTo(x,y-2)
    p.moveTo(x-z,y-2)
    p.moveTo(x+z,y-2)
    k.release('space')
    z = -z #invert z so the next tree faces the opposite direction
def tree_1(): #normal style tree that using every color for the leaves based on colorshift()
    global z, x, y, vector, thecolor
    vectoring()
    whichcolor5()#tree trunk colors
    p.moveTo(x,y)
    k.press('space')
    for _ in range(3):
        p.moveTo(x,y)
        y-=1
    if z > 0:
        for _ in range(1):
            p.moveTo(x,y)
            y-=1
    p.moveTo(x, y)
    colorshift() #leaf color, you can use whichcolor1() here for example or the other whichcolor() functions to change which color the leaves will be
    p.moveTo(x-z,y)
    p.moveTo(x+z,y)
    p.moveTo(x,y-1)
    y = y - 1
    p.moveTo(x-z,y)
    p.moveTo(x+z,y)
    p.moveTo(x,y-1)
    if z > 0:
        y -= 1
        p.moveTo(x-z,y)
        p.moveTo(x+z,y)
        p.moveTo(x,y-1)
    k.release('space')    
def mongus(): #everyones favorite, draw an among us character, facing either left or right, and the color it chooses can be set with whichcolor() or colorshift() or nextcolor()
    global z, thecolor, x, y
    whichcolor8()
    p.moveTo(x,y)
    k.press('space')
    for _ in range(2):
        p.moveTo(x, y)
        p.moveTo(x+z+z, y)
        y -= 1
    for _ in range(2):
        p.moveTo(x, y)
        p.moveTo(x, y+1)
        x += z
    y = y + 2
    for _ in range(2):
        p.moveTo(x, y)
        p.moveTo(x+z, y-2)
        y -= 1
    for _ in range(2):
        p.moveTo(x, y)
        y -= 1
    for _ in range(3):
        p.moveTo(x, y)
        x -= z
    x += z*2
    y += 1
    p.moveTo(x,y)
    blue7.click()
    p.moveTo(x-z,y)
    p.moveTo(x-z,y)
    k.release('space')
    z = -z #next amongus will face other direction if you invert z
### Controls Section ###
def mouse_handler(event):
    global x, y, z, tX, tY, bX, bY, a1, a2, handler, cx1, cx2, b1, b2, coords
    x, y = p.position()
    #this code is how to set your own hotkeys:
    if k.is_pressed("j"):  #set the hotkey like this. Note: use reload_colors() if you have changed pages before drawing again (doesnt work on different tabs)
        reload_colors()    #and the function you want it to run when you press the key
    #and the rest of the controls (add your own to this list if you want)
    if k.is_pressed("q"):
        next_color()        
    if k.is_pressed("e"): #draws an amongus character where your mouse is, make sure your zoom is at 1 or it will not scale properly
        mongus()
    if k.is_pressed("w") == True or k.is_pressed("a") == True or k.is_pressed("s") == True or k.is_pressed("d") == True: #this activates on any combination of WASD and is how you change colors fast
        rainbowbrush()
    #these next two hotkeys are needed to set your square for random tree and among us drawing, first press Y for your top left corner, and then U for your bottom left corner
    #and then you can use R to draw random trees or K to draw random Among Us characters
    if k.is_pressed("y"):
        tX, tY = p.position()
    if k.is_pressed("u"):
        bX, bY = p.position()
    if k.is_pressed("r"):#random tree, make sure your zoom is at 1 or won't scale correctly
        while True:
            if r.random() > 0.5:
                z = 1
            else:
                z = -1
            x = r.randrange(tX,bX)
            y = r.randrange(tY,bY)
            p.moveTo(x,y)
            pixx = p.pixel(x+z, y+z)
            pixx2 = p.pixel(x-z*4, y-5)
            if pixx != (204,204,204) and pixx2 != (204,204,204): #makes sure you aren't trying to start your drawing on the ocean
                if r.random() > 0.75:
                    tree_2()
                else:
                    tree_1()
            else:                
                pass                
            if k.is_pressed("j"):#hold down on J to end the random drawing
                break            
    if k.is_pressed("k"):#random amongus, make sure your zoom is at 1 or won't scale correctly
        while True:
            if r.random() > 0.5:
                z = 1
            else:
                z = -1
            x = r.randrange(tX,bX)
            y = r.randrange(tY,bY)
            p.moveTo(x,y)
            pixx = p.pixel(x+z, y+z)
            pixx2 = p.pixel(x-z*4, y-5)
            if pixx != (204,204,204) and pixx2 != (204,204,204): #makes sure you aren't trying to start your drawing on the ocean
                mongus()
            else:                
                pass                
            if k.is_pressed("j"):#hold down on J to end the random drawing
                break
    if k.is_pressed('esc'):#hold esc to halt the script in case of emergency, you will need to run the script again to use it again if you do this
        m.unhook(mouse_handler)
        quit()
### End Controls ##        
m.hook(mouse_handler)### program starting now ###
