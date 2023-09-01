import time
from desmume.controls import Keys


class SleepManager:
    def __init__(self):
        self.time = time.time_ns()

    @staticmethod
    def calculateSec(start, end):
        return 1 / 60 - (end - start) / 1000000000

    def start(self):
        self.time = time.time_ns()

    def stop(self):
        stop = time.time_ns()
        secs = SleepManager.calculateSec(self.time, stop)
        if secs > 0:
            time.sleep(secs)


class Helper:
    def __init__(self, game, sleeper, kh):
        self.game = game
        self.kh = kh
        self.sleeper = sleeper

    def advanceFrame(self, funct, *args, num=2):
        self.sleeper.start()
        funct(*args)
        self.game.window.process_input()
        self.game.emu.cycle(False)
        self.game.window.draw()
        self.sleeper.stop()
        for i in range(0, num - 1):
            self.sleeper.start()
            self.game.window.process_input()
            self.game.emu.cycle(False)
            self.game.window.draw()
            self.sleeper.stop()

    def navigateMenu(self, option):
        self.advanceFrame(self.kh.tapKey, Keys.KEY_X)
        self.advanceFrame(self.kh.tapXTimes, Keys.KEY_DOWN, option, 2)
        self.advanceFrame(self.kh.tapKey, Keys.KEY_A)
        return option

    def exitMenu(self, option):
        self.advanceFrame(self.kh.tapKey, Keys.KEY_B, num=120)
        self.advanceFrame(self.kh.tapXTimes, Keys.KEY_UP, option, 2)
        self.advanceFrame(self.kh.tapKey, Keys.KEY_B)

    # UNTESTED
    def navigateBattleMenu(self, option):
        self.advanceFrame(self.kh.tapKey, Keys.KEY_A)
        for i in range(0, option):
            if i == 0:
                self.advanceFrame(self.kh.tapKey, Keys.KEY_DOWN)
            else:
                self.advanceFrame(self.kh.tapKey, Keys.KEY_RIGHT)
        self.advanceFrame(self.kh.tapKey, Keys.KEY_A)
        return option

    # UNTESTED
    def resetBattleMenu(self):
        self.advanceFrame(self.kh.tapXTimes, Keys.KEY_UP, 2)

    # UNTESTED
    def selectMonFromMenu(self, option):
        if option % 2 == 1:
            self.advanceFrame(self.kh.tapKey, Keys.KEY_RIGHT)
        self.advanceFrame(self.kh.tapXTimes, Keys.KEY_DOWN, (option // 2))
        self.advanceFrame(self.kh.tapKey, Keys.KEY_A)

