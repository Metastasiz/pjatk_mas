import pickle

main_dir = "MP2"
from package.path import *
from package.utils import *
path_to_target_extent = "data/robotExtent.pickle"

from package.vector3 import vector3
from package.sensor import *
from package.engineerRobot import *

class robot():
	def __init__(self, name, vector3=vector3()):
		self.id_ = None
		self.setID()
		self.name_ = None
		self.setName(name)
		self.vector3_ = None
		self.setVector3(vector3)
		
		self.sensorIDList = []
		self.scheduleIDList = []

		robotExtent.addInstance(self)

	def setID(self):
		assignID = "RB-"+idGenerator(8)
		extent = robotExtent.getExtent()
		while assignID in extent:
			assignID = "RB-"+idGenerator(8)
		self.id_ = assignID
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

	def addSensorID(self, *sensorID):
		for s in sensorID:
			#checks if exist
			if s not in sensorExtent.getExtent():
				continue
			self.sensorIDList.append(s)
			#reverse connection
			sensorExtent.getInstance(s).setRobotID(self.getID())
	def removeSensorID(self, *sensorID):
		for s in sensorID:
			#checks if exist
			if s not in self.sensorIDList:
				continue
			self.sensorIDList.remove(s)
			#reverse connection
			sensorExtent.getInstance(s).setRobotID(None)
	def getSensorID(self):
		return self.sensorIDList

	def addSchedule(self,engineerID,schedule):
		#verifies in intermediate class
		scheduleID = engineerRobot.addLink(engineerID,self.getID(),schedule)
	def addScheduleID(self, scheduleID):
		#verifies in intermediate class
		self.scheduleIDList.append(scheduleID)
	def removeScheduleID(self, scheduleID):
		#verifies in intermediate class
		self.scheduleIDList.remove(scheduleID)
	def getScheduleID(self):
		return self.scheduleIDList

	def __str__(self):
		out = f"Robot: {self.getID()}\
		\n- name: {self.getName()}\
		\n- position: {self.getVector3()}"
		if bool(len(self.sensorIDList)):
			out = out + "\nWith following Sensor(s):"
		for s in self.sensorIDList:
			out = out + f"\n{sensorExtent.getInstance(s)}"
		return out

class robotExtent():
	extent = {}
	@classmethod
	def addInstance(cls,instance: robot):
		cls.extent[instance.getID()] = instance

	@classmethod
	def getInstance(cls,id: str):
		return cls.extent.get(id)

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

#testing - not involved
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