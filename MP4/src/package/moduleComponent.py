from package.utils import *

class moduleComponent():
    def __init__(self):
        self.wheel = None
        self.chasis = None
        self.pcb = None

    def setWheel(self,wheel_):
        if not isinstance(wheel_,wheel):
            return
        self.wheel = wheel_
    def removeWheel(self):
        self.wheel = None
    def getNumWheel(self):
        if self.wheel == None:
            print("No wheel")
            return
        return self.wheel.getNumWheel()
    
    def setChasis(self,chasis_):
        if not isinstance(chasis_,chasis):
            return
        self.chasis = chasis_
    def removeChasis(self):
        self.chasis = None
    def getSize(self):
        if self.chasis == None:
            print("No chasis")
            return
        return self.chasis.getSize()
    
    def setPcb(self,pcb_):
        if not isinstance(pcb_,pcb):
            return
        self.pcb = pcb_
    def removePcb(self):
        self.pcb = None
    def getModel(self):
        if self.pcb == None:
            print("No pcb")
            return
        return self.pcb.getModelNum()


class wheel():
    def __init__(self,numWheel):
        self.numWheel = numWheel
    
    def getNumWheel(self):
        return self.numWheel

class chasis(moduleComponent):
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def getSize(self):
        return self.x * self.y

class pcb(moduleComponent):
    def __init__(self,modelNum):
        self.modelNum = modelNum
    
    def getModelNum(self):
        return self.modelNum