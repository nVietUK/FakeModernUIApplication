from lib import measure
import pygame, win32api, pyautogui

class __button__:
    def __init__(self, x, y, image, imagex, Surface, P = 0):
        self.x, self.y, self.w, self.h = x, y, 28, 22
        self.image = image
        self.imagex = imagex
        self.Surface = Surface
        self.p = P
        self.drawI = self.image
    def first(self, input):
        try: x = input(self.p)
        except: x = input
        return x
    def check(self) -> bool:       
        x = self.first(self.x)
        if x < measure.mouse_pos()[0] and measure.mouse_pos()[0] < x + self.w:
            if self.y < measure.mouse_pos()[1] and measure.mouse_pos()[1] < self.y + self.h:
                self.drawI = self.imagex
                return True
        self.drawI = self.image
        return False
    def draw(self):
        x = self.first(self.x)
        pygame.draw.rect(self.Surface, (47, 49, 54), ((x, self.y), (self.w, self.h)))   
        self.Surface.blit(self.drawI, (x, self.y))
class __edge__:
    def __init__(self, x, y, w, h):
        self.x, self.y, self.w, self.h = x, y, w, h
        self.change = False
    def check(self) -> bool:
        try: w = self.w() 
        except: w = self.w
        try: h = self.h()
        except: h = self.h  
        try: x = self.x() - self.w
        except: x = self.x
        try: y = self.y() - self.h
        except: y = self.y  
        if x <= measure.mouse_pos()[0] and measure.mouse_pos()[0] <= x + w:
            if y <= measure.mouse_pos()[1] and measure.mouse_pos()[1] <= y + h:
                return True
        return False
class titlebar():
    def __init__(self, x, y, w, h, Surface, color):
        self.x, self.y, self.w, self.h = x, y, w, h
        self.change = False
        self.Surface = Surface
        self.color = color
    def draw(self):
        pygame.draw.rect(self.Surface, self.color, ((self.x, self.y), (self.w(), self.h))) 
    def check(self) -> bool: 
        if self.x <= measure.mouse_pos()[0] and measure.mouse_pos()[0] <= self.x + self.w():
            if self.y + 1 <= measure.mouse_pos()[1] and measure.mouse_pos()[1] <= self.y + self.h:
                return True
        return False
class button():
    def __init__(self, Surface) -> None:
        #------- title bar setup --------------
        self.close = __button__(
            measure.title_button, 0, 
            pygame.image.load('./image/TitleBar/close.png'),
            pygame.image.load('./image/TitleBar/closex.png'),
            Surface, 1
        )  
        self.maximize = __button__(
            measure.title_button, 0,
            pygame.image.load('./image/TitleBar/maximize.png'), 
            pygame.image.load('./image/TitleBar/maximizex.png'),
            Surface, 2
        )
        self.minimize = __button__(
            measure.title_button, 0,
            pygame.image.load('./image/TitleBar/minimize.png'), 
            pygame.image.load('./image/TitleBar/minimizex.png'),
            Surface, 3
        )
        self.Discord = __button__(
            0, 0, 
            pygame.image.load('./image/TitleBar/Discord.png'),
            pygame.image.load('./image/TitleBar/Discord.png'),
            Surface
        )
        #--------------------------------------
class edge:
    def __init__(self, titlebar) -> None:
        #----------screen edge setup-----------
        Thickness = 5
        self.top = __edge__(
            0, 0,
            measure.screen_wide, Thickness
        )
        self.left = __edge__(
            0, 0,
            Thickness, measure.screen_height
        )
        self.right = __edge__(
            measure.screen_wide, 0,
            Thickness, measure.screen_height
        )
        self.bottom = __edge__(
            0, measure.screen_height,
            measure.screen_wide, Thickness
        )
        self.titlebar = titlebar
        #--------------------------------------
        self.Wmouse = (0, 0)
    def Window_Change():
        pass # thêm phần thay đổi window
    def change_check(self):
        if not self.top.change and not self.bottom.change and not self.left.change and not self.right.change and not self.titlebar.change:
            return True
        return False
    def check(self, Window):
        if self.top.check() and self.change_check() or self.top.change:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_SIZENS)
            if win32api.GetKeyState(0x01) in [-128, -127] and not self.top.change:
                self.top.change = True
                self.Wmouse = pyautogui.position()[1]
            elif win32api.GetKeyState(0x01) not in [-128, -127]:
                self.top.change = False
            elif pyautogui.position()[1] != self.Wmouse and self.top.change:
                Nmouse = pyautogui.position()[1]
                Window.resizeTo(Window.size[0], Window.size[1] + (self.Wmouse - Nmouse))
                Window.moveTo(Window.left, Window.top + (-1* (self.Wmouse - Nmouse)))
                self.Wmouse = Nmouse
            return True
        elif self.left.check() and self.change_check() or self.left.change:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_SIZEWE)
            if win32api.GetKeyState(0x01) in [-128, -127] and not self.left.change:
                self.left.change = True
                self.Wmouse = pyautogui.position()[0]
            elif win32api.GetKeyState(0x01) not in [-128, -127]:
                self.left.change = False
            elif pyautogui.position()[0] != self.Wmouse and self.left.change:
                Nmouse = pyautogui.position()[0]
                Window.resizeTo(Window.size[0] + (self.Wmouse - Nmouse), Window.size[1])
                Window.moveTo(Window.left + (-1* (self.Wmouse - Nmouse)), Window.top)
                self.Wmouse = Nmouse  
            return True
        elif self.right.check() and self.change_check() or self.right.change:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_SIZEWE)
            if win32api.GetKeyState(0x01) in [-128, -127] and not self.right.change:
                self.right.change = True
                self.Wmouse = pyautogui.position()[0]
            elif win32api.GetKeyState(0x01) not in [-128, -127]:
                self.right.change = False
            elif pyautogui.position()[0] != self.Wmouse and self.right.change:
                Nmouse = pyautogui.position()[0]
                Window.resizeTo(Window.size[0] - (self.Wmouse - Nmouse), Window.size[1]) 
                self.Wmouse = Nmouse
            return True
        elif self.bottom.check() and self.change_check() or self.bottom.change:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_SIZENS)
            if win32api.GetKeyState(0x01) in [-128, -127] and not self.bottom.change:
                self.bottom.change = True
                self.Wmouse = pyautogui.position()[1]
            elif win32api.GetKeyState(0x01) not in [-128, -127]:
                self.bottom.change = False
            elif pyautogui.position()[0] != self.Wmouse and self.bottom.change:
                Nmouse = pyautogui.position()[1]
                Window.resizeTo(Window.size[0], Window.size[1] + (Nmouse - self.Wmouse))
                self.Wmouse = Nmouse
            return True
        elif self.titlebar.check() and self.change_check() or self.titlebar.change:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
            if win32api.GetKeyState(0x01) in [-128, -127] and not self.titlebar.change:
                self.titlebar.change = True
                self.Wmouse = pyautogui.position()
            elif win32api.GetKeyState(0x01) not in [-128, -127]:
                self.titlebar.change = False
            elif pyautogui.position() != self.Wmouse and self.titlebar.change:
                Nmouse = pyautogui.position()
                Window.move(
                    (-1* (self.Wmouse[0] - Nmouse[0])),
                    (-1* (self.Wmouse[1] - Nmouse[1]))
                )
                self.Wmouse = Nmouse
            return True
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)