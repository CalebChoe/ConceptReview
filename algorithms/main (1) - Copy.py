import pygame

pygame.init()

surface = pygame.display.set_mode((400, 300))
color = (255, 0, 0)
surface.fill(color)
pygame.display.flip()

run = True

while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
