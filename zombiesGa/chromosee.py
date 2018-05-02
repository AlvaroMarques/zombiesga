import pygame
import chromossome

chromo = chromossome.Chromossome((25,25),(2,2),3)

pygame.init()

screen = pygame.display.set_mode((100,100))

done = False

frame = 0

n = 0

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    if frame % 50 == 0:
        for i in [0.0, 0.7853981633974483, 1.5707963267948966, 2.356194490192345, 3.141592653589793, 3.9269908169872414, 4.71238898038469, 5.497787143782138]:
            chromo.move(chromo.angles[n])
        n+=1
        if n == len(chromo.angles): n = 0
    screen.fill((0,0,0))
    pygame.draw.rect(screen,(255,255,255),chromo.rect)
    pygame.display.flip()
    frame+=1
