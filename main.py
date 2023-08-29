from desmume.emulator import DeSmuME

emu = DeSmuME()
emu.open("rom/Pokemon Platinum.nds")

window = emu.create_sdl_window()

while not window.has_quit():
    window.process_input()
    emu.cycle(False)
    window.draw()
