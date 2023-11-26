import pickle

main_dir = "MP2"
from package.path import *
from package.utils import *
path_to_target_extent = "data/certificationExtent.pickle"

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

class licenseExtent():
	extent = {}
	@classmethod
	def addInstance(cls,instance: license):
		cls.extent[instance.getID()] = instance

	@classmethod
	def getInstance(cls,id: str):
		return cls.extent.get(id)
	
	@classmethod
	def removeInstance(cls,id: str):
		del cls.extent[id]

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
			for license in cls.getExtent().values():
				pickle.dump(license, file)

	@classmethod
	def read(cls):
		path_ = getPath(main_dir,path_to_target_extent)
		with open(path_,"rb") as file:
			size = pickle.load(file)
			for _ in range(size):
				cls.addInstance(pickle.load(file))
