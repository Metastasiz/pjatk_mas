from pathlib import Path
import pickle

main_dir = "MP2"
from package.path import *
from package.utils import *
path_to_target_extent = "data/sensorExtent.pickle"

class sensor():
	sensor_max_ = 8
	sensor_efficiency_ = 0.73 #model_sample_1234
	model_name_ = "Sensor"
	def __init__(self,*sensor_power):
		self.id_ = None
		self.setID()
		self.sensor_num_ = 0
		self.setSensorNumber(*sensor_power)
		self.sensor_power_ = []
		self.setSensorPower(*sensor_power)

		sensorExtent.addInstance(self)

		self.robotID_ = None

	def setID(self):
		assignID = "RBS-"+idGenerator(8)
		extent = sensorExtent.getExtent()
		while assignID in extent:
			assignID = "RBS-"+idGenerator(8)
		self.id_ = assignID
	def setSensorNumber(self,*sensor_power):
		self.sensor_num_ = len(sensor_power)
		if len(sensor_power) > self.__class__.sensor_max_:
			self.sensor_num_ = self.__class__.sensor_max_
	def setSensorPower(self,*sensor_power):
		for index in range(self.getSensorNumber()):
			self.sensor_power_.append(sensor_power[index])
	def setRobotID(self,robotID):
		self.robotID_ = robotID
	
	def getID(self):
		return self.id_
	def getSensorNumber(self):
		return self.sensor_num_
	def getSensorPower(self):
		return self.sensor_power_
	def getRobotID(self):
		return self.robotID_

	def getSensorTotalEfficiency(self):
		return self.sensor_efficiency_ * sum(self.getSensorPower())
	
	@classmethod
	def getMaxSensor(cls):
		return cls.sensor_max_
	
	@classmethod
	def getSensorEfficiency(cls):
		return cls.sensor_efficiency_

	def __str__(self):
		return f"{self.__class__.model_name_}: {self.getID()} with {self.getSensorNumber()} modules, belongs to {self.getRobotID()}\
		\n- sensor total efficiency: {round(self.getSensorTotalEfficiency(),2)}"
	
class lidar(sensor):
	sensor_max_ = 4
	sensor_efficiency_ = 0.47 #model_sample_2345
	diminising_efficiency_ = 0.95
	model_name_ = "Lidar Sensor"

	def getSensorTotalEfficiency(self):
		return self.sensor_efficiency_ * sum(self.getSensorPower()) * pow(self.__class__.diminising_efficiency_,self.getSensorNumber())

class sensorExtent():
	extent = {}
	@classmethod
	def addInstance(cls,instance: sensor):
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
			for sensor in cls.getExtent().values():
				pickle.dump(sensor, file)

	@classmethod
	def read(cls):
		path_ = getPath(main_dir,path_to_target_extent)
		with open(path_,"rb") as file:
			size = pickle.load(file)
			for _ in range(size):
				cls.addInstance(pickle.load(file))

if __name__ == "__main__":
	s1 = sensor(1,2,3,4)

	s2 = lidar(1,2,3,4,5)

	print(s1.getSensorNumber())
	print(s1.getSensorPower())
	print(s1.getSensorTotalEfficiency())
	keys = sensorExtent.getExtent().keys()
	for key in keys:
		print(key)
		print(type(key))
		print(sensorExtent.getInstance(key))
	print(sensorExtent.getExtent())