import pygame

running = True
x, y = 800, 800
src = pygame.display.set_mode((x, y))

while running:
    x2, y2 = x/2, y/2
    pygame.init()
    # pygame.draw.line(src, (255,0,0), (x2,y), (x2,y2), width=2)
    # pygame.draw.line(src, (255,0,0), (x2,y2), (x2/2, y2/2), width=2)
    # pygame.draw.line(src, (255,0,0), (x2,y2), (x-(x2/2), y2-(y2/2)), width=2)

    for i in range(1,10):
        pygame.draw.circle(src, (255,255,255), (x/(2*i), y/(2*i)), 2, width=0)
        pygame.draw.circle(src, (255,255,255), (x/(x/(2*i)), y/i), 2, width=0)
        pass
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.flip()