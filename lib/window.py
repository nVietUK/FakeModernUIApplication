from lib import measure, WindowCore, WindowsBox, titlebar
import pygetwindow, sys, win32gui, pygame

class window:
    def __init__(self, wintitle, Surface, Screen) -> None:
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
        self.Screen = Screen
def find(name):
    try:
        return pygetwindow.getWindowsWithTitle(name)[0]
    except:
        WindowsBox.error('"'+ name+'" not found', 'Window Error')
        sys.exit()
def run(MainUI, Edge, FakeDisTitle, RealDisTitle, core, insert, WindowUI, Interface):
    if not MainUI.is_alive(): MainUI.shoot()
    def ModernUI(MainUI, FakeDisTitle, RealDisTitle, core, insert, WindowUI, Interface):
        #------------modern ui-------------------
        mUI = Interface.surface
        titlebar.draw(core)
        if win32gui.GetWindowText(win32gui.GetForegroundWindow()) == core.title:
            run = titlebar.process(core)
            if not run: MainUI.shut(); return False
            titlebar.draw(core)
            if insert:
                find(RealDisTitle).moveTo(
                    find(FakeDisTitle).left,
                    find(FakeDisTitle).top
                )
        core.Screen.blit(
            WindowUI, (0, 0)
        )
        try: core.Screen.blit(
            mUI, (0, 22)
        )
        except: pass
        pygame.display.update()
        return True
        #----------------------------------------
    core.screen = pygame.display.set_mode(
        (530, 386),
        pygame.RESIZABLE|pygame.NOFRAME 
    )
    return ModernUI(MainUI, FakeDisTitle, RealDisTitle, core, insert, WindowUI, Interface)