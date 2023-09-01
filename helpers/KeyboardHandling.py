from desmume.controls import keymask


class KeyboardHandler:
    def __init__(self, game, sleeper):
        self.game = game
        self.sleeper = sleeper

    def pressKey(self, key):
        self.game.emu.input.keypad_add_key(keymask(key))

    def releaseKey(self, key):
        self.game.emu.input.keypad_rm_key(keymask(key))

    def tapKey(self, key):
        self.pressKey(key)
        for i in range(0, 5):
            self.sleeper.start()

            self.game.emu.cycle(False)
            self.game.window.draw()

            self.sleeper.stop()
        self.releaseKey(key)

    def tapXTimes(self, key, x, num=2):
        for i in range(0, x):
            self.tapKey(key)
            for j in range(0, num):
                self.sleeper.start()

                self.game.emu.cycle(False)
                self.game.window.draw()

                self.sleeper.stop()
