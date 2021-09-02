import pygame as pg
import pygame.image
from tower_class import Tower
from escape_menu import escape_menu
from port_reading import serclose
from port_reading import open_port
from port_reading import get_value
WHITE = (255, 255, 255)
text_colore = (245, 245, 245)


def test_level(screen):
    open_port()
    sound_of_rythm = pg.mixer.Sound("towers/appear.mp3")
    
    size = [screen.get_width(), screen.get_height()]
    level = True
    clock = pg.time.Clock()
    text = pg.font.Font("font/font.ttf", int(36 * screen.get_width() / 1920))
    image_ground = pygame.image.load("towers/Ground.png")
    ground_on_screen = pygame.transform.scale(image_ground, (int(image_ground.get_width() * screen.get_width()/1920), int(image_ground.get_height() * screen.get_height()/1080)))

    text_of_wining = text.render("You win", False, text_colore)

    win = False

    alpha_rythm = False

    need_alpha = True

    find_of_lower = [0, 0, 0]
    lower_finded = False
    low = 0

    find_of_max = [0, 0, 0]
    max_finded = False
    max = 0

    text_of_rythm = text.render("Finding....", False, (255, 255, 255))

    number_in_port = 0

    tower = Tower(screen, 2, 1.2)
    for i in range(0, 5):
        tower.add_image_off_floor("towers/tower_test/Test_tower_" + str(i) + ".png")

    while level:
        screen.fill((124, 124, 124))
        screen.blit(ground_on_screen, (0, screen.get_height() - ground_on_screen.get_height()))
        val = get_value()
        if size != [screen.get_width(), screen.get_height()]:
            size = [screen.get_width(), screen.get_height()]
            ground_on_screen = pygame.transform.scale(image_ground, (int(image_ground.get_width() * screen.get_width() / 1920), int(image_ground.get_height() * screen.get_height() / 1080)))
        if type(val) == str:
            text_on_screen = text.render(val, True, [245, 245, 245])
            rect_of_text = text_on_screen.get_rect()
            rect_of_text.center = (rect_of_text.width//2, screen.get_height() - rect_of_text.height//2)
            screen.blit(text_on_screen, rect_of_text)
            if val != "Nothing" and val != '':
                number_in_port = float(val)
                if not max_finded:
                    find_of_max[2] = find_of_max[1]
                    find_of_max[1] = find_of_max[0]
                    find_of_max[0] = number_in_port
                elif not lower_finded:
                    find_of_lower[2] = find_of_lower[1]
                    find_of_lower[1] = find_of_lower[0]
                    find_of_lower[0] = number_in_port
                    #print(find_of_lower[0], find_of_lower[1], find_of_lower[2])


        for events in pg.event.get():
            if events.type == pg.KEYDOWN:
                if events.key == pg.K_ESCAPE:
                    #level = False
                    serclose()
                    s = escape_menu(screen)
                    if s == "1":
                        level = False
                if events.key == pg.K_o:
                    if tower.index_of_open_tower_up():
                        win = True
                if events.type == pygame.KEYDOWN:
                    if events.key == pygame.K_f:
                        tower.index_of_open_tower_up()
            if events.type == pg.QUIT:
                serclose()
                pg.quit()
                quit()

        if number_in_port != 0:
                if not max_finded and find_of_max[0] < find_of_max[1] and find_of_max[1] > find_of_max[2]:
                    max_finded = True
                    max = find_of_max[1]
                    find_of_lower[2] = find_of_max[1]
                    find_of_lower[1] = find_of_max[0]
                    val = get_value()
                    find_of_lower[0] = float(val)
                if max_finded and find_of_lower[0] > find_of_lower[1] and find_of_lower[1] < find_of_lower[2] and find_of_lower[1] != 0 and find_of_lower[0] !=0:
                    lower_finded = True
                    low = find_of_lower[1]

                if max_finded and lower_finded:
                    print(max, " - ",low, " = ", abs(max - low))
                    if abs(max - low) > 15:
                        text_of_rythm = text.render("Beta-rythm", False, (255, 255, 255))
                        alpha_rythm = False
                    else:
                        text_of_rythm = text.render("Alpha-rythm", False, (255, 255, 255))
                        alpha_rythm = True
                    max_finded = False
                    lower_finded = False
                    find_of_max[2] = find_of_lower[1]
                    find_of_max[1] = find_of_lower[0]
                    find_of_max[0] = float(get_value())
                    
                rect_of_rythm = text_of_rythm.get_rect()
                rect_of_rythm.bottomleft = rect_of_text.topleft
                screen.blit(text_of_rythm, rect_of_rythm)


        if need_alpha:
            if alpha_rythm:
                if tower.index_of_open_tower_up():
                    win = True
                need_alpha = False
                if not win:
                    sound_of_rythm.play()
        else:
            if not alpha_rythm:
                if tower.index_of_open_tower_up():
                    win = True
                need_alpha = True
                if not win:
                    sound_of_rythm.play()

        tower.draw()

        if win:
            rect = text_of_wining.get_rect()
            rect.center = (screen.get_width() // 2, screen.get_height() // 2)
            screen.blit(text_of_wining, rect)


        pg.display.flip()
        clock.tick(60)
