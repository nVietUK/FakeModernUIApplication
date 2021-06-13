
import pygame

def screen_wide():
    return pygame.display.get_surface().get_size()[0]
def screen_height():
    return pygame.display.get_surface().get_size()[1]
def title_button(x = 3):
    return screen_wide() - (28* x)
def mouse_pos():
    #print(pygame.mouse.get_pos())
    return pygame.mouse.get_pos()