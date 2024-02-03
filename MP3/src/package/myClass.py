from abc import ABC, abstractclassmethod, abstractmethod

from package.utils import *
class myClass(ABC):
    from package.classExtent import classExtent
    def __init__(self, extentClassList: list):
        self.extentClassList = extentClassList
        self.id = None
        self.setID()

    def setID(self):
        idPrefix = self.getLastClass().__name__+"-"
        assignID = idPrefix+idGenerator(8)
        extent = self.getLastExtent()
        while assignID in extent:
            assignID = idPrefix+idGenerator(8)
        self.id = assignID

    def getID(self):
        return self.id
    
    def getLastExtent(self):
        return next(iter(self.extentClassList)).getExtent()
    
    def getLastClass(self):
        return self.extentClassList[0]
    
    def addToLastExtent(self):
        self.getLastClass().addInstance(self)