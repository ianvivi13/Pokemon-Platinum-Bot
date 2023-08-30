import random
import Game
import KeyboardHandling
import pygetwindow as gw
from desmume.controls import Keys
from PIL import ImageGrab

game = Game.Emulation()
kh = KeyboardHandling.KeyboardHandler(game)

frame = 0
window = gw.getWindowsWithTitle("Desmume SDL")[0]


class PixelMatch:
    def __init__(self, x, y, r, g, b):
        self.pos = (x, y)
        self.rgb = (r, g, b)

    def test(self, image):
        return image.getpixel(self.pos) == self.rgb


MENU_ARROW = PixelMatch(245, 174, 255, 255, 255)
MENU_BROWN = PixelMatch(7, 174, 148, 115, 90)


def getScreenshot():
    if not window.isActive:
        window.activate()
    return ImageGrab.grab((window.left + 8, window.top + 31, window.right - 8, window.bottom - 8))


while not game.window.has_quit():

    game.window.process_input()
    frame += 1
    if frame % 150 == 0:
        screenshot = getScreenshot()
        # print(f"{MENU_ARROW.test(screenshot)} : {MENU_BROWN.test(screenshot)}")

        if MENU_ARROW.test(screenshot) and MENU_BROWN.test(screenshot):
            i = 1
        else:
            i = random.randint(1, 12)

        # screenshot().save(f"shot{frame}.png")

        if i == 1:
            kh.tapKey(Keys.KEY_A)
        elif i == 2:
            kh.tapKey(Keys.KEY_B)
        elif i == 3:
            kh.tapKey(Keys.KEY_X)
        elif i == 4:
            kh.tapKey(Keys.KEY_Y)
        elif i == 5:
            kh.tapKey(Keys.KEY_L)
        elif i == 6:
            kh.tapKey(Keys.KEY_R)
        elif i == 7:
            kh.tapKey(Keys.KEY_START)
        elif i == 8:
            kh.tapKey(Keys.KEY_SELECT)
        elif i == 9:
            kh.tapKey(Keys.KEY_UP)
        elif i == 10:
            kh.tapKey(Keys.KEY_DOWN)
        elif i == 11:
            kh.tapKey(Keys.KEY_LEFT)
        elif i == 12:
            kh.tapKey(Keys.KEY_RIGHT)
        # pyautogui.leftClick(duration=0.1)
        frame += 2

        # print(getScreenshot().getpixel((245, 174)))
        # print(f"shot{frame}.png: {str(pyautogui.position().x)}, {str(pyautogui.position().y)}")
        # print(str(window.topleft))
    game.emu.cycle(False)
    game.window.draw()
