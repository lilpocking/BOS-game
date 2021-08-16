import pygame
import serial
from pygame.locals import *
import serial.tools.list_ports

class Text():
    def __init__(self, screen, text='text', color=(0, 0, 0), cof_x=0, cof_y=0, smooth=False,selects={"select": None}, saved_key=""):

        # selected parametr and parametrs
        self.selects = selects # словарь параметров
        self.keys = list(selects.keys()) # массив ключей
        self.selected = 0
        if saved_key != "":
            for i in range(len(self.keys)):
                if saved_key == self.keys[i]:
                    self.selected = i # выбранный параметр
                    break

        # Text parametrs
        self.form = pygame.font.Font('font/font.ttf', int(36 * screen.get_width() / 1920))
        self.text = text
        self.text_on_screen = self.form.render(text + self.keys[self.selected], smooth, color)
        self.rect = self.text_on_screen.get_rect()
        self.rect.center = (screen.get_width()//cof_x, screen.get_height()//cof_y)

        # Other parametrs
        self.smooth = smooth
        self.screen = screen
        self.cof_x = cof_x
        self.cof_y = cof_y
        self.color = color
        self.select_changed = False

        self.check_screen_size = [screen.get_width(), screen.get_height()]

    def set_saved_key(self, saved_key):
        for i in range(len(self.keys)):
            if saved_key == self.keys[i]:
                self.selected = i  # выбранный параметр
                break
            else:
                self.selected = 0

    def correct_text(self):
        self.form = pygame.font.Font('font/font.ttf', int(36 * self.screen.get_width() / 1920))
        self.text_on_screen = self.form.render(self.text + self.keys[self.selected], self.smooth, self.color)
        self.rect = self.text_on_screen.get_rect()
        self.rect.center = (self.screen.get_width() // self.cof_x, self.screen.get_height() // self.cof_y)

    def draw(self):
        if [self.screen.get_width(),self.screen.get_height()] != self.check_screen_size:
            self.correct_text()
            self.check_screen_size = [self.screen.get_width(),self.screen.get_height()]
        if self.select_changed:
            self.correct_text()
            self.select_changed = False
        self.screen.blit(self.text_on_screen, self.rect)

    def change_selected(self, where=0):
        self.selected += where
        if self.selected >= len(self.keys):
            self.selected = 0
        if self.selected < 0:
            self.selected = len(self.keys) - 1
        self.select_changed = True

    def get_selected(self):
        return self.selects[self.keys[self.selected]]

    def append_selects(self, key, numbers):
        if self.selects == {"select": None}:
            self.selects.clear()
        self.selects[key] = []
        self.selects[key] = numbers

    def get_rect(self):
        return self.rect

def save_settings(save):
    f = open('settings.txt', 'w')
    for i in save:
        f.write(save[i].keys[save[i].selected] + '\n')
    f.close()



def Menu_settings(screen):
    bg_menu_load = pygame.image.load("background/Menu_settings.png")
    bg_menu_file = pygame.transform.scale(bg_menu_load, (screen.get_width(),screen.get_height()))
    run = True
    text_colore = (245,245,245)
    save = []
    clock = pygame.time.Clock()



    list = serial.tools.list_ports.comports()
    element = {}
    for i in list:
        element[str(i.device)] = []
        element[str(i.device)].append(str(i.device))



    with open("settings.txt", "r") as file:
        while True:
            line = file.readline()
            if not line:
                break
            save.append(line[0:-1])




    text_window_size = Text(
        screen,
        'Window size:        ',
        text_colore,
        2,
        5.3,
        selects={
           "1920x1080": (1920,1080),
            "1600x900": (1600, 900),
            "1366x768": (1366, 768),
           "1280x720": (1280,720)
        },
        saved_key=save[0]
    )

    text_fullscrean = Text(
        screen,
        "Fullscrean:         ",
        text_colore,
        2,
        4,
        selects={
            "On": True,
            "Off": False
        },
        saved_key=save[1]
    )

    text_finded_ports = Text(
        screen,
        "Used port:      ",
        text_colore,
        2,
        3.19,
        selects=element,
        saved_key=save[2]
    )

    text_speed_of_reading = Text(
        screen,
        "Speed of reading:       ",
        text_colore,
        2,
        2.66,
        selects={
            "9600": 9600,
            "14400": 14400,
            "19200": 19200,
            "28800": 28800,
            "38400": 38400,
            "57600": 57600,
            "115200": 115200
        },
        saved_key=save[3]
    )
    save.clear()
    selected_option = {
        0: text_window_size,
        1: text_fullscrean,
        2: text_finded_ports,
        3: text_speed_of_reading
    }
    key_of_selected_option = 0
    while run:
        screen.blit(bg_menu_file,(0,0))
        bg_menu_file = pygame.transform.scale(bg_menu_load, (screen.get_width(), screen.get_height()))

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                quit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    save_settings(selected_option)
                    run = False
                if event.key == K_w:
                    if key_of_selected_option > 0:
                        key_of_selected_option -= 1
                elif event.key == K_s:
                    if event.key == K_s:
                        if key_of_selected_option < len(selected_option)-1:
                            key_of_selected_option += 1
                if event.key == K_a:
                    selected_option[key_of_selected_option].change_selected(1)

                elif event.key == K_d:
                    selected_option[key_of_selected_option].change_selected(-1)


        # ЛОГИКА РАБОТЫ ПЕРВОГО ПАРАМЕТРА РАЗРЕШЕНИЕ ЭКРАНА
        if selected_option[0].select_changed:
            if selected_option[1].get_selected():
                pygame.display.set_mode(selected_option[0].get_selected(), FULLSCREEN)
            else:
                pygame.display.set_mode(selected_option[0].get_selected())

        # ЛОГИКА РАБОТЫ ВТОРОГО ПАРАМЕТРА ПОЛНОЭКРАННЫЙ РЕЖИМ ДА ИЛИ НЕТ
        elif selected_option[1].select_changed:
            if selected_option[1].get_selected():
                pygame.display.set_mode(selected_option[0].get_selected(), FULLSCREEN)
            else:
                pygame.display.set_mode(selected_option[0].get_selected())
        for text in selected_option:
            if text == key_of_selected_option:
                temp = selected_option[text].get_rect()
                pygame.draw.rect(screen,(255, 215, 0), (0, temp.y, screen.get_width(), temp.height))
            selected_option[text].draw()

        pygame.display.update()
        clock.tick(60)