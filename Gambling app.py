import pygame 
import pygame
import time
screen = pygame.display.set_mode((500,500))
screen.fill((255,255,255))#white
img = pygame.image.load('banana.png')
img = pygame.transform.scale(img,(25,25))
img2 = pygame.image.load('chili.jpg')
img2 = pygame.transform.scale(img,(25,25))
screen.blit(img,(250,250))
screen.blit(img2,(350,250))
pygame.display.update()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        screen.fill((255,255,255))
        screen.blit(img2, (350, 250))
        pygame.display.update()
        time.sleep(10)
        screen.blit(img, (255,255))
        pygame.display.update()


