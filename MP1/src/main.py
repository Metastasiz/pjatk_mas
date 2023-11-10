import pickle
import sys

from package import *
from package.robot import robotExtent
from package.sensor import lidar

##################################################################################
#		This MP1 uses my package that is located on PYPI named metastasiz
#		The package fixes some issue when importing and has no other impact
#		The package is required in the module robot.py
#		The source code is here https://github.com/Metastasiz/metastasiz_package
#		Must do: pip install metastasiz==0.1.1
##################################################################################

######################################
#		The Extent
######################################
a = robot("name1") 
b = robot("name2") 

for ins in robot.getExtent().values(): #internal Extent
	print("Robot ID:",ins.getID())

for ins in robotExtent.getExtent().values(): #external Extent
	print("Robot ID:",ins.getID())

######################################
#		Extent Persistency
######################################

robotExtent.write()
print("Saving the extent")

robotExtent.clearExtent()
for ins in robotExtent.getExtent().values(): #external Extent
	print("Robot ID:",ins.getID())
print("The extent is empty")

robotExtent.read()
print("Loading the extent")
for ins in robotExtent.getExtent().values(): #external Extent
	print("Robot ID:",ins.getID())

######################################
#		Complex Attribute
######################################

c = robot("name3", vector3(10,-5,3)) #vector3 is an attribute showing the robot location in x,y,z
c.getVector3().printDescription()

######################################
#		Optional Attribute
######################################

vector = vector3(5,z=10) #y = optional, which is default to 0 in this case
vector.printDescription()

######################################
#		Multivalued Attribute
######################################

sensor1 = sensor(1,2,3)
sensor2 = sensor(1,2,3,4,5) #instance can have multiple sensors at the same time with different power values
print(sensor1.getSensorPower())
print(sensor2.getSensorPower())

######################################
#		Class Attribute
######################################

sensor3 = sensor(1,2,3,4,5,6,7,8,9,10,11,12,1,2,3,4)
print(sensor3.getSensorPower()) #limited number of sensors even if input more than max
print(sensor.getMaxSensor())

######################################
#		Derived Attribute
######################################

print(sensor1.getSensorTotalEfficiency()) #calculate the total sensor cluster efficiency 
print(sensor2.getSensorTotalEfficiency())
print(sensor3.getSensorTotalEfficiency())

######################################
#		Class Method
######################################

print(sensor.getSensorEfficiency()) #get the standard sensor effciency of the stadard model

######################################
#		Override
######################################

sensor4 = lidar(2,3,4,5,6) #another type of sensor
print(sensor4.getSensorPower())
print(sensor4.getMaxSensor()) #different max
print(sensor4.getSensorEfficiency()) #different efficiency
print(sensor4.getSensorTotalEfficiency()) #with different way of calculating total efficiency

######################################
#		Override
######################################

vector1 = vector3(5,y=10) #no Z input, Z default is set to 0
vector1.printDescription()

vector2 = vector3(5,z=10) #no Y input, Y default is set to 0
vector2.printDescription()