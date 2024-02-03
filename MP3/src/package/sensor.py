from package.utils import *

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

from package.classExtent import *
class sensorExtent(classExtent):
	extent = {}
	className = set()

	@classmethod
	def getClass(cls):
		return sensor
	
	@classmethod
	def getClassDescription(cls):
		from package.robot import robot
		classLink = {robot}
		for class_ in classLink:
			cls.className.add(class_.__name__)
		return cls.className