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
#		Disjoint
######################################################
""")
#engineer disjointly extends person

e1 = engineer("engineer1") #assign object name engineer1 to class engineer
c1 = customer("customer1")
p1 = person("person1") #assign object name person1 to class person

for instance in engineerExtent.getExtent().values():
	print(instance.getName())
print("Then")
for instance in personExtent.getExtent().values():
    print(instance.getName())
print(personExtent.getExtent())

print("""
######################################################
#		Abstract
######################################################
""")

print(robotExtent.getClassDescription()) #robotExtent is an extent of "classExtent"
print(engineerExtent.getClassDescription()) #classExtent is an abstract class for building classes in the system

t1 = robotExtent()
try: 
	t2 = classExtent()
except TypeError:
	print("Cannot assign object to abstract class")


print("""
######################################################
#		Polymorphic
######################################################
""")

try:
	loc = location(1,2)
except TypeError:
	print("Cannot assign object to abstract class")

b1 = building(1,2,10)
r1 = room(1,2)

print(b1.getVolumnStr())
print(r1.getVolumnStr())

print("""
######################################################
#		Overlaping
######################################################
""")

#module can contain multiple type of component in 1 module, each with their specifics

m1 = moduleComponent()
m1.setWheel(wheel(6))

print("wheel num", m1.getNumWheel())
print("chasis size", m1.getSize()) #raise error "No chasis and returns None, when "

m2 = moduleComponent()
m2.setWheel(wheel(4))
m2.setChasis(chasis(4,5))
m2.setPcb(pcb("A#429"))

print("wheel num", m2.getNumWheel())
print("chasis size", m2.getSize())
print("pcb model",m2.getModel())

m2.removeChasis()
print("chasis size", m2.getSize())

print("""
######################################################
#		Multi inheritance
######################################################
""")
from package.movement import wheels, rotor, wheel_rotor

w1 = wheels(1,2)
r1 = rotor(3,4)
print(w1.getLandSpeed())
print(r1.getAirSpeed())

wr1 = wheel_rotor(1,2,3,4) #extended from wheels with rotor "python interface"
print(wr1.getLandSpeed()) #wheel_rotor have different Land Speed calculation

print("""
######################################################
#		Multi aspect
######################################################
""")

c1 = customer("name1", civilianClearance("homeAddress1")) #inherits clearance on customer object that belongs to parent class "Person"
p1 = person("name2", civilianClearance("homeAddress2"))
c2 = customer("name3", militaryClearance("badgeNumber1")) 

temp = [c1,p1,c2]

for i in temp:
	print(i.getClearance().notCivilian())
	if not i.getClearance().notCivilian() == 1:
		print("badge",i.getClearance().getBadgeNumber())
		continue
	print(i.getClearance().getAddress())


print("""
######################################################
#		Dynamic 
######################################################
""")