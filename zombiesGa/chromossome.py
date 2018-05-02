# cost -> numero de ciclos vivo
from pygame import Rect
from random import randint,random
from math import pi,sin,cos
from zombie import Zombie
_sin = lambda n: round(100*sin(n))/100
_cos = lambda n: round(100*cos(n))/100
tan = lambda n: round(_sin(n)/_cos(n)*100)/100 if _cos(n) != 0 else False

angles = [2*pi/8*i for i in range(8)]

class Chromossome:
    def __init__(self,position,size,_range,cic=3,angl=[]):
        self.size = size
        self.initialp = position
        self.position = position
        self.xposition = (self.position[0]+self.size[0]//2),(self.position[1]+self.size[1]//2)
        self.rect = Rect(position,size)
        self.angles = [angles[randint(0,7)] for i in range(cic)] if angl == [] else angl
        self._range = _range
        self.cic = cic
        self.cicles = -1
    def crossover(self,other):
        i1 = randint(0,self.cic-1)
        newchromo1 = Chromossome(self.initialp,self.size,self._range,self.cic,self.angles[:i1]+other.angles[i1:])
        newchromo2 = Chromossome(self.initialp,self.size,self._range,self.cic,other.angles[:i1]+self.angles[i1:])
        return newchromo1,newchromo2
    def move(self,ang):
        if ang>=pi:
            if (type(tan(ang)) == float):
                self.rect.move_ip(-self._range,round(tan(ang)*(-self._range)))
                self.position = (self.position[0]-self._range,self.position[1]+round(tan(ang)*(-self._range)))
            else:
                self.rect.move_ip(0,-self._range)
                self.position = (self.position[0],self.position[1]-self._range)
        else:
            if type(tan(ang)) == float:
                self.rect.move_ip(self._range,round(tan(ang)*(self._range)))
                self.position = (self.position[0]+self._range,self.position[1]+round(tan(ang)*(self._range)))
            else:
                self.rect.move_ip(0,self._range)
                self.position = (self.position[0],self.position[1]+self._range)
        self.xposition = (self.position[0]+self.size[0]//2),(self.position[1]+self.size[1]//2)
    def mutate(self,p=0.03):
        if random()<=p:
            self.angles[randint(0,self.cic-1)] = angles[randint(0,7)]
    def getCicl(self,nzombies,zombieargs,dist):
        if self.cicles > -1: return
        initialp = self.position,self.xposition
        zs = [Zombie(zombieargs[0],[zombieargs[1][0]+i,zombieargs[1][1]+dist*i],zombieargs[2]) for i in range(nzombies)]
        k = 0
        while True:
            for z in zs: z.move(self.xposition)
            self.move(self.angles[k])
            k+=1
            if ((self.rect.collidelist([z.rect for z in zs]))>-1) or (self.xposition[0]>= 100 or self.xposition[1] >= 100) or (self.xposition[0] <= 0 or self.xposition[1] <= 0) :
                ##print(k)
                self.cicles = k
                break
        self.position,self.xposition = initialp
if __name__ == "__main__":
    chromo1 = Chromossome((90,90),(2,2),1,100)
    chromo2 = Chromossome((25,25),(2,2),1,100)
    chromo1.getCicl(10,([4,4],[24,24],1),5)
    print(chromo1.cicles)
    print(chromo1.angles)
