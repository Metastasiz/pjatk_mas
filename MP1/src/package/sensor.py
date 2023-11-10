class sensor():
	_sensor_max = 8
	_sensor_efficiency = 0.73 #model_sample_1234
	def __init__(self,*sensor_power):
		self.sensor_num_ = 0
		self.setSensorNumber(*sensor_power)

		self.sensor_power_ = []
		self.setSensorPower(*sensor_power)

	def setSensorNumber(self,*sensor_power):
		self.sensor_num_ = len(sensor_power)
		if len(sensor_power) > self.__class__._sensor_max:
			self.sensor_num_ = self.__class__._sensor_max
	def getSensorNumber(self):
		return self.sensor_num_
	

	def setSensorPower(self,*sensor_power):
		for index in range(self.getSensorNumber()):
			self.sensor_power_.append(sensor_power[index])
	def getSensorPower(self):
		return self.sensor_power_

	def getSensorTotalEfficiency(self):
		return self._sensor_efficiency * sum(self.getSensorPower())
	
	@classmethod
	def getMaxSensor(cls):
		return cls._sensor_max
	
	@classmethod
	def getSensorEfficiency(cls):
		return cls._sensor_efficiency
	
class lidar(sensor):
	_sensor_max = 4
	_sensor_efficiency = 0.47 #model_sample_2345

	
if __name__ == "__main__":
	sensor1 = sensor(1,2,3,4)

	sensor = lidar(1,2,3,4,5)

	print(sensor.getSensorNumber())
	print(sensor.getSensorPower())
	print(sensor.getSensorTotalEfficiency())