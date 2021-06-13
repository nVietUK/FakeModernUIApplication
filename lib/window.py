from lib import measure
from win32gui import GetWindowText, GetForegroundWindow
import pygame, pygetwindow, win32api, win32gui, pyautogui, os, win32con

class __button__:
    def __init__(self, x, y, color = (47, 49, 54), image = '', imagex = '', P = 0):
        self.x, self.y, self.w, self.h = x, y, 28, 22
        self.image = image
        self.imagex = imagex
        self.color = color
        self.p = P
    def first(self, input):
        try:
            x = input(self.p)
        except:
            x = input
        return x
    def check(self, screen) -> bool:       
        x = self.first(self.x)
        if x < measure.mouse_pos()[0] and measure.mouse_pos()[0] < x + self.w:
            if self.y < measure.mouse_pos()[1] and measure.mouse_pos()[1] < self.y + self.h:
                if self.imagex != '':
                    screen.blit(self.imagex, (x, self.y))
                else:
                    pygame.draw.rect(screen, self.color, (x, self.y, self.w, self.h))
                    if self.image != '':
                        screen.blit(self.image, (x, self.y))
                return True
        return False
    def draw(self, screen):
        x = self.first(self.x)
        pygame.draw.rect(screen, (47, 49, 54), ((x, self.y), (self.w, self.h)))   
        if self.image != '':
            screen.blit(self.image, (x, self.y))
class __edge__:
    def __init__(self, x, y, w, h):
        self.x, self.y, self.w, self.h = x, y, w, h
        self.change = False
    def check(self) -> bool:
        try:
            w = self.w()
        except:
            w = self.w
        try:
            h = self.h()
        except:
            h = self.h  
        try:
            x = self.x() -2
        except:
            x = self.x
        try:
            y = self.y() - 2
        except:
            y = self.y  
        if x <= measure.mouse_pos()[0] and measure.mouse_pos()[0] <= x + w:
            if y <= measure.mouse_pos()[1] and measure.mouse_pos()[1] <= y + h:
                return True
        return False
class titlebar():
    def __init__(self, x, y, w, h, window, screen):
        self.x, self.y, self.w, self.h = x, y, w, h
        self.change = False
        self.Wmouse = pyautogui.position()
        self.screen = screen
        self.window = window
    def draw(self):
        pygame.draw.rect(self.screen, (47, 49, 54), ((self.x, self.y), (self.w(), self.h))) 
    def check(self) -> bool: 
        if self.x <= measure.mouse_pos()[0] and measure.mouse_pos()[0] <= self.x + self.w():
            if self.y + 1 <= measure.mouse_pos()[1] and measure.mouse_pos()[1] <= self.y + self.h:
                return True
        return False
class button():
    def __init__(self) -> None:
        #------- title bar setup --------------
        self.close = __button__(
            measure.title_button, 0, 
            (235, 64, 73),
            pygame.image.load(os.getcwd() + '/image/TitleBar/close.png'),
            pygame.image.load(os.getcwd() + '/image/TitleBar/closex.png'),
            1
        )  
        self.maximize = __button__(
            measure.title_button, 0,
            (52, 55, 60),
            pygame.image.load(os.getcwd() + '/image/TitleBar/maximize.png'), '',
            2
        )
        self.minimize = __button__(
            measure.title_button, 0,
            (52, 55, 60),
            pygame.image.load(os.getcwd() + '/image/TitleBar/minimize.png'), '',
            3
        )
        self.Discord = __button__(
            0, 0, 
            (0, 0, 0), 
            pygame.image.load(os.getcwd() + '/image/TitleBar/Discord.png')
        )
        #--------------------------------------
class edge:
    def __init__(self) -> None:
        #----------screen edge setup-----------
        self.top = __edge__(
            0, 0,
            measure.screen_wide, 2
        )
        self.left = __edge__(
            0, 0,
            2, measure.screen_height
        )
        self.right = __edge__(
            measure.screen_wide, 0,
            2, measure.screen_height
        )
        self.bottom = __edge__(
            0, measure.screen_height,
            measure.screen_wide, 2
        )
        #--------------------------------------
        self.Wmouse = (0, 0)
    def change_check(self, core):
        if not self.top.change and not self.bottom.change and not self.left.change and not self.right.change and not core.titlebar.change:
            return True
        return False
    def check(self, core):
        window = core.screen
        if GetWindowText(GetForegroundWindow()) != core.title and self.change_check:
            return False
        if self.top.check() and self.change_check(core) or self.top.change:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_SIZENS)
            if win32api.GetKeyState(0x01) in [-128, -127] and not self.top.change:
                self.top.change = True
                self.Wmouse = pyautogui.position()[1]
            elif win32api.GetKeyState(0x01) not in [-128, -127]:
                self.top.change = False
            elif pyautogui.position()[1] != self.Wmouse and self.top.change:
                Nmouse = pyautogui.position()[1]
                window.resizeTo(window.size[0], window.size[1] + (self.Wmouse - Nmouse))
                window.moveTo(window.left, window.top + (-1* (self.Wmouse - Nmouse)))
                self.Wmouse = Nmouse
            return True
        elif self.left.check() and self.change_check(core) or self.left.change:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_SIZEWE)
            if win32api.GetKeyState(0x01) in [-128, -127] and not self.left.change:
                self.left.change = True
                self.Wmouse = pyautogui.position()[0]
            elif win32api.GetKeyState(0x01) not in [-128, -127]:
                self.left.change = False
            elif pyautogui.position()[0] != self.Wmouse and self.left.change:
                Nmouse = pyautogui.position()[0]
                window.resizeTo(window.size[0] + (self.Wmouse - Nmouse), window.size[1])
                window.moveTo(window.left + (-1* (self.Wmouse - Nmouse)), window.top)
                self.Wmouse = Nmouse  
            return True
        elif self.right.check() and self.change_check(core) or self.right.change:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_SIZEWE)
            if win32api.GetKeyState(0x01) in [-128, -127] and not self.right.change:
                self.right.change = True
                self.Wmouse = pyautogui.position()[0]
            elif win32api.GetKeyState(0x01) not in [-128, -127]:
                self.right.change = False
            elif pyautogui.position()[0] != self.Wmouse and self.right.change:
                Nmouse = pyautogui.position()[0]
                window.resizeTo(window.size[0] - (self.Wmouse - Nmouse), window.size[1]) 
                self.Wmouse = Nmouse
            return True
        elif self.bottom.check() and self.change_check(core) or self.bottom.change:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_SIZENS)
            if win32api.GetKeyState(0x01) in [-128, -127] and not self.bottom.change:
                self.bottom.change = True
                self.Wmouse = pyautogui.position()[1]
            elif win32api.GetKeyState(0x01) not in [-128, -127]:
                self.bottom.change = False
            elif pyautogui.position()[0] != self.Wmouse and self.bottom.change:
                Nmouse = pyautogui.position()[1]
                window.resizeTo(window.size[0], window.size[1] + (Nmouse - self.Wmouse))
                self.Wmouse = Nmouse
            return True
        elif core.titlebar.check() and self.change_check(core) or core.titlebar.change:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
            if win32api.GetKeyState(0x01) in [-128, -127] and not core.titlebar.change:
                core.titlebar.change = True
                self.Wmouse = pyautogui.position()
            elif win32api.GetKeyState(0x01) not in [-128, -127]:
                core.titlebar.change = False
            elif pyautogui.position() != self.Wmouse and core.titlebar.change:
                self.Nmouse = pyautogui.position()
                core.titlebar.window.move(
                    (-1* (self.Wmouse[0] - self.Nmouse[0])),
                    (-1* (self.Wmouse[1] - self.Nmouse[1]))
                )
                self.Wmouse = self.Nmouse
            return True
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
class __window__:
    def __init__(self, wintitle, window) -> None:
        self.button = button()
        self.screen = pygetwindow.getWindowsWithTitle(wintitle)[0]
        self.titlebar = titlebar(
            0, 0,
            measure.title_button, 22,
            self.screen, window
        )
        self.edge = edge()
        self.title = wintitle
        self.win32 = win32gui.FindWindow(None, wintitle)
def refresh(insert, core, Distitle, FakeDiscord, x, y, w, h):
    pygame.display.update()
    if insert:
        win32gui.SetWindowPos(
            core.win32, win32con.HWND_TOPMOST, 
            x, y, w, h,
            pygame.RESIZABLE|pygame.NOFRAME
        )
        win32gui.SetWindowPos(
            win32gui.FindWindow(None, Distitle),
            win32con.HWND_NOTOPMOST, 
            x, y, w, h,
            pygame.RESIZABLE|pygame.NOFRAME
        )
    FakeDiscord = pygame.display.set_mode(
        (
            w, h
        ),
        pygame.RESIZABLE|pygame.NOFRAME
    )