from package import *
from package.moduleComponent import wheel, chasis, pcb
from package.location import building, room
from package.person import personExtent
from package.robot import robotExtent
from package.sensor import sensorExtent, lidar
from package.engineer import engineerExtent
from package.engineerRobot import engineerRobotExtent
from package.license import licenseExtent
from package.clearance import clearance, civilianClearance, militaryClearance


print("""
######################################################
#		Attribute Constraint
######################################################
""")

s1 = sensor(1,2,3,4,5,6,7) #static attribute sensor_max_ = 8
print(s1.getSensorPower())
s2 = sensor(1,2,3,4,5,6,7,8,9) #number of sensors can only be of sensor_max_, if more raises message then assign only first sensor_max_
print(s2.getSensorPower())

print("""
######################################################
#		Unique Constraint
######################################################
""")

for _ in range(7): #currently ID is auto generated for simplicity, but can also be manually put in
    stemp = sensor(1) #sensor ID must be unique, if not raises error and (with default mode) auto generation handles
    
for s in sensorExtent.getExtent():
    print("Sensor ID ",s)
    
print("""
######################################################
#		Subset Constraint
######################################################
""")
#association 1
#boss -> manages -> engineer
#boss <- managed by <- engineer

#association 2
#object -> belongs to -> engineer whole group
#object <- contains <- engineer whole group

#to have association 1, both object must have association 2
engi1 = engineer("name1")
engi2 = engineer("name2")
engi2.addBoss(s1) #object must be a subset of engineer extent to be have association "bossOf"
engi2.addBoss(engi1)

print("""
######################################################
#		Ordered Constraint
######################################################
""")

for e in engineerExtent.getExtent(): #instance of engineer is store in ordered
    print("Engineer ID ",e)
print()

engi3 = engineer("name3")

for e in engineerExtent.getExtent(): #added an instance
    print("Engineer ID ",e)
print()

engineerExtent.removeInstance(engi2.getID())

for e in engineerExtent.getExtent(): #removed an instance
    print("Engineer ID ",e)
print()

engineerExtent.write()
engineerExtent.clearExtent()

print("Removing Extent")
for e in engineerExtent.getExtent(): #removing whole extent
    print("Engineer ID ",e)
print()

engineerExtent.read()
for e in engineerExtent.getExtent(): #reading from an store ordered
    print("Engineer ID ",e)

print("""
######################################################
#		History/Bag Constraint
######################################################
""")

bot1 = robot("b1")
bot2 = robot("b2")
engi1.addSchedule(bot1.getID(),"link11-1") #link between engi1 and bot1
engi1.addSchedule(bot1.getID(),"link11-2") #Another link
bot1.addSchedule(engi3.getID(),"link21-1") #can be linked by both classes methods
engineerRobot.addLink(engi3.getID(),bot2.getID(),"link22-1") #can be linked using intermediate method

for instance in engineerRobotExtent.getExtent().values():
	print(instance)
keys = engineerRobotExtent.getExtent().keys()
for key in list(keys):
	engineerRobot.removeLink(key) #remove both ways
print("len =",len(engineerRobotExtent.getExtent()))

print("""
######################################################
#		Xor Constraint
######################################################
""")

civil1 = civilianClearance("Address1, warszawa")
military1 = militaryClearance("Badge number 123")

p1 = person("name1", civil1) #association from abstract class clearance can only be 1 or "Xor"
p2 = person("name2", military1)

print("""
######################################################
#		Custom Constraint
######################################################
""")

#Given contraints
#if a new sensor has the same ID as a sensor stored but 'better' sensor values, add a version to it

#so it's like Unique+Dynamic Attr Constraint
#maybe it's quite simple to implement but lets see

for s in sensorExtent.getExtent():
    print("Sensor ID ",s)

print("checking...")
for _ in range(10):
    stemp = sensor(10,10,10) #works as intended! 
    print()