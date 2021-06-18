import sys

import multitasking
from lib import measure, WindowCore, WindowsBox
import pygame, pygetwindow, win32gui, win32con
class __window__:
    def __init__(self, wintitle, Surface) -> None:
        self.button = WindowCore.button(Surface)
        self.edge = WindowCore.edge(
            WindowCore.titlebar(
                0, 0,
                measure.title_button, 22,
                Surface,
                (47, 49, 54)
            )
        )
        self.title = wintitle
def find(name):
    try:
        return pygetwindow.getWindowsWithTitle(name)[0]
    except:
        WindowsBox.error('"'+ name+'" not found', 'Window Error')
        sys.exit()
'''def show(insert, FakeDisTitle, RealDisTitle, x, y, w, h):
    def screen_refresh(x, y, w, h, WindowTitle, mode):
        win32gui.SetWindowPos(
            win32gui.FindWindow(None, WindowTitle), mode, 
            x, y, w, h,
            pygame.RESIZABLE|pygame.NOFRAME
        )
    if insert:
        screen_refresh(x, y, w, h, RealDisTitle, win32con.HWND_NOTOPMOST)
        screen_refresh(x, y, w, h, FakeDisTitle, win32con.HWND_TOPMOST)
    pygame.display.set_mode(
        (
            w, h
        ),
        pygame.RESIZABLE|pygame.NOFRAME
    )
def hide(insert, core, RealDisTitle, x, y, w, h):
    def screen_refresh(x, y, w, h, WindowTitle, mode):
        win32gui.SetWindowPos(
            win32gui.FindWindow(None, WindowTitle), mode, 
            x, y, w, h,
            pygame.RESIZABLE|pygame.NOFRAME
        )
FakeDiscord    global 
    if insert:
        screen_refresh(x, y, w, h, RealDisTitle, win32con.HWND_TOPMOST)
        screen_refresh(x, y, w, h, core.title, win32con.HWND_NOTOPMOST)'''