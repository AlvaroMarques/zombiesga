# width height
from math import pi,sin,cos
from pygame import Rect
_sin = lambda n: round(100*sin(n))/100
_cos = lambda n: round(100*cos(n))/100
tan = lambda n: round(_sin(n)/_cos(n)*100)/100 if _cos(n) != 0 else False
aprox = lambda n: round(100*n)/100
class Zombie:
    def __init__(self,size,position,_range):
        self.size = size
        self.position = position
        self.xposition = (position[0]+size[0]//2),(position[1]+size[1]//2)
        self._range = _range
        self.rect = Rect(self.position,self.size)
    def findAngle(self,oposition,_range):
        angles = [tan(2*pi/12*i) for i in range(12)]
        tangle = aprox(self.xposition[1]-oposition[1])/aprox(self.xposition[0]-oposition[0]) if self.xposition[0] != oposition[0] else False

        if tangle == False and type(tangle) == bool: return False
        return (min(angles,key=lambda i: (tangle-i)**2))
    def move(self,oposition):
        ang = self.findAngle(oposition,self._range)
        #if ang == 0: print("ta indo")
        
        if type(ang) == bool:

            if oposition[1]-self.xposition[1]>0:
                self.position[1]+=self._range
                self.rect.move_ip(0,self._range)
            elif oposition[1]-self.xposition[1]<0:
                self.position[1]-=self._range
                self.rect.move_ip(0,-self._range)
            self.xposition = (self.position[0]+self.size[0]//2),(self.position[1]+self.size[1]//2)
        else:
            #print(ang)
            if oposition[0]-self.xposition[0]>0:
                self.position = [self.position[0]+self._range,(round(ang*(self._range))+self.position[1])]
                self.rect.move_ip(self._range,round(ang*(self._range)))
            elif oposition[0]-self.xposition[0]<0:
                self.position = [self.position[0]-self._range,(round(ang*(-self._range))+self.position[1])]
                self.rect.move_ip(-self._range,round(ang*(-self._range)))
            self.xposition = (self.position[0]+self.size[0]//2),(self.position[1]+self.size[1]//2)
if __name__ == "__main__":
    zombie = Zombie((2,2),(25,25),2)
    print(zombie.findAngle((0,26),zombie._range))
