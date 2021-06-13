from lib import window, titlebar, DiscordImageSave
import pygame, pyaudio, numpy, win32gui, win32con, pygetwindow, win32ui

pygame.init()
filename = 'FakeDiscord'
def inputcheck(x):
    if x.upper() == 'true'.upper():
        return True
    return False
try:
    settingfile = open(filename+'.txt', 'r',  encoding="utf-8")
    insert = inputcheck(settingfile.readline().split(' ', 2)[2].rstrip("\n"))
    Distitle = settingfile.readline().split(' ', 2)[2].rstrip("\n")
    wintitle = settingfile.readline().split(' ', 2)[2].rstrip("\n")
    DiscordImage = DiscordImageSave.__ava__()
    DiscordImage.ava1.noneactive = settingfile.readline().split(' ', 2)[2].rstrip("\n")
    DiscordImage.ava1.active     = settingfile.readline().split(' ', 2)[2].rstrip("\n")
    DiscordImage.ava2.noneactive = settingfile.readline().split(' ', 2)[2].rstrip("\n")
    DiscordImage.ava2.active     = settingfile.readline().split(' ', 2)[2].rstrip("\n")
except:
    try:
        open(filename+'.txt', 'r',  encoding="utf-8")
    except:
        createfile = open(filename+'.txt', 'w')
        createfile.write('insert = ')
        createfile.write('\nRealDiscord.title = ')
        createfile.write('\nFakeDiscord.title =')
        createfile.write('\nDiscord.Avatar.1.NoneActive = ')
        createfile.write('\nDiscord.Avatar.1.Active = ')
        createfile.write('\nDiscord.Avatar.2.NoneActive = ')
        createfile.write('\nDiscord.Avatar.2.Active = ')
    win32ui.MessageBox(filename+".txt not found or option is incorrect", "FakeModernUIApplication_Error", win32con.MB_ICONERROR)
    exit()
pygame.display.set_caption(wintitle)
FakeDiscord = pygame.display.set_mode(
    (
        530,
        386 
    ),
    pygame.RESIZABLE|pygame.NOFRAME
)
try:
    mic = pyaudio.PyAudio().open(format=pyaudio.paInt16,channels=1,rate=44100,input=True,frames_per_buffer=2048, input_device_index=1)
except:
    print('No microphone detected')
core = window.__window__(wintitle, FakeDiscord)
if insert:
    Discord = pygetwindow.getWindowsWithTitle(Distitle)[0]
    x, y, w, h = Discord.topleft[0], Discord.topleft[1], Discord.size[0], Discord.size[1]
    win32gui.SetWindowPos(
        core.win32, win32con.HWND_TOPMOST, 
        x, y, w, h,
        pygame.RESIZABLE|pygame.NOFRAME
    )
run = True
while run:
    if insert:
        x, y, w, h = core.screen.topleft[0], core.screen.topleft[1], core.screen.size[0], core.screen.size[1]
        win32gui.SetWindowPos(
            core.win32, win32con.HWND_TOPMOST, 
            x, y, w, h,
            pygame.RESIZABLE|pygame.NOFRAME
        )
        win32gui.SetWindowPos(
            win32gui.FindWindow(None, Distitle),
            win32con.HWND_NOTOPMOST, 
            x+ 25, y+25, w - 50, h- 50,
            pygame.RESIZABLE|pygame.NOFRAME
        )
    #-------------pygame screen sync window screen------------------
    FakeDiscord = pygame.display.set_mode(
        core.screen.size,
        pygame.RESIZABLE|pygame.NOFRAME
    )
    #---------------------------------------------------------------

    #------------modern ui-------------------
    core.edge.check(core)
    for event in pygame.event.get():
        run = titlebar.process(core, FakeDiscord)
        if event.type == pygame.quit or not run:
            run = False
            break
    if not run: break
        
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

    pygame.display.update()
if insert:
    win32gui.SetWindowPos(
        win32gui.FindWindow(None, Distitle),
        win32con.HWND_TOPMOST, 
        x, y, w, h,
        pygame.RESIZABLE|pygame.NOFRAME
    )