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
        WindowsBox.error(filename+".txt not found", "FakeModernUIApplication_Error")
        createfile.close()
    os.system('notepad.exe '+ os.getcwd()+'/'+filename+'.txt')
    sys.exit()
#----------------------------------------------------------------
from lib import window
import pygame, pygetwindow, keyboard
#------------- file check -----------------------------------
FileCheck.resource('https://raw.githubusercontent.com/nVietUK/FakeModernUIApplication/main/Request.file', os.getcwd())
try:
    import MyUI 
except:
    from lib import FileCheck
    WindowsBox.error('MyUI.py not found', 'Program Error')
    FileCheck.existent(
        settingfile.readline().split(' ', 2)[2].replace("\n", ''), 
        cwd, 'MyUI.py https://raw.githubusercontent.com/nVietUK/FakeModernUIApplication/main/MyUI.py'
    )
    sys.exit()
#------------------------------------------------------------
#------------------ hide window------------------------------
hide = False
def hidewindow():
    global hide
    hide = not hide
keyboard.add_hotkey(hotkey, hidewindow)
#-------------------------------------------------------------
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
core = window.window(FakeDisTitle, WindowUI)
run = True
obj = MyUI.MyUI()
while run:
    run = window.run(obj, FakeDisTitle, RealDisTitle, core, insert, WindowUI)