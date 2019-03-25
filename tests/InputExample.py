import pygame, sys, temp_text as text
from pygame.locals import *

pygame.init()
DISP = pygame.display.set_mode((400, 400))
pygame.display.set_caption('Input Example')
clock = pygame.time.Clock()
pygame.key.set_repeat(350, 45)

WHITE = (255, 255, 255)
BLUE  = (0,   0,   128)

keys   = 'Input:'

DISP.fill(WHITE)

while True:
    Objs = text.text_display(keys, 12, BLUE, WHITE, 'center', (200, 200))
    keys = text.get_typed(keys, 200,['a'])
    if keys == 1:
        pygame.quit()
        sys.exit()
    m = 0
    #print(pygame.K_a)
    #print(pygame.event.get(NewText.HOTKEYEVENT))
    for e in pygame.event.get(text.HOTKEYEVENT):
        if e.key == K_a:
            print('hi')
    DISP.fill(WHITE)
    DISP.blit(Objs[0], Objs[1])
    pygame.display.update()
    clock.tick(30)
    for i in pygame.event.get(pygame.QUIT):
        if i.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
