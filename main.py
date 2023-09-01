import random
import time

import pyautogui
import Game
import pygetwindow as gw
from PIL import ImageGrab
from ImageHandling import PixelMatch
from HelperFunctions import *

game = Game.Emulation()
kh = KeyboardHandling.KeyboardHandler(game)
helper = Helper(game)

frame = 0
window = gw.getWindowsWithTitle("Desmume SDL")[0]


DIALOGUE_ARROW = PixelMatch(245, 174, 255, 255, 255)
DIALOGUE_BROWN = PixelMatch(7, 174, 148, 115, 90)


def getScreenshot():
    if not window.isActive:
        window.activate()
    return ImageGrab.grab((window.left + 8, window.top + 31, window.right - 8, window.bottom - 8))


option = 0
while not game.window.has_quit():
    before = time.time_ns()

    game.window.process_input()
    frame += 1
    game.emu.cycle(False)
    game.window.draw()
    if frame == 1500:
        helper.navigateMenu(0)
    if frame == 1800 or frame == 2400 or frame == 3000:
        helper.exitMenu(option)
    if frame == 2100:
        option = helper.navigateMenu(1)
    if frame == 2700:
        option = helper.navigateMenu(3)
    after = time.time_ns()
    secs = 1 / 60 - (after - before) / 1000000000
    if secs > 0:
        time.sleep(secs)
