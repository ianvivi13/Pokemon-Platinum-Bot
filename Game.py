from desmume.emulator import DeSmuME


class Emulation:
    def __init__(self):
        self.emu = DeSmuME()
        self.emu.open("rom/Pokemon Platinum.nds")
        self.window = self.emu.create_sdl_window()

    def getGame(self):
        return self.emu

    def getWindow(self):
        return self.window

