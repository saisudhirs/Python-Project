import pygame 

pygame.init()

screen = pygame.display.set_mode((1000, 600))
pygame.display.set_caption('Game')

#loopimport pygame 

pygame.init()

#screen
screen = pygame.display.set_mode((1000, 600))
pygame.display.set_caption('Game')

#Car
xpos = 500-32
ypos = 300-32
carImage = pygame.image.load('racing-car3.png')

def car():
    screen.blit(carImage, (xpos, ypos))

#loop
running = True
while running:
    screen.fill((255, 255, 0))
    car()
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                pygame.transform.rotate(carImage, -10)
                pygame.display.update()
            elif event.key == pygame.K_RIGHT:
                pygame.transform.rotate(carImage, 10)        


running = True
while running:
    screen.fill((0, 255, 255))
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
