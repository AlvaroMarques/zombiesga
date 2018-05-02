import pygame
from chromossome import Chromossome
from zombie import Zombie
class Population:
    def __init__(self,size,chromoargs,zombieargs):
        self.population = [Chromossome(chromoargs[0],chromoargs[1],chromoargs[2],chromoargs[3]) for i in range(size)]
        self.zombieargs = zombieargs
        self.xs,self.ys = [],[]
    def organize(self):
        for i,_ in enumerate(self.population): self.population[i].getCicl(self.zombieargs[0],self.zombieargs[1:-1],self.zombieargs[-1])
        self.population = sorted(self.population,key=lambda chrom: chrom.cicles)
    def mutations(self):
        for i,_ in enumerate(self.population): self.population[i].mutate(0.2)
    def evaluate(self,ngens):
        for gen in range(ngens):
            self.mutations()
            c1,c2 = self.population[-1].crossover(self.population[-2])
            self.population.append(c1)
            self.population.append(c2)
            self.organize()
            self.population = self.population[2:]
            if self.ys != [] and self.population[-1].cicles != self.ys[-1]:
                self.ys.append(self.population[-1].cicles)
                self.xs.append(gen)
            elif self.ys == []:
                self.ys.append(self.population[-1].cicles)
                self.xs.append(gen)
            print(gen,self.population[-1].cicles)
if __name__ == '__main__':
    pop = Population(20,[(90,90),(4,4),3,100],[10,[4,4],[24,24],1,5])
    #for i,_ in enumerate(pop.population): pop.population[i].getCicl(pop.zombieargs[0],pop.zombieargs[1:-1],pop.zombieargs[-1])
    pop.evaluate(30000)
    zom = open('zombies.txt','w')
    zom.write(str(pop.population[-1].cicles))
    zom.write("\n")
    zom.write(str(pop.population[-1].angles))
    zom.write('\n')
    zom.write(str(pop.xs))
    zom.write('\n')
    zom.write(str(pop.ys))

    zom.close()
    del zom
