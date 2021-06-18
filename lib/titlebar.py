import pygame, win32api

def draw(core):
    core.edge.titlebar.draw()
    core.button.close.draw()
    core.button.maximize.draw()
    core.button.minimize.draw()
    core.button.Discord.draw()
def process(core):
    draw(core)
    if core.edge.titlebar.change:
        return True
    if core.button.close.check() and win32api.GetKeyState(0x01) in [-128, -127]:
        pygame.display.quit()
        return False
    if core.button.maximize.check() and win32api.GetKeyState(0x01) in [-128, -127]:
        core.screen.maximize()
    if core.button.minimize.check() and win32api.GetKeyState(0x01) in [-128, -127]:
        pygame.display.iconify()
    core.button.Discord.check()
    return True