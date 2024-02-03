from abc import ABC, abstractmethod

class absClass(ABC):
    @abstractmethod
    def do(self):
        print("abs")
    
    def yes(self):
        print("hi")

class anotherClass(ABC):
    @abstractmethod
    def some(self):
        print("aight")

class c1(absClass,anotherClass):
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def do(self):
        print(self.x)
    def some(self):
        print(self.y)

class something():
    def __init__(self):
        pass

    classT = None
    @classmethod
    def defineClass(cls, classT):
        cls.classT = classT

    @classmethod
    def get(cls):
        return cls.classT

    @classmethod
    def do(cls):
        print()

something.defineClass(list)
print(something.get())

x = something()

print(isinstance(x,something.get()))


c = c1(2,3)
print(c.x)
print(c.y)
c.yes()
try:
    a = absClass()
    a.do()
except TypeError:
    print("TypeError: Can't instantiate abstract class absClass with abstract method do")

print("end")

d = {1}
d.add(4)