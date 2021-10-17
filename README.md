# susbot for pixelplace.io, made by deviousname

It is probably best if you use Python 3.7.9 or the imposter will jump out of a vent and get you:

https://www.python.org/downloads/release/python-379/

-susbot works by opening an automated browser window and logging in through Reddit to bypass the CAPTCHA system of pixelplace.io-

If you do not have a Reddit account, you will need one in order to use susbot, otherwise you will need to rewrite the code to suit your non-Reddit needs.

If you use Chrome, you need to find the matching chromedriver.exe

chromedriver can be found here:  https://chromedriver.chromium.org/downloads

Firefox users should work too, and they will need to get their corresponding Firefox (geckodriver) driver.

Firefox drivers can be found here: https://github.com/mozilla/geckodriver/releases

To run it: right click on susbot_main.py and open with IDLE then press F5 to run. Doubleclicking the file does not work.


Also read this comment to set the driver in the code if you are using Firefox: https://github.com/deviousname/susbot/blob/be712780379d2fb0215220c59d3cbf306317b7c5/susbot_main.py#L52

Once you have the driver, simply copy and paste it into the same folder as susbot.

Set your Reddit name and password in crewmate.py and then run susbotmain.py

Note: while it is logging in don't click around or do anything, just wait for pixeplace.io to fully load in, and then you can use it.

If you switch maps in the main tab, you need to reload the colors by holding down "j" for a moment.

IMPORTANT: All the imports need to be installed, if you don't know how to do that, I reccomend looking up how pip install for Windows 10 Python 3.7.9 which is what I use.

For example to install pyautogui you open your command prompt and type: pip install pyautogui

Different system setups may have different syntax, good luck!

The full list of imports you need to install are:

pyautogui

(https://pyautogui.readthedocs.io/en/latest/)

keyboard

(https://pypi.org/project/keyboard/)

mouse

(https://pypi.org/project/mouse/)

selenium

(https://selenium-python.readthedocs.io/)

itertools

(https://docs.python.org/3/library/itertools.html)
