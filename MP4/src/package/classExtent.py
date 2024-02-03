import pickle
from abc import ABC, abstractclassmethod, abstractmethod

import json
configPath = "conf/config.json"
config = json.load(open(configPath))
main_dir = config["mainDirectory"]
data_dir = config["dataDirectory"]

from package.path import *
from package.utils import *

class classExtent(ABC):
    @property
    @abstractmethod
    def extent(self):
        pass
    
    @property
    @abstractmethod
    def className(self):
        pass

    @classmethod
    @abstractclassmethod
    def getClassDescription(cls):
        pass

    @classmethod
    @abstractclassmethod
    def getClass(cls):
        pass

    @classmethod
    def addInstance(cls,instance):
        if not isinstance(instance,cls.getClass()):
            if cls.getClass() == None:
                print("Must assign a class first")
                return
            print("Instance is not from the same class")
        cls.extent[instance.getID()] = instance

    @classmethod
    def getInstance(cls,id: str):
        return cls.extent.get(id)

    @classmethod
    def getExtent(cls):
        return cls.extent

    @classmethod
    def removeInstance(cls,id: str):
        del cls.extent[id]

    @classmethod
    def clearExtent(cls):
        cls.extent.clear()

    @classmethod
    def write(cls):
        class_path = data_dir + "/" + cls.__name__ + ".pickle"
        path_ = getPath(main_dir,class_path)
        with open(path_, "wb") as file:
            pickle.dump(len(cls.getExtent()), file)
            for engineer in cls.getExtent().values():
                pickle.dump(engineer, file)

    @classmethod
    def read(cls):
        class_path = data_dir + "/" + cls.__name__ + ".pickle"
        path_ = getPath(main_dir,class_path)
        with open(path_,"rb") as file:
            size = pickle.load(file)
            for _ in range(size):
                cls.addInstance(pickle.load(file))