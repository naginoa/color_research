import pygame
#初始化引擎
pygame.init()

screen = pygame.display.set_mode((600, 500))
font = pygame.font.Font(None, 40)
life = 3
score = 0
y = 100
fps = 200
fcclock = pygame.time.Clock()
while True:
    screen.fill((255, 255, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = pygame.mouse.get_pos()
            if (mx - 100) ** 2 + (my - y) ** 2 <= 900:
                score += 1
                y = 100
            else:
                life -= 1
                y = 100

    if life == 0:
        lifeText = font.render('game over', True, (100, 200, 0))
        screen.blit(lifeText, (0, 0))

    else:
        lifeText = font.render('life: ' + str(life),True, (100, 200, 0))
        scoreText = font.render('score: ' + str(score), True, (100, 200, 0))
        screen.blit(lifeText, (0, 0))
        screen.blit(scoreText, (480, 0))

        y += 1
        pygame.draw.circle(screen, (100, 100, 30), (100, y), 30, 0)

    #渲染屏幕
    fcclock.tick(fps)
    pygame.display.update()

