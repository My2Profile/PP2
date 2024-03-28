import pygame
import datetime

pygame.init()


screen = pygame.display.set_mode((800,600))

x=400
y=300

pygame.draw.circle(screen, (0,255,0), (400,300), 25)

flag = True
while flag:
    pygame.time.delay(20)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            flag = False

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_UP and y<=25:
            print("Border")
        elif event.key == pygame.K_UP and y>25:
            y=y-25
        if event.key == pygame.K_DOWN and y>=575:
            print("Border")
        elif event.key == pygame.K_DOWN and y<575:
            y=y+25
        if event.key == pygame.K_LEFT and x<=25:
            print("Border")
        elif event.key == pygame.K_LEFT and x>25:
            x=x-25
        if event.key == pygame.K_RIGHT and x>=775:
            print("Border")
        elif event.key == pygame.K_RIGHT and x<775:
            x=x+25
    screen.fill((255,255,255))
    pygame.draw.circle(screen, (0,255,0), (x,y), 25)
    pygame.display.update()
