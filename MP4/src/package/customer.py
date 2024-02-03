from package.person import person
class customer(person):
    def __init__(self,name,clearance=None,recursive=False,extentClass=None):
        if extentClass == None:
            extentClass = []

        #recursive disjoint
        if recursive and len(extentClass) > 0:
            customer(name,recursive)

        extentClass.append(customerExtent)
        super().__init__(name,clearance,recursive,extentClass)
        
        #parameters verified
        self.addToLastExtent()


from package.classExtent import *
class customerExtent(classExtent):
    extent = {}
    className = set()

    @classmethod
    def getClass(cls):
        return customer
    
    @classmethod
    def getClassDescription(cls):
        from package.person import person
        classLink = {person}
        for class_ in classLink:
            cls.className.add(class_.__name__)
        return cls.className