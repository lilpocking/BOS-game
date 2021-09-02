import pygame
from pygame.locals import *
from Menu_settings import Menu_settings
from test_level import test_level

class Buttons(pygame.sprite.Sprite):
    def __init__(self,image_path,cof_x,cof_y):
        super().__init__()
        self.orig_image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.orig_image, (int(self.orig_image.get_rect().width * screen.get_width()/1920) , int(self.orig_image.get_rect().height * screen.get_height()/1080)))
        self.rect = self.image.get_rect()
        self.rect.center = screen.get_width()//cof_x, screen.get_height()//cof_y
        self.cof_x, self.cof_y = cof_x, cof_y
        self.changed = False

    def draw(self):
        self.resize()
        screen.blit(self.image, self.rect)

    def resize(self):
        self.image = pygame.transform.scale(self.image, (int(self.orig_image.get_rect().width * screen.get_width() / 1920), int(self.orig_image.get_rect().height * screen.get_height() / 1080)))
        self.rect = self.image.get_rect()
        self.rect.center = screen.get_width() // self.cof_x, screen.get_height() // self.cof_y

    def update_image_from_event(self,image_path):
        self.image = pygame.image.load(image_path)
        self.resize()

    def get_rect(self):
        return self.rect


#SETTINGS OF APPLICATION
pygame.init()
clock = pygame.time.Clock()

#size of window application

width, height = [1920,1080]

f = open("settings.txt", 'r')
str = f.readline()
str = str[:-1]
str_temp = ""
for i in str:
    if i != "x":
        str_temp += i
        height = int(str_temp)
    else:
        width = int(str_temp)
        str_temp = ""

size = (width, height)
str = f.readline()
str = str[:-1]
if str == "On":
    screen = pygame.display.set_mode(size, pygame.HWSURFACE | pygame.DOUBLEBUF | FULLSCREEN)
else:
    screen = pygame.display.set_mode(size, pygame.HWSURFACE | pygame.DOUBLEBUF)
f.close()

#background menu settings
bg_menu_load = pygame.image.load("background/Main_menu_background.png")
bg_menu_file = pygame.transform.scale(bg_menu_load, size)
i = 0

#menu sound
#sound_in_menu = pygame.mixer.Sound("sounds/no_press_play_button.wav")

#display settings
pygame.display.set_icon(pygame.image.load("images/icon_of_BOS-play.png"))
pygame.display.set_caption("BOS-game")

#Buttons
button_play = Buttons("images/button_menu_play.png", 2, 2)
button_settings = Buttons("images/button_menu_settings.png", 2, 1.6)


while True:
    bg_menu_file = pygame.transform.scale(bg_menu_load, (screen.get_width(), screen.get_height()))
    screen.blit(bg_menu_file, (i, 0))
    screen.blit(bg_menu_file, (screen.get_width() + i, 0))
    if i <= -width:
        #screen.blit(bg_menu_file, (width + i, 0))
        i = 0
    i -= 1 * screen.get_width()/1920

    button_play.draw()
    button_settings.draw()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            quit()
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                quit()


        elif event.type == MOUSEBUTTONDOWN:
            if button_play.get_rect().collidepoint(event.pos):
                if event.button == 1:
                    button_play.update_image_from_event("images/button_menu_play_activated.png")
            elif button_settings.get_rect().collidepoint(event.pos):
                if event.button == 1:
                    button_settings.update_image_from_event("images/button_menu_settings_activated.png")

        elif event.type == MOUSEBUTTONUP:
            if button_play.get_rect().collidepoint(event.pos):
                if event.button == 1:
                    button_play.update_image_from_event("images/button_menu_play.png")
                    test_level(screen)
            elif button_settings.get_rect().collidepoint(event.pos):
                if event.button == 1:
                    button_settings.update_image_from_event("images/button_menu_settings.png")
                    Menu_settings(screen)

    if not(button_settings.get_rect().collidepoint(pygame.mouse.get_pos())):
        button_settings.update_image_from_event("images/button_menu_settings.png")
    if not(button_play.get_rect().collidepoint(pygame.mouse.get_pos())):
        button_play.update_image_from_event("images/button_menu_play.png")

    pygame.display.flip()
    clock.tick(60)
