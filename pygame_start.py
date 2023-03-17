import pygame

pygame.init()

screen = pygame.display.set_mode((500, 500))


pygame.display.update()
running = True
while running:
    pygame.time.delay(100)
    screen.fill((255, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()


