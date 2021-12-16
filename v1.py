import pygame 
import time
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
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT]:
        carImage=pygame.transform.rotate(carImage, -22.5)
        time.sleep(0.15)
        
    elif keys[pygame.K_RIGHT]:
        carImage=pygame.transform.rotate(carImage, 22.5)
        time.sleep(0.15)

    elif keys[pygame.K_w]:
        ypos-=1
        
    elif keys[pygame.K_s]:
        ypos+=1
        
    elif keys[pygame.K_a]:
        xpos-=1
        
    elif keys[pygame.K_d]:
        xpos+=1    
    else:
        pass
