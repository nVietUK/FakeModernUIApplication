import pygame, win32api

def process(core, window):
    core.titlebar.draw()
    if core.button.close.check(window) and win32api.GetKeyState(0x01) in [-128, -127]:
        pygame.display.quit()
        return False
    if core.button.maximize.check(window) and win32api.GetKeyState(0x01) in [-128, -127]:
        core.screen.maximize()
    if core.button.minimize.check(window) and win32api.GetKeyState(0x01) in [-128, -127]:
        pygame.display.iconify()
    core.button.Discord.check(window)
    return True