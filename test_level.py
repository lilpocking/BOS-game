import pygame as pg
from port_reading import get_value
WHITE = (255,255,255)
text_colore = (245,245,245)
def test_level(screen):
    level = True
    clock = pg.time.Clock()
    text = pg.font.Font("font/font.ttf", int(36 * screen.get_width() / 1920))
    while level:
        screen.fill((124, 124, 124))
        val = get_value()
        if type(val) == str:
            text_on_screen = text.render(val, True, [245, 245, 245])
            rect_of_text = text_on_screen.get_rect()
            rect_of_text.center = (screen.get_width()//2, screen.get_height() // 2)
            screen.blit(text_on_screen, rect_of_text)
        for events in pg.event.get():
            if events.type == pg.KEYDOWN:
                if events.key == pg.K_ESCAPE:
                    level = False
            if events.type == pg.QUIT:
                pg.quit()
                quit()

        pg.display.flip()
        clock.tick(60)