from package.utils import *

class sensor():
	sensor_max_ = 8
	sensor_efficiency_ = 0.73 #model_sample_1234
	model_name_ = "Sensor"
	def __init__(self,*sensor_power):
		self.sensor_num_ = 0
		self.setSensorNumber(*sensor_power)
		self.sensor_power_ = []
		self.setSensorPower(*sensor_power)

		self.id_ = None
		self.setID()

		sensorExtent.addInstance(self)

		self.robotID_ = None

	def setID(self):
		__gen_id_length = 1
		assignID = "RBS-"+idNumGenerator(__gen_id_length)
		extent = sensorExtent.getExtent()
		while assignID in extent:
			print(f"ID {assignID} assigned is already in the extent")
			if self.getSensorPower() > sensorExtent.getInstance(assignID).getSensorPower():
				print("This is a new version of the sensor")
				__version = 1
				while str(assignID)+"."+str(__version) in extent:
					__version += 1
				print(f"Current version can be assigned to {assignID}.{__version}")
				assignID = str(assignID)+"."+str(__version)
			else:
				assignID = "RBS-"+idNumGenerator(__gen_id_length)
		self.id_ = assignID
	def setSensorNumber(self,*sensor_power):
		self.sensor_num_ = len(sensor_power)
		if len(sensor_power) > self.__class__.sensor_max_:
			print(f'Number of Sensors is more than {self.__class__.sensor_max_}, assigning only first {self.__class__.sensor_max_} ones.')
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