import pygame
pygame.init()

width, height = 500, 400
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("grapics lab test")
screen.fill(white)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_F1:
                pygame.quit()
            run = False
        pygame.draw.line(screen, green, (50, 50), (250, 250), 3)
        pygame.draw.polygon(screen, blue, [(250, 0), (100,150), (400, 150)])
        pygame.draw.polygon(screen, blue, [(100, 150), (-50,300), (250, 300)])
        pygame.draw.polygon(screen, blue, [(400, 150), (250,300), (550, 300)])
        pygame.draw.circle(screen, red, (250, 200), 5)
    pygame.display.flip()
