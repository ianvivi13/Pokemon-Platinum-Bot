import time
from desmume.controls import keymask


class KeyboardHandler:
    def __init__(self, game):
        self.game = game

    def pressKey(self, key):
        self.game.emu.input.keypad_add_key(keymask(key))

    def releaseKey(self, key):
        self.game.emu.input.keypad_rm_key(keymask(key))

    def tapKey(self, key):
        self.pressKey(key)
        for i in range(0, 10):
            before = time.time_ns()

            self.game.emu.cycle(False)
            self.game.window.draw()

            after = time.time_ns()
            secs = 1 / 60 - (after - before) / 1000000000
            if secs > 0:
                time.sleep(secs)
        self.releaseKey(key)

    def tapScreen(self, x, y):
        self.game.emu.input.touch_set_pos(x, y)
        for i in range(0, 5):
            before = time.time_ns()

            self.game.emu.cycle(False)
            self.game.window.draw()

            after = time.time_ns()
            secs = 1 / 60 - (after - before) / 1000000000
            if secs > 0:
                time.sleep(secs)
        self.game.emu.input.touch_release()
