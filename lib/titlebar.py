import pygame, win32api

def draw(core):
    core.edge.titlebar.draw()
    core.button.close.draw()
    core.button.maximize.draw()
    core.button.minimize.draw()
    core.button.Discord.draw()
def process(core):
    def check():
        if win32api.GetKeyState(0x01) in [-128, -127]:
            return True
        return False
    if core.edge.titlebar.change:
        return True
    if core.button.close.check() and check():
        return False
    elif core.button.maximize.check() and check():
        core.screen.maximize()
    elif core.button.minimize.check() and check():
        pygame.display.iconify()
    core.button.Discord.check()
    return True