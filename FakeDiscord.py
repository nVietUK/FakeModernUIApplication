#------------FakeDiscord.txt check----------------------------------
from lib import DiscordImageSave, WindowsBox, FileCheck
import os, sys
filename = 'FakeDiscord'
def inputcheck(x):
    if x.upper() == 'true'.upper():
        return True
    return False
cwd = os.getcwd()
try:
    settingfile = open(filename+'.txt', 'r',  encoding="utf-8")
    insert   = inputcheck(settingfile.readline().split(' ', 2)[2].replace("\n", ''))
    hotkey   = settingfile.readline().split(' ', 2)[2].replace("\n", '')
    Distitle = settingfile.readline().split(' ', 2)[2].replace("\n", '')
    wintitle = settingfile.readline().split(' ', 2)[2].replace("\n", '')
    DiscordImage = DiscordImageSave.__ava__()
    DiscordImage.ava1.noneactive = FileCheck.existent(
        settingfile.readline().split(' ', 2)[2].replace("\n", ''), 
        cwd, 'image/Avatar/macosx.png https://github.com/nVietUK/FakeModernUIApplication/raw/main/image/Avatar/macosx.png'
    )
    DiscordImage.ava1.active     = FileCheck.existent(
        settingfile.readline().split(' ', 2)[2].replace("\n", ''),
        cwd, 'image/Avatar/macos.png https://github.com/nVietUK/FakeModernUIApplication/raw/main/image/Avatar/macos.png'
    )
    DiscordImage.ava2.noneactive = FileCheck.existent(
        settingfile.readline().split(' ', 2)[2].replace("\n", ''),
        cwd, 'image/Avatar/windowsx.png https://github.com/nVietUK/FakeModernUIApplication/raw/main/image/Avatar/windowsx.png'
    )
    DiscordImage.ava2.active     = FileCheck.existent(
        settingfile.readline().split(' ', 2)[2].replace("\n", ''),
        cwd, 'image/Avatar/windows.png https://github.com/nVietUK/FakeModernUIApplication/raw/main/image/Avatar/windows.png'
    )
except:
    try:
        settingfile.close()
        WindowsBox.info(filename+ '.txt should be checked or deleted', 'File Error')
    except:
        createfile = open(filename+'.txt', 'w')
        createfile.write('insert = ')
        createfile.write('\nhotkey = ')
        createfile.write('\nRealDiscord.title = ')
        createfile.write('\nFakeDiscord.title =')
        createfile.write('\nDiscord.Avatar.1.NoneActive = ')
        createfile.write('\nDiscord.Avatar.1.Active = ')
        createfile.write('\nDiscord.Avatar.2.NoneActive = ')
        createfile.write('\nDiscord.Avatar.2.Active = ')
        WindowsBox.error(filename+".txt not found", "FakeModernUIApplication_Error")
        createfile.close()
    os.system('notepad.exe '+ os.getcwd()+'/'+filename+'.txt')
    sys.exit()
#----------------------------------------------------------------
from lib import window, titlebar
import pygame, pyaudio, numpy, win32gui, pygetwindow, win32ui, win32con, keyboard
#------------- file check -----------------------------------
FileCheck.resource('https://raw.githubusercontent.com/nVietUK/FakeModernUIApplication/main/Request.file', os.getcwd())
#------------------------------------------------------------
#------------------ hide window------------------------------
hide = False
def hidewindow():
    global hide
    hide = not hide
keyboard.add_hotkey(hotkey, hidewindow)
#-------------------------------------------------------------
pygame.init()
pygame.display.set_caption(wintitle)
FakeDiscord = pygame.display.set_mode(
    (530, 386),
    pygame.RESIZABLE|pygame.NOFRAME
)
pygame.display.set_icon(
    pygame.image.load(
        os.getcwd() + "/image/DiscordIcon/app.ico"
        )
    )
try:
    mic = pyaudio.PyAudio().open(format=pyaudio.paInt16,channels=1,rate=44100,input=True,frames_per_buffer=2048, input_device_index=1)
except:
    win32ui.MessageBox('There is no microphone', "FakeModernUIApplication_Error", win32con.MB_ICONINFORMATION|win32con.MB_OK)
core = window.__window__(wintitle, FakeDiscord)
if insert:
    Discord = pygetwindow.getWindowsWithTitle(Distitle)[0]
    x, y, w, h = Discord.topleft[0], Discord.topleft[1], Discord.size[0], Discord.size[1]
    win32gui.SetWindowPos(
        core.win32, win32con.HWND_TOPMOST, 
        x, y, w, h,
        pygame.RESIZABLE|pygame.NOFRAME
    )
    FakeDiscord = pygame.display.set_mode(
        (w, h),
        pygame.RESIZABLE|pygame.NOFRAME
    )
run = True
while run:
    #------------modern ui-------------------
    if win32gui.GetWindowText(win32gui.GetForegroundWindow()) == core.title:
        core.edge.check(core.screen)
    run = titlebar.process(core, FakeDiscord)
    run = True if run == 12 or run else False
    if not run or pygame.event.peek(pygame.QUIT) == True:
        break
    #----------------------------------------
    #---------------fake avatar--------------
        #---------------------- mic check -----------------------
    try:
        noise = int(numpy.average(numpy.abs(numpy.fromstring(mic.read(2048),dtype=numpy.int16))) // 10)
    except:
        noise = 1
        #--------------------------------------------------------
    if noise >= 30:
        ava1 = pygame.image.load(DiscordImage.ava1.active)
    else:
        ava1 = pygame.image.load(DiscordImage.ava1.noneactive)

    # thêm tính năng
    ava2 = pygame.image.load(DiscordImage.ava2.noneactive)

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
    #-------------------window refresh and change------------------------
    x, y, w, h = core.screen.topleft[0], core.screen.topleft[1], core.screen.size[0], core.screen.size[1]
    if not hide:
        window.refresh(
            insert, core, Distitle, 
            x, y, w, h
        )
    if hide:
        window.hide(
            insert, core, Distitle,
            x, y, w, h
        )
    #------------------------------------------------------------------
keyboard.wait()
if insert:
    win32gui.SetWindowPos(
        win32gui.FindWindow(None, Distitle),
        win32con.HWND_TOPMOST, 
        x, y, w, h,
        pygame.RESIZABLE|pygame.NOFRAME
    )