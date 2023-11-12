from pathlib import Path
import pickle

main_dir = "MP1"
path_to_package = "src/package"
max_subDir = 10
import sys
import re
path_to_add = Path().resolve()
for _ in range(max_subDir):
    if re.search(main_dir+"$",str(path_to_add)):
        break
    path_to_add = path_to_add.parent
path_to_target = path_to_package.split("/")
for dir_ in path_to_target:
    path_to_add = path_to_add / dir_
sys.path.append(str(path_to_add))

from vector3 import vector3
from path import *
from utils import *

path_to_target_extent = "data/robotExtent.pickle"

class robot():
	extent_ = {}
	def __init__(self, name, vector3=vector3()):
		self.id_ = "RB-"+idGenerator(8)

		self.name_ = None
		self.setName(name)
		self.vector3_ = None
		self.setVector3(vector3)

		self.__class__.extent_[self.getID()] = self
		robotExtent.addInstance(self)

	def setName(self,name):
		self.name_ = name
	def setVector3(self, vector3):
		self.vector3_ = vector3

	def getID(self):
		return self.id_
	def getName(self):
		return self.name_
	def getVector3(self):
		return self.vector3_

	@classmethod
	def getExtent(cls):
		return cls.extent_

class robotExtent():
	extent = {}
	@classmethod
	def addInstance(cls,instance: robot):
		cls.extent[instance.getID()] = instance

	@classmethod
	def getExtent(cls):
		return cls.extent

	@classmethod
	def clearExtent(cls):
		cls.extent.clear()

	@classmethod
	def write(cls):
		path_ = getPath(main_dir,path_to_target_extent)
		with open(path_, "wb") as file:
			pickle.dump(len(cls.getExtent()), file)
			for robot in cls.getExtent().values():
				pickle.dump(robot, file)

	@classmethod
	def read(cls):
		path_ = getPath(main_dir,path_to_target_extent)
		with open(path_,"rb") as file:
			size = pickle.load(file)
			for _ in range(size):
				cls.addInstance(pickle.load(file))

#testing - not involved in MP1
class classExtent():
	extents = {}
	@classmethod
	def add(cls,instance):
		class_ = instance.__class__
		if class_ not in cls.extents.keys():
			cls.extents[class_] = []
		cls.extents[class_].append(instance)

	@classmethod
	def getExtent(cls,class_):
		return cls.extents[class_]

if __name__ == "__main__":
	robot = robot("name1")
