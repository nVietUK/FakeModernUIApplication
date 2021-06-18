#------------WindowUI.txt check----------------------------------
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
    RealDisTitle = settingfile.readline().split(' ', 2)[2].replace("\n", '')
    FakeDisTitle = settingfile.readline().split(' ', 2)[2].replace("\n", '')
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
import pygame, pyaudio, numpy, win32gui, pygetwindow, win32ui, win32con, keyboard, multitasking
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
try:
    mic = pyaudio.PyAudio().open(format=pyaudio.paInt16,channels=1,rate=44100,input=True,frames_per_buffer=2048, input_device_index=1)
except:
    WindowsBox.error('Microphone not found', 'System error')
    sys.exit()
if insert:
    try:
        RealDiscord = pygetwindow.getWindowsWithTitle(RealDisTitle)[0]
    except:
        WindowsBox.error(RealDisTitle+' not found', filename+'.txt error')
        sys.exit()
    x, y, w, h = RealDiscord.topleft[0], RealDiscord.topleft[1], RealDiscord.size[0], RealDiscord.size[1]
#----------------- pygame --------------------------------
pygame.init()
pygame.display.set_caption(FakeDisTitle)
WindowUI = pygame.display.set_mode(
    (530, 386),
    pygame.RESIZABLE|pygame.NOFRAME
)
pygame.display.set_icon(
    pygame.image.load(
        os.getcwd() + "/image/DiscordIcon/app.ico"
        )
    )
#--------------------------------------------------------
core = window.__window__(FakeDisTitle, WindowUI)
run = True
def WindowChange():
    def ModernUI():
        global run, core, WindowUI
        #------------modern ui-------------------
        if win32gui.GetWindowText(win32gui.GetForegroundWindow()) == core.title:
            core.edge.check(window.find(FakeDisTitle))
            if insert:
                window.find(RealDisTitle).moveTo(
                    window.find(FakeDisTitle).left,
                    window.find(FakeDisTitle).top
                )
        run = titlebar.process(core)
        run = True if run == 12 or run else False
        if not run or pygame.event.peek(pygame.QUIT) == True:
            run = False
            return False
        else:
            pygame.display.update()
        return True
    #----------------------------------------
    global x, y, w, h, core, insert, RealDisTitle
    if not ModernUI(): return
    pygame.display.set_mode(
        window.find(FakeDisTitle).size,
        pygame.RESIZABLE|pygame.NOFRAME
    )
    #-------------------window refresh and change------------------------
    '''x, y, w, h = core.screen.topleft[0], core.screen.topleft[1], core.screen.size[0], core.screen.size[1]
    if not hide:
        window.refresh(
            insert, core, RealDisTitle,
            x, y, w, h
        )
    if hide:
        window.hide(
            insert, core, RealDisTitle,
            x, y, w, h
        )'''
    #------------------------------------------------------------------
while run:
    WindowChange()
if insert:
    win32gui.SetWindowPos(
        win32gui.FindWindow(None, RealDisTitle),
        win32con.HWND_TOPMOST, 
        x, y, w, h,
        pygame.RESIZABLE|pygame.NOFRAME
    )