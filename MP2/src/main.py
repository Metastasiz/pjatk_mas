from package import *
from package.robot import robotExtent
from package.sensor import sensorExtent, lidar
from package.engineer import engineerExtent
from package.engineerRobot import engineerRobotExtent

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
engi2.addBossID(engi1.getID()) #recursive qualified association by uniquely generated ID
engi1.addSubordinateID(engi3.getID()) #qualifier is store in a key-value/dict like container, access time is O(1)
print(engi1.getSubordinateByID(engi2.getID())) #returns an instance that meets the criteria (e.g. engineer ID)
print(engi1.getSubordinateID()) #contains qualifier from engi2 and engi3
print(engi4.getSubordinateID()) #empty qualifier
print(engi4.getSubordinateByID(engi2.getID())) #when the criteria is not met, raises error and returns None

