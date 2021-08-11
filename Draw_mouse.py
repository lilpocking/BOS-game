import pygame
def draw_cursor(screen,the_cursor_image):
    temp = the_cursor_image.get_rect()
    temp.x, temp.y = pygame.mouse.get_pos()
    #pygame.draw.circle(screen, (0, 0, 0), pygame.mouse.get_pos(), 5)
    #pygame.draw.circle(screen,(255,255,255),pygame.mouse.get_pos(),3)

    screen.blit(the_cursor_image, temp)  # draw the cursor