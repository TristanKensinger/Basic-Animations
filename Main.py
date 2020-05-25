import pygame
from Player import Player

#pygame setup
pygame.init()
win = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Pumpkin Man")

#variables
run = True
player = Player(0, win.get_height() - 125, 100, 125)
font = pygame.font.Font("PixelGameFont.ttf",20)
text1 = font.render("Use Arrow Keys to Move Left and Right", True, (255,0,0), (0))
text2 = font.render("Press Space to Jump", True, (255,0,0), (0))
text3 = font.render("Press D to Die", True, (255,0,0), (0))
text4 = font.render("Press R to Resurect", True, (255,0,0), (0))

#paints surfaces to screen
def paint():
    win.fill((0))
    win.blit(text1, (25, 25))
    win.blit(text2, (25, 50))
    win.blit(text3, (25, 75))
    win.blit(text4, (25, 100))
    player.draw(win)
    pygame.display.update()

#main loop of program
while run:
    pygame.time.delay(1000//60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    player.update(win, keys)

    paint()

pygame.quit()
