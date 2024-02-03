class vector3():
	def __init__(self, x=0,y=0,z=0):
		self._x = None
		self._y = None
		self._z = None
		self.setX(x)
		self.setY(y)
		self.setZ(z)		

	def setX(self, x):
		self._x = x
	def setY(self, y):
		self._y = y
	def setZ(self, z):
		self._z = z

	def getX(self):
		return self._x
	def getY(self):
		return self._y
	def getZ(self):
		return self._z
	
	def printDescription(self):
		print("Coordinate: ",end="")
		print(self.getX(),self.getY(),self.getZ(),sep=",")
