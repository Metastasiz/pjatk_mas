from package import *
from package.robot import robotExtent
from package.sensor import sensorExtent, lidar
from package.engineer import engineerExtent
from package.engineerRobot import engineerRobotExtent
from package.license import licenseExtent

print("""
######################################################
#		Binary Association
######################################################
""")

bot1 = robot("b1")
sen1 = sensor(1,2,3) 
sen2 = lidar(1,2,3)
bot1.addSensorID(sen1.getID(),sen2.getID()) #1-to-many binary relationship
print(bot1.getSensorID())
print(sen1.getRobotID()) #reverse connection
bot1.removeSensorID(sen1.getID())
print("Removing this link",sen1.getID()) #removing this link
print(bot1.getSensorID())
print(sen1.getRobotID()) #reverse connection

print("""
######################################################
#		Association with Attribute
######################################################
""")

bot2 = robot("b2")
engi1 = engineer("e1")
engi2 = engineer("e2")
engi1.addSchedule(bot1.getID(),"link11-1") 
engi1.addSchedule(bot1.getID(),"link11-2") #with attribute
bot1.addSchedule(engi2.getID(),"link21-1") #can be linked by both classes methods
engineerRobot.addLink(engi2.getID(),bot2.getID(),"link22-1") #can be linked using intermediate method

for instance in engineerRobotExtent.getExtent().values():
	print(instance)
keys = engineerRobotExtent.getExtent().keys()
for key in list(keys):
	engineerRobot.removeLink(key) #remove both ways
print("len =",len(engineerRobotExtent.getExtent()))

print("""
######################################################
#		Qualified Association
######################################################
""")

engi3 = engineer("e3")
engi4 = engineer("e4")
engi5 = engineer("e5")
engi2.addBoss(engi1) #recursive qualified association by uniquely generated ID by instance
engi1.addSubordinate(engi3) #reverse connection
print(engi1.getSubordinateByID(engi2.getID())) #returns an instance that meets the criteria (e.g. engineer ID)
print(engi1.getSubordinateID()) #contains qualifier from engi2 and engi3
print(engi4.getSubordinateID()) #empty qualifier
print(engi4.getSubordinateByID(engi2.getID())) #when the criteria is not met, raises error and returns None
engineerExtent.removeInstance(engi5.getID())
print(engi4.getSubordinateByID(engi5.getID())) #also handles when not found in extent

print("""
######################################################
#		Composite Association
######################################################
""")

license1 = license(engi1,"lc1")
print(license1)

license2 = license(bot1,"lc2") #handles wrong class instance
print(license2)

engineerExtent.removeInstance(engi1.getID())
license3 = license(engi1,"lc3") #instance that's not in the extent
print(license3)

license4 = license(engi2,"lc4")
print(license4)
print(engi2.getLicenseID())
license4.removeLink() #reverse connection
print(license4)
print("Empty",engi2.getLicenseID())

license5 = license(engi2,"lc5")
print(license5)
print(engi2.getLicenseID())
engi2.removeLicenseID(license5.getID()) #reverse connection
print(license5)
print("Empty",engi2.getLicenseID())
