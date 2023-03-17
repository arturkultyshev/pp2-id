import pygame

pygame.init()
clock = pygame.time.Clock()

screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("My first game")


img = pygame.image.load('cosmos_1.jpg')
img_rect = img.get_rect()


x, y = 250, 250
fps = 300

running = True
while running:
    screen.fill((255, 255, 255))
    screen.blit(img, img_rect)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_w]:
        y -= 1
    if pressed[pygame.K_s]:
        y += 1
    if pressed[pygame.K_a]:
        x -= 1
    if pressed[pygame.K_d]:
        x += 1
    if pressed[pygame.K_q]:
        running = False
    pygame.draw.circle(screen, (0, 255, 0), (x, y), 30)
    pygame.display.flip()

    clock.tick(fps)