import pygame

pygame.init()

screen = pygame.display.set_mode((600, 600))

background = pygame.image.load("images/img.jpg")
background = pygame.transform.scale(background, (600, 600))

def draw_stickman():
    color = (255, 255, 255)

    pygame.draw.circle(screen, color, (300, 180), 40, 5)

    pygame.draw.line(screen, color, (300, 220), (300, 350), 5)

    pygame.draw.line(screen, color, (300, 250), (240, 300), 5)
    pygame.draw.line(screen, color, (300, 250), (360, 300), 5)

    pygame.draw.line(screen, color, (300, 350), (250, 430), 5)
    pygame.draw.line(screen, color, (300, 350), (350, 430), 5)

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(background, (0, 0))
    draw_stickman()
    pygame.display.update()

pygame.quit()