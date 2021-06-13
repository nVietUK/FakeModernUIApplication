import pygame, win32api

def process(core, window):
    core.edge.titlebar.draw()
    core.button.close.draw(window)
    core.button.maximize.draw(window)
    core.button.minimize.draw(window)
    core.button.Discord.draw(window)
    if core.edge.titlebar.change:
        return True
    if core.button.close.check(window) and win32api.GetKeyState(0x01) in [-128, -127]:
        pygame.display.quit()
        return False
    if core.button.maximize.check(window) and win32api.GetKeyState(0x01) in [-128, -127]:
        core.screen.maximize()
    if core.button.minimize.check(window) and win32api.GetKeyState(0x01) in [-128, -127]:
        pygame.display.iconify()
    core.button.Discord.check(window)
    return True