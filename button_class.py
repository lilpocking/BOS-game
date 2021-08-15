import pygame as pg
import numpy as np

class Button:
    def __init__(self, screen,text_of_button="Text", cof_x=2, cof_y=2, size_of_button=36):
        self.screen = screen

        self.text_of_button = text_of_button

        self.size_of_button =size_of_button
        self.font = pg.font.Font("font/font.ttf", int(size_of_button * self.screen.get_width() / 1920))
        self.text = self.font.render(text_of_button, False, [0, 0, 0])
        self.text_rect = self.text.get_rect()
        self.text_rect.center = (self.screen.get_width()//cof_x, self.screen.get_height()//cof_y)

        self.backgr = pg.surface.Surface((self.text_rect.width + 20, self.text_rect.height + 10))
        self.backgr.fill([255, 255, 255])
        self.backgr_rect = self.backgr.get_rect()
        self.backgr_rect.center = self.text_rect.center

        self.cof_x = cof_x
        self.cof_y = cof_y
        self.text_color = [0, 0, 0]
        self.backgr_color = [255, 255, 255]
        self.pressed = False
        self.size = [self.screen.get_width(), self.screen.get_height()]

    def resize(self):
        self.font = pg.font.Font("font/font.ttf", int(self.size_of_button * self.screen.get_width() / 1920))
        self.text = self.font.render(self.text_of_button, False, self.text_color)
        self.text_rect = self.text.get_rect()
        self.text_rect.center = (self.screen.get_width() // self.cof_x, self.screen.get_height() //self.cof_y)

        self.backgr = pg.surface.Surface((self.text_rect.width, self.text_rect.height))
        self.backgr.fill(self.backgr_color)
        self.backgr_rect = self.backgr.get_rect()
        self.backgr_rect.center = self.text_rect.center

    def draw(self):
        if self.size != [self.screen.get_width(), self.screen.get_height()]:
            self.size = [self.screen.get_width(), self.screen.get_height()]
            self.resize()

        if self.pressed:
            temp = np.array([45, 45, 45])
            color_temp = np.array(self.text_color)
            self.text = self.font.render(self.text_of_button, False, color_temp + temp)
            color_temp = np.array(self.backgr_color)
            self.backgr.fill(color_temp - temp)
        else:
            self.text = self.font.render(self.text_of_button, False, self.text_color)
            self.backgr.fill(self.backgr_color)
        self.screen.blit(self.backgr, self.backgr_rect)
        self.screen.blit(self.text, self.text_rect)

    def set_pressed(self, true_or_false):
        self.pressed = true_or_false
