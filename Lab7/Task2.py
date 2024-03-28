import pygame

pygame.init()

screen = pygame.display.set_mode((800,600))

flag = True

pygame.mixer.music.load('fds.mp3')

songs = []

while flag:
    pygame.time.delay(20)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            flag = False



        if event.type == pygame.KEYDOWN:
            if event.type == pygame.K_p:
                pygame.mixer.music.play(-1)
            elif event.type == pygame.K_s:
                pygame.mixer.music.stop()
            elif event.type == pygame.K_n:
                songs = songs[1:] + [songs[0]]
                pygame.mixer.music.stop()
                pygame.mixer.music.load(songs[0])
                pygam.mixer.music.play()
            elif event.type == pygame.K_p:
                songs = songs[-1:] + [songs[0]]
                pygame.mixer.music.load(songs)
                pygame.mixer.music.play()

    pygame.screen.fill((255,255,255))
    
    pygame.display.update()
