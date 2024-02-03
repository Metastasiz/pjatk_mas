from pathlib import Path
from package.utils import *

from package.engineerRobot import *

from package.person import person
class engineer(person):
    def __init__(self,name,clearance=None,recursive=False,extentClass=None):
        if extentClass == None:
            extentClass = []
            
        #recursive disjoint
        if recursive and len(extentClass) > 0:
            engineer(name,recursive=recursive)

        extentClass.append(engineerExtent)
        super().__init__(name,clearance,recursive,extentClass)

        #parameters verified
        self.addToLastExtent()

        self.scheduleIDList = []
        self.bossID = None
        self.subordinateIDList = {}
        self.licenseIDList = set()

    def addSubordinate(self,*engineers):
        for engi in engineers:
            if not isinstance(engi,engineer):
                print(engi.__class__.__name__,"is not instance of class engineer")
                continue
            sID = engi.getID()
            #checks if exist
            if sID not in engineerExtent.getExtent():
                continue
            #checks if not added
            if sID not in self.subordinateIDList:
                self.subordinateIDList[sID] = engi
                #checks if boss not self
                if engineerExtent.getInstance(sID).getBossID != self.getID():
                    engineerExtent.getInstance(sID).addBoss(self)
    def addBoss(self,engi):
        if not isinstance(engi,engineer):
            print(engi.__class__.__name__,"is not instance of class engineer")
            return
        self.bossID = engi.getID()
        if not engi.containSubordinateID(self.getID()):
            engi.addSubordinate(self)
    
    def addLicenseID(self, *licenseID):
        from package.license import license, licenseExtent
        for lID in licenseID:            
            #checks if not added
            if lID not in self.getLicenseID():
                self.licenseIDList.add(lID)

            #reverse connection, not necessary because called through constructor
            #checks if exist
            if lID not in licenseExtent.getExtent():
                continue
            l = licenseExtent.getInstance(lID)
            #checks if same
            if not self.getID() == l.getEngineerID():
                l.setEngineerID(self.getID())
    def removeLicenseID(self, licenseID):
        from package.license import license, licenseExtent
        #checks if exist
        if licenseID in self.getLicenseID():
            self.licenseIDList.remove(licenseID)
        
        #reverse connection
        #checks if exist
        if licenseID in licenseExtent.getExtent():
            #delete
            licenseExtent.getInstance(licenseID).removeLink()
    def getLicenseID(self):
        return self.licenseIDList

    def removeSubordinateID(self,subID):
        if not self.containSubordinateID(subID):
            return
        engi = engineer(self.subordinateIDList.pop(subID))
        engi.removeBoss()
    def removeBoss(self):
        self.bossID = None

    def containSubordinateID(self,subID):
        if subID in self.subordinateIDList:
            return True
        return False
    def getSubordinateByID(self,subID):
        if subID in self.subordinateIDList:
            return self.subordinateIDList.get(subID)
        if subID in engineerExtent.getExtent():
            print("ID is not subordinate of this engineer but found in the extent")
            return None
        print("ID is not found in the extent")
        return None
    def getSubordinateID(self):
        return self.subordinateIDList
    def getBossID(self):
        return self.bossID

    def addSchedule(self,robotID,schedule):
        #verifies in intermediate class
        scheduleID = engineerRobot.addLink(self.getID(),robotID,schedule)
    def addScheduleID(self, scheduleID):
        #verifies in intermediate class
        self.scheduleIDList.append(scheduleID)
    def removeScheduleID(self, scheduleID):
        #verifies in intermediate class
        self.scheduleIDList.remove(scheduleID)
    def getScheduleID(self):
        return self.scheduleIDList

    def __str__(self):
        out = f"Engineer: {self.getID()}\
        \n- name: {self.getName()}"
        return out

from package.classExtent import *
class engineerExtent(classExtent):
    extent = {}
    className = set()

    @classmethod
    def getClass(cls):
        return engineer
    
    @classmethod
    def getClassDescription(cls):
        from package.license import license
        from package.person import person
        classLink = {engineer,engineerRobot,license,person}
        for class_ in classLink:
            cls.className.add(class_.__name__)
        return cls.className