from package.utils import *

from package.myClass import myClass
class person(myClass):
    from package.clearance import clearance
    def __init__(self,name,clear: clearance = None,recursive=False,extentClass=None):
        if extentClass == None:
            extentClass = []
        #recursive disjoint
        if recursive and len(extentClass) > 0:
            person(name,recursive)

        extentClass.append(personExtent)
        super().__init__(extentClass)

        self.name = None
        self.setName(name)
        print(clear)
        self.clear = clear

        #parameters verified
        self.addToLastExtent()

    def getClearance(self):
        return self.clear

    def setName(self,name):
        self.name = name
    def getName(self):
        return self.name

from package.classExtent import *
class personExtent(classExtent):
    extent = {}
    className = set()

    @classmethod
    def getClass(cls):
        return person
    
    @classmethod
    def getClassDescription(cls):
        from package.engineer import engineer
        classLink = {engineer}
        for class_ in classLink:
            cls.className.add(class_.__name__)
        return cls.className