from lib import measure, WindowCore, WindowsBox, titlebar
import pygetwindow, sys, threading, win32gui, pygame

class window:
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
def run(MainUI, FakeDisTitle, RealDisTitle, core, insert, WindowUI):
    def ModernUI(MainUI, FakeDisTitle, RealDisTitle, core, insert):
        #------------modern ui-------------------
        if win32gui.GetWindowText(win32gui.GetForegroundWindow()) == core.title:
            MainUI.shoot()
            core.edge.check(find(FakeDisTitle))
            run = titlebar.process(core)
            if not run: MainUI.shut(); return False
            try:
                titlebar.draw(core)
                if insert:
                    find(RealDisTitle).moveTo(
                        find(FakeDisTitle).left,
                        find(FakeDisTitle).top
                    )
                while MainUI.is_alive(): pass
                pygame.display.update()
            except: return False
        return True
        #----------------------------------------
    pygame.display.set_mode(
        find(FakeDisTitle).size,
        pygame.RESIZABLE|pygame.NOFRAME
    )
    return ModernUI(MainUI, FakeDisTitle, RealDisTitle, core, insert)