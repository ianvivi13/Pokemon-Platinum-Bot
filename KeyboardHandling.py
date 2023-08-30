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
        self.game.emu.cycle(False)
        self.game.window.draw()
        self.game.emu.cycle(False)
        self.game.window.draw()
        self.releaseKey(key)

    def tapScreen(self, x, y):
        self.game.emu.input.touch_set_pos(x, y)
        self.game.emu.cycle(False)
        self.game.window.draw()
        self.game.emu.cycle(False)
        self.game.window.draw()
        self.game.emu.input.touch_release()
