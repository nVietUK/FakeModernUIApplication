from lib import DiscordImageSave, FileCheck, WindowsBox
import numpy, pygame, os, sys, pyaudio

class MyUI:
    def __init__(self, surface) -> None:
        filename = 'MyUI'
        self.surface = surface
        try:
            self.mic = pyaudio.PyAudio().open(format=pyaudio.paInt16,channels=1,rate=44100,input=True,frames_per_buffer=2048, input_device_index=1)
        except:
            WindowsBox.error('Microphone not found', 'System error')
            sys.exit()

        try:
            cwd = os.getcwd()
            settingfile = open(filename+'.txt', 'r',  encoding="utf-8")
            self.image = DiscordImageSave.__ava__()
            self.image.ava1.noneactive = FileCheck.existent(
                settingfile.readline().split(' ', 2)[2].replace("\n", ''), 
                cwd, 'image/Avatar/macosx.png https://github.com/nVietUK/FakeModernUIApplication/raw/main/image/Avatar/macosx.png'
            )
            self.image.ava1.active     = FileCheck.existent(
                settingfile.readline().split(' ', 2)[2].replace("\n", ''),
                cwd, 'image/Avatar/macos.png https://github.com/nVietUK/FakeModernUIApplication/raw/main/image/Avatar/macos.png'
            )
            self.image.ava2.noneactive = FileCheck.existent(
                settingfile.readline().split(' ', 2)[2].replace("\n", ''),
                cwd, 'image/Avatar/windowsx.png https://github.com/nVietUK/FakeModernUIApplication/raw/main/image/Avatar/windowsx.png'
            )
            self.image.ava2.active     = FileCheck.existent(
                settingfile.readline().split(' ', 2)[2].replace("\n", ''),
                cwd, 'image/Avatar/windows.png https://github.com/nVietUK/FakeModernUIApplication/raw/main/image/Avatar/windows.png'
            )
        except:
            try:
                settingfile.close()
                WindowsBox.info(filename+ '.txt should be checked or deleted', 'File Error')
            except:
                createfile = open(filename+'.txt', 'w')
                createfile.write('Discord.Avatar.1.NoneActive = ')
                createfile.write('\nDiscord.Avatar.1.Active = ')
                createfile.write('\nDiscord.Avatar.2.NoneActive = ')
                createfile.write('\nDiscord.Avatar.2.Active = ')
                WindowsBox.error(filename+".txt not found", "FakeModernUIApplication_Error")
                createfile.close()
                os.system('notepad.exe '+ os.getcwd()+'/'+filename+'.txt')
                sys.exit()
    def main(self):
        #---------------fake avatar--------------
            #---------------------- mic check -----------------------
        try:
            noise = int(numpy.average(numpy.abs(numpy.fromstring(self.mic.read(2048),dtype=numpy.int16))) // 10)
        except:
            noise = 1
            #--------------------------------------------------------
        if noise >= 30:
            ava1 = pygame.image.load(self.image.ava1.active)
        else:
            ava1 = pygame.image.load(self.image.ava1.noneactive)

        # thêm tính năng
        ava2 = pygame.image.load(self.image.ava2.noneactive)
        ava_width = pygame.display.get_surface().get_size()[0] // 2 - 16
        ava_height= ava1.get_height()* (pygame.display.get_surface().get_size()[0] // 2 - 16) // ava1.get_width()
        try:
            self.surface.blit(
                pygame.transform.scale(
                    ava1, (ava_width, ava_height)
                ), 
                (
                    8,
                    (
                        pygame.display.get_surface().get_size()[1] // 2 -
                        ava_height // 2
                    )
                )
            )
            self.surface.blit(
                pygame.transform.scale(
                    ava2, 
                    (ava_width, ava_height)
                ),
                (
                    pygame.display.get_surface().get_size()[0] // 2 + 8,
                    (
                        pygame.display.get_surface().get_size()[1] // 2 -
                        ava_height // 2
                    )
                )
            )
        except: sys.exit()
        #----------------------------------------