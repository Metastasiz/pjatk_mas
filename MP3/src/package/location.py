from package.utils import *

from abc import ABC, abstractmethod

class location(ABC):
    def __init__(self,x,y):
        self.x = x
        self.y = y
    @abstractmethod
    def getVolumn(self) -> float:
        pass

    @abstractmethod
    def getVolumnStr(self) -> str:
        pass
    
class building(location):
    def __init__(self,x,y,z):
        super().__init__(x,y)
        self.z = z
    
    def getVolumn(self):
        return self.x*self.y*self.z
    def getVolumnStr(self):
        return str(self.getVolumn()) + " m3"
    
class room(location):
    def __init__(self,x,y):
        super().__init__(x,y)
    
    def getVolumn(self):
        return self.x*self.y*4
    def getVolumnStr(self):
        return str(self.getVolumn()) + " m3"

