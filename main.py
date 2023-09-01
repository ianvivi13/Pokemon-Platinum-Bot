import Game
import pygetwindow as gw
from helpers.KeyboardHandling import *
from helpers.ImageHandling import *
from helpers.HelperFunctions import *

game = Game.Emulation()
sleeper = SleepManager()
kh = KeyboardHandler(game, sleeper)
helper = Helper(game, sleeper, kh)

window = gw.getWindowsWithTitle("Desmume SDL")[0]

DIALOGUE_ARROW = PixelMatch(245, 174, 255, 255, 255)
DIALOGUE_BROWN = PixelMatch(7, 174, 148, 115, 90)

frame = 0
option = 0

# Process game start
while not game.window.has_quit() and frame <= 3020:
    sleeper.start()

    game.window.process_input()
    frame += 1
    game.emu.cycle(False)
    game.window.draw()
    if frame % 60 == 0 and frame < 1500:
        kh.tapKey(Keys.KEY_A)
    if frame == 1500:
        helper.navigateMenu(0)
    if frame == 1800 or frame == 2400 or frame == 3000:
        helper.exitMenu(option)
    if frame == 2100:
        option = helper.navigateMenu(1)
    if frame == 2700:
        option = helper.navigateMenu(3)
    sleeper.stop()

# Process game loop
while not game.window.has_quit():
    sleeper.start()

    game.window.process_input()
    frame += 1
    game.emu.cycle(False)
    game.window.draw()
    # dodo

    sleeper.stop()
