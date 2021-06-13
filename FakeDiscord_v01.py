from os import fdopen
from tkinter.constants import N
import pygame
import pyaudio
import numpy
from pygame.constants import SYSTEM_CURSOR_SIZEWE 
import pygetwindow
import pyautogui
import win32api

pygame.init()
Wmouse = 0
wintitle = "Discord - cơm tró 5.0"
pygame.display.set_caption(
    wintitle
)
run = True
FakeDiscord = pygame.display.set_mode(
    (
        530,
        386 
    ),
    pygame.RESIZABLE|pygame.NOFRAME
)
class __mesure__():
    def __init__(self) -> None:
        pass
    def screen_wide(self):
        return pygame.display.get_surface().get_size()[0]
    def screen_height(self):
        return pygame.display.get_surface().get_size()[1]
    def title_button(self, x):
        return self.screen_wide() - (28* x)
mesure = __mesure__()
try:
    mic = pyaudio.PyAudio().open(format=pyaudio.paInt16,channels=1,rate=44100,input=True,frames_per_buffer=2048, input_device_index=1)
except:
    print('No microphone detected')
window = pygetwindow.getWindowsWithTitle(wintitle)[0]
class button:
    def __init__(self, x, y, color = (47, 49, 54), image = '', imagex = '', P = 0):
        self.x, self.y, self.w, self.h = x, y, 28, 22
        self.image = image
        self.imagex = imagex
        self.color = color
        self.p = P
    def check(self) -> bool:       
        try:
            x = self.x(self.p)
        except:
            x = self.x
        pygame.draw.rect(FakeDiscord, (47, 49, 54), ((x, self.y), (self.w, self.h)))    
        if x < pygame.mouse.get_pos()[0] and pygame.mouse.get_pos()[0] < x + self.w:
            if self.y < pygame.mouse.get_pos()[1] and pygame.mouse.get_pos()[1] < self.y + self.h:
                if self.imagex != '':
                    FakeDiscord.blit(self.imagex, (x, self.y))
                else:
                    pygame.draw.rect(FakeDiscord, self.color, (x, self.y, self.w, self.h))
                    if self.image != '':
                        FakeDiscord.blit(self.image, (x, self.y))
                return True
        if self.image != '':
            FakeDiscord.blit(self.image, (x, self.y))
        return False
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
        if x <= pygame.mouse.get_pos()[0] and pygame.mouse.get_pos()[0] <= x + w:
            if y <= pygame.mouse.get_pos()[1] and pygame.mouse.get_pos()[1] <= y + h:
                return True
        return False
class __titlebar__():
    def __init__(self, x, y, w, h):
        self.x, self.y, self.w, self.h = x, y, w, h
    def check(self) -> bool:
        pygame.draw.rect(FakeDiscord, (47, 49, 54), ((self.x, self.y), (self.w(), self.h)))    
        if self.x <= pygame.mouse.get_pos()[0] and pygame.mouse.get_pos()[0] <= self.x + self.w():
            if self.y <= pygame.mouse.get_pos()[1] and pygame.mouse.get_pos()[1] <= self.y + self.h:
                return True
        return False
class __window__:
    def __init__(self) -> None:
        #------- title bar setup --------------
        self.closebutton = button(
            mesure.title_button, 0, 
            (235, 64, 73),
            pygame.image.load('C:\\Users\\nVietUK\\Desktop\\FakeDiscord\\close.png'),
            pygame.image.load('C:\\Users\\nVietUK\\Desktop\\FakeDiscord\\closex.png'),
            1
        )  
        self.maximizebutton = button(
            mesure.title_button, 0,
            (52, 55, 60),
            pygame.image.load('C:\\Users\\nVietUK\\Desktop\\FakeDiscord\\maximize.png'), '',
            2
        )
        self.minimizebutton = button(
            mesure.title_button, 0,
            (52, 55, 60),
            pygame.image.load('C:\\Users\\nVietUK\\Desktop\\FakeDiscord\\minimize.png'), '',
            3
        )
        self.Discordbutton = button(
            0, 0, 
            (0, 0, 0), 
            pygame.image.load('C:\\Users\\nVietUK\\Desktop\\FakeDiscord\\Discord.png')
        )
        #--------------------------------------

        #----------screen edge setup-----------
        self.topedge = __edge__(
            0, 0,
            mesure.screen_wide, 1
        )
        self.leftedge = __edge__(
            0, 0,
            1, mesure.screen_height
        )
        self.rightedge = __edge__(
            mesure.screen_wide, 0,
            1, mesure.screen_height
        )
        self.bottomedge = __edge__(
            0, mesure.screen_height,
            mesure.screen_wide, 1
        )
        #--------------------------------------

        #---------title bar setup--------------
        self.TitleBar = __titlebar__(
            0, 0,
            mesure.screen_wide, 22
        )
        #--------------------------------------
FD = __window__()
while run:
    #-----------screen edge-------------------
    if FD.topedge.check() or FD.topedge.change:
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_SIZENS)
        if win32api.GetKeyState(0x01) in [-128, -127] and not FD.topedge.change:
            FD.topedge.change = True
            Wmouse = pyautogui.position()[1]
        if win32api.GetKeyState(0x01) not in [-128, -127]:
            FD.topedge.change = False
        if pyautogui.position()[1] != Wmouse and FD.topedge.change:
            Nmouse = pyautogui.position()[1]
            window.resizeTo(window.size[0], window.size[1] + (Wmouse - Nmouse))
            window.moveTo(window.left, window.top + (-1* (Wmouse - Nmouse)))
            Wmouse = Nmouse
    elif FD.leftedge.check() or FD.leftedge.change:
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_SIZEWE)
        if win32api.GetKeyState(0x01) in [-128, -127] and not FD.leftedge.change:
            FD.leftedge.change = True
            Wmouse = pyautogui.position()[0]
        if win32api.GetKeyState(0x01) not in [-128, -127]:
            FD.leftedge.change = False
        if pyautogui.position()[0] != Wmouse and FD.leftedge.change:
            Nmouse = pyautogui.position()[0]
            window.resizeTo(window.size[0] + (Wmouse - Nmouse), window.size[1])
            window.moveTo(window.left + (-1* (Wmouse - Nmouse)), window.top)
            Wmouse = Nmouse  
    elif FD.rightedge.check() or FD.rightedge.change:
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_SIZEWE)
        if win32api.GetKeyState(0x01) in [-128, -127] and not FD.rightedge.change:
            FD.rightedge.change = True
            Wmouse = pyautogui.position()[0]
        if win32api.GetKeyState(0x01) not in [-128, -127]:
            FD.rightedge.change = False
        if pyautogui.position()[0] != Wmouse and FD.rightedge.change:
            Nmouse = pyautogui.position()[0]
            window.resizeTo(window.size[0] - (Wmouse - Nmouse), window.size[1])
            Wmouse = Nmouse
    elif FD.bottomedge.check() or FD.bottomedge.change:
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_SIZENS)
        if win32api.GetKeyState(0x01) in [-128, -127] and not FD.bottomedge.change:
            FD.bottomedge.change = True
            Wmouse = pyautogui.position()[1]
        if win32api.GetKeyState(0x01) not in [-128, -127]:
            FD.bottomedge.change = False
        if pyautogui.position()[0] != Wmouse and FD.bottomedge.change:
            Nmouse = pyautogui.position()[1]
            window.resizeTo(window.size[0], window.size[1] + (Nmouse - Wmouse))
            Wmouse = Nmouse
    else:
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
    #-----------------------------------------

    #-------------pygame screen sync window screen------------------
    FakeDiscord = pygame.display.set_mode(
        window.size,
        pygame.RESIZABLE|pygame.NOFRAME
    )
    #---------------------------------------------------------------

    for event in pygame.event.get():
        if event.type == pygame.quit:
            run = False
            continue

        #---------- title bar --------------------  
        if FD.TitleBar.check() and event.type == pygame.MOUSEBUTTONDOWN:
            pass
        if FD.closebutton.check() and event.type == pygame.MOUSEBUTTONDOWN:
            run = False
            pygame.display.quit()
            continue
        if FD.maximizebutton.check() and event.type == pygame.MOUSEBUTTONDOWN:
            window.maximize()
        if FD.minimizebutton.check() and event.type == pygame.MOUSEBUTTONDOWN:
            pygame.display.iconify()
        FD.Discordbutton.check()
        #----------------------------------------
    if not run:
        continue

    #---------------fake avatar--------------

        #---------------------- mic check -----------------------
    try:
        noise = int(numpy.average(numpy.abs(numpy.fromstring(mic.read(2048),dtype=numpy.int16))) // 10)
    except:
        noise = 1
        #--------------------------------------------------------
    if noise >= 30:
        ava1 = pygame.image.load('C:\\Users\\nVietUK\\Desktop\\FakeDiscord\\vietuk.png')
    else:
        ava1 = pygame.image.load('C:\\Users\\nVietUK\\Desktop\\FakeDiscord\\vietukx.png')

    # thêm tính năng
    ava2 = pygame.image.load('C:\\Users\\nVietUK\\Desktop\\FakeDiscord\\tamtam.png')

    ava_width = pygame.display.get_surface().get_size()[0] // 2 - 16
    ava_height= ava1.get_height()* (pygame.display.get_surface().get_size()[0] // 2 - 16) // ava1.get_width()

    FakeDiscord.blit(
        pygame.transform.scale(ava1, (ava_width, ava_height)), 
        (
            8,
            (
                pygame.display.get_surface().get_size()[1] // 2 -
                ava_height // 2
            )
        )
    )

    FakeDiscord.blit(
        pygame.transform.scale(ava2, (ava_width, ava_height)),
        (
            pygame.display.get_surface().get_size()[0] // 2 + 8,
            (
                pygame.display.get_surface().get_size()[1] // 2 -
                ava_height // 2
            )
        )
    )
    #----------------------------------------

    pygame.display.update()