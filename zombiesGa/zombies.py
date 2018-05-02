import zombie
import chromossome
import evaluation
import pygame
import sys
from math import pi
from time import sleep
gen, positionC, sizeC, rangeC, positionZ, sizeZ, distance, nzomb = int(sys.argv[1]), [int(i) for i in sys.argv[2].split(',')],\
    [int(i) for i in sys.argv[3].split(',')], int(sys.argv[4]), [int(i) for i in sys.argv[5].split(',')],\
    [int(i) for i in sys.argv[6].split(',')], int(sys.argv[7]), int(sys.argv[8])


pop = evaluation.Population(nzomb,(positionC,sizeC,rangeC,1000),(nzomb,sizeZ,positionZ,2,distance))
pop.evaluate(gen)
pygame.init()


screen = pygame.display.set_mode((100,100))

chromo = pop.population[-1]
zs = [zombie.Zombie(sizeZ,[positionZ[0],positionZ[1]+i*distance],1) for i in range(nzomb)]

done = False
count = 0
k = 0


while not done:
    #print(chromo.xposition)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    if count%10 == 0:
        if k< 100: chromo.move(chromo.angles[k])
        for z,_ in enumerate(zs): zs[z].move(chromo.xposition)

        k+=1
    screen.fill((0,0,0))
    pygame.draw.rect(screen,(255,255,255),chromo.rect)
    for z in zs: pygame.draw.rect(screen,(78,124,50),z.rect)
    pygame.display.flip()
    count +=1
    if (chromo.rect.collidelist([z.rect for z in zs]))>-1 or chromo.xposition[0]>= 100 or chromo.xposition[1] >= 100 or chromo.xposition[0] <= 0 or chromo.xposition[1] <= 0 :
        break
