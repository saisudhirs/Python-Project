import pygame 

pygame.init()

screen = pygame.display.set_mode((1000, 600))
pygame.display.set_caption('Game')


running = True
while running:
    screen.fill((0, 255, 0))
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    