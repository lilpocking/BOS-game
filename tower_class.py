import pygame as pg


class Tower:
    def __init__(self, screen, cof_x, cof_y):
        self.screen = screen
        self.cof_x = cof_x
        self.cof_y = cof_y
        self.arr_orig_image = []
        self.arr_image = []
        self.index_of_open_floor = -1
        self.check_size = [self.screen.get_width(), self.screen.get_height()]

    def add_image_off_floor(self, file_path):
        temp = pg.image.load(file_path)
        self.arr_orig_image.append(temp)
        temp_load = pg.transform.scale(temp, (int(temp.get_width() * self.screen.get_width()/1920), int(temp.get_height() * self.screen.get_height()/1080 - 100 * self.screen.get_height() / 1080)))
        self.arr_image.append(temp_load)

    def resize_image_floor(self):
        for i in range(len(self.arr_image)):
            self.arr_image[i] = pg.transform.scale(self.arr_orig_image[i], (int(self.arr_orig_image[i].get_width() * self.screen.get_width()/1920), int(self.arr_orig_image[i].get_height() * self.screen.get_height()/1080 - 100 * self.screen.get_height() / 1080)))

    def draw(self):
        if self.check_size != [self.screen.get_width(), self.screen.get_height()]:
            self.check_size = [self.screen.get_width(), self.screen.get_height()]
            self.resize_image_floor()
        height = 0
        if self.index_of_open_floor > -1:
            for i in range(self.index_of_open_floor+1):
                temp = self.arr_image[i].get_rect()
                if i == 0:
                    height = self.arr_image[i].get_height()
                    temp.center = (self.screen.get_width() // self.cof_x, self.screen.get_height() // self.cof_y)
                    self.screen.blit(self.arr_image[i], temp)
                else:
                    temp.center = (self.screen.get_width() // self.cof_x, self.screen.get_height() // self.cof_y - height)
                    self.screen.blit(self.arr_image[i], temp)
                    height += self.arr_image[i].get_height()

    def index_of_open_tower_up(self):
        self.index_of_open_floor += 1
        if self.index_of_open_floor >= len(self.arr_image) - 1:
            if self.index_of_open_floor >= len(self.arr_image):
                self.index_of_open_floor = len(self.arr_image) - 1
            return True
        else:
            print(self.index_of_open_floor)
            return False