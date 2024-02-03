from package.utils import *

from package.engineer import engineer, engineerExtent

class license():
	def __new__(cls, engineerIns: engineer, name):
		#required, composite
		if not isinstance(engineerIns, engineer):
			print(engineerIns.__class__.__name__,"is not instance of class engineer")
			return None
		if engineerIns.getID() not in engineerExtent.getExtent():
			print("Engineer ID does not exist in the extent")
			return None
		
		return super().__new__(cls)

	def __init__(self, engineerIns: engineer, name):
		self.id_ = None
		self.setID()
		self.name_ = None
		self.setName(name)

		self.engineerID = None
		self.setEngineerID(engineerIns)

		licenseExtent.addInstance(self)

	def setID(self):
		assignID = "EGL-"+idGenerator(8)
		extent = licenseExtent.getExtent()
		while assignID in extent:
			assignID = "EGL-"+idGenerator(8)
		self.id_ = assignID
	def setName(self,name):
		self.name_ = name
	def setEngineerID(self,engineerIns):
		engineerID = engineerIns.getID()
		self.engineerID = engineerID
		#reverse connection
		engi = engineerExtent.getInstance(self.getEngineerID())
		#checks if exist
		if self.getID() not in engi.getLicenseID():
			engi.addLicenseID(self.getID())
		return True

	def getID(self):
		return self.id_
	def getName(self):
		return self.name_
	def getEngineerID(self):
		return self.engineerID
	
	def removeLink(self):
		#reverse connection
		#checks if exist
		if self.getEngineerID() in engineerExtent.getExtent():
			engi = engineerExtent.getInstance(self.getEngineerID())
			#checks if exist
			if self.getID() in engi.getLicenseID():
				engi.removeLicenseID(self.getID())
		
		#checks if exist
		if self.getID() in licenseExtent.getExtent():
			#delete
			licenseExtent.removeInstance(self.getID())
			self.deleteSelf()

	def deleteSelf(self):
		self.id_ = None
		self.name_ = None
		self.engineerID = None



	def __str__(self):
		out = f"License: {self.getID()}\
		\n- name: {self.getName()}\
		\n- engineer ID: {self.getEngineerID()}"
		return out

from package.classExtent import *
class licenseExtent(classExtent):
	extent = {}
	className = set()

	@classmethod
	def getClass(cls):
		return license
	
	@classmethod
	def getClassDescription(cls):
		from package.license import license
		classLink = {engineer}
		name = {}
		for class_ in classLink:
			cls.className.add(class_.__name__)
		return cls.className