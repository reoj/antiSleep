#region Global Depandencies
import importlib.util
import sys
import random
import time
#endregion

#region Global Variables
dependency = 'pyautogui'
MAX_SCREEN_WIDTH = 1366
MAX_SCREEN_HEIGHT = 768
minutes = 0.1
openWindowsMenuEvery = 10
globalDisplacementDuration = 0.5
#endregion


#region Main Functions
def verifyDependencies():
    return importlib.util.find_spec(dependency) is not None


def loop():
    while True:
        for i in range(0, openWindowsMenuEvery):
            pointAtRandomPosition()
        openNCloseStartMenu()
#endregion


#region Helper Functions
def openNCloseStartMenu():
    import pyautogui
    pyautogui.press('win')
    time.sleep(1)
    pyautogui.press('win')


def pointAtRandomPosition():
    new_x, new_y = generateRandomPosition()
    setMousePosition(new_x, new_y)
    time.sleep(minutes * 60)


def setMousePosition(x, y):
    import pyautogui
    pyautogui.moveTo(x, y, duration=globalDisplacementDuration)


def generateRandomPosition():
    x = random.randint(0, MAX_SCREEN_WIDTH)
    y = random.randint(0, MAX_SCREEN_HEIGHT)
    return x, y
#endregion


# region Main Program
def main(args=None):
    if verifyDependencies():
        loop()
    else:
        print(f'\n\nPlease run "pip install {dependency}"\n')


if __name__ == '__main__':
    main()
# endregion