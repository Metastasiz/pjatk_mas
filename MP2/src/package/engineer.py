from pathlib import Path
import pickle

main_dir = "MP2"
from package.path import *
from package.utils import *
path_to_target_extent = "data/engineerExtent.pickle"

from package.engineerRobot import *

class engineer():
    def __init__(self, name):
        self.id_ = None
        self.setID()
        self.name_ = None
        self.setName(name)

        engineerExtent.addInstance(self)

        self.scheduleIDList = []
        self.bossID = None
        self.subordinateIDList = {}
        self.licenseIDList = set()

    def setID(self):
        assignID = "EG-"+idGenerator(8)
        extent = engineerExtent.getExtent()
        while assignID in extent:
            assignID = "EG-"+idGenerator(8)
        self.id_ = assignID
    def setName(self,name):
        self.name_ = name

    def getID(self):
        return self.id_
    def getName(self):
        return self.name_

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

class engineerExtent():
    extent = {}
    @classmethod
    def addInstance(cls,instance: engineer):
        cls.extent[instance.getID()] = instance

    @classmethod
    def getInstance(cls,id: str):
        return cls.extent.get(id)

    @classmethod
    def getExtent(cls):
        return cls.extent

    @classmethod
    def removeInstance(cls,id: str):
        del cls.extent[id]

    @classmethod
    def clearExtent(cls):
        cls.extent.clear()

    @classmethod
    def write(cls):
        path_ = getPath(main_dir,path_to_target_extent)
        with open(path_, "wb") as file:
            pickle.dump(len(cls.getExtent()), file)
            for engineer in cls.getExtent().values():
                pickle.dump(engineer, file)

    @classmethod
    def read(cls):
        path_ = getPath(main_dir,path_to_target_extent)
        with open(path_,"rb") as file:
            size = pickle.load(file)
            for _ in range(size):
                cls.addInstance(pickle.load(file))