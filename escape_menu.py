import pygame
import pygame as pg
from button_class import Button
from Menu_settings import Menu_settings

button_arr = []

def escape_menu(screen):
    pygame.init()
    width = 0
    height = 0
    button_arr.append(Button(screen, "Play", 2, 2.3, 56))
    button_arr.append(Button(screen, "Setting", 2, 1.9, 56))
    button_arr.append(Button(screen, "Main menu", 2, 1.6, 56))
    run = True
    size = [screen.get_width(), screen.get_height()]
    for i in button_arr:
        if i.backgr.get_rect().width > width:
            width = i.backgr.get_rect().width
        height += i.backgr.get_rect().height
    while run:
        screen.fill((148, 148, 148))
        if size != [screen.get_width(), screen.get_height()]:
            size = [screen.get_width(), screen.get_height()]
            width = 0
            height = 0
            for i in button_arr:
                if i.backgr.get_rect().width > width:
                    width = i.backgr.get_rect().width
                height += i.backgr.get_rect().height

        for event in pg.event.get():
            if event.type == pg.MOUSEBUTTONDOWN:
                for i in range(len(button_arr)):
                    if button_arr[i].text_rect.collidepoint(event.pos):
                        if event.button == 1:
                            button_arr[i].pressed = True

            elif event.type == pg.MOUSEBUTTONUP:
                for i in range(len(button_arr)):
                    if button_arr[i].text_rect.collidepoint(event.pos):
                        if event.button == 1:
                            button_arr[i].pressed = False
                            if i == 0:
                                run = False
                            if i == 1:
                                Menu_settings(screen)
                            if i == 2:
                                button_arr.clear()
                                return "1"
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    run = False
                    button_arr.clear()
                    return "0"
        pg.draw.rect(screen, (255, 255, 255), (screen.get_width()//2 - width//2, screen.get_height()//2 - height//2, width, height))
        for i in button_arr:
            i.draw()
        pygame.display.update()
    button_arr.clear()