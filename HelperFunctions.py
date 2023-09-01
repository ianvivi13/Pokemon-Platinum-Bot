import time
import KeyboardHandling
from desmume.controls import keymask, Keys


class Helper:
    def __init__(self, game):
        self.game = game
        self.kh = KeyboardHandling.KeyboardHandler(game)

    def advanceFrame(self, before, after, num):
        addBefore = time.time_ns()
        for i in range(0, num):
            self.game.window.process_input()
            self.game.emu.cycle(False)
            self.game.window.draw()
            if i == 0:
                addAfter = time.time_ns()
                secs = 1 / 60 - (after + (addAfter - addBefore) - before) / 1000000000
                if secs > 0:
                    time.sleep(secs)
            else:
                addAfter = time.time_ns()
                secs = 1 / 60 - (addAfter - addBefore) / 1000000000
                if secs > 0:
                    time.sleep(secs)

    def navigateMenu(self, option):
        before = time.time_ns()
        self.kh.tapKey(Keys.KEY_X)
        after = time.time_ns()
        self.advanceFrame(before, after, 10)
        for i in range(0, option):
            before = time.time_ns()
            self.kh.tapKey(Keys.KEY_DOWN)
            after = time.time_ns()
            self.advanceFrame(before, after, 10)
        before = time.time_ns()
        self.kh.tapKey(Keys.KEY_A)
        after = time.time_ns()
        self.advanceFrame(before, after, 10)
        return option

    def exitMenu(self, option):
        before = time.time_ns()
        self.kh.tapKey(Keys.KEY_B)
        after = time.time_ns()
        self.advanceFrame(before, after, 120)
        for i in range(0, option):
            before = time.time_ns()
            self.kh.tapKey(Keys.KEY_UP)
            after = time.time_ns()
            self.advanceFrame(before, after, 10)
        before = time.time_ns()
        self.kh.tapKey(Keys.KEY_B)
        after = time.time_ns()
        self.advanceFrame(before, after, 10)
        return option
