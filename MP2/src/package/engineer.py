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
        self.subordinateIDSet = set()

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

    def addSubordinateID(self,*subID):
        for sID in subID:
            #checks if exist
            if sID not in engineerExtent.getExtent():
                continue
            #checks if not added
            if sID not in self.subordinateIDSet:
                self.subordinateIDSet.add(sID)
                if engineerExtent.getInstance(sID).getBossID != self.getID():
                    engineerExtent.getInstance(sID).addBossID(self.getID())
    def addBossID(self,bossID):
        self.bossID = bossID
        boss = engineerExtent.getInstance(bossID)
        if not boss.containSubordinateID(self.getID()):
            boss.addSubordinateID(self.getID())

    def removeSubordinateID(self,subID):
        self.subordinateIDSet.discard(subID)
        engineerExtent.getInstance(sID).removeBossID(self.getID())
    def removeBossID(self):
        self.bossID = None

    def containSubordinateID(self,subID):
        if subID in self.subordinateIDSet:
            return True
        return False
    def getSubordinateByID(self,subID):
        if subID not in engineerExtent.getExtent():
            print("ID is not found in the extent")
            return None
        if subID not in self.subordinateIDSet:
            print("ID is not subordinate of this engineer")
            return None
        return engineerExtent.getInstance(subID)
    def getSubordinateID(self):
        return self.subordinateIDSet
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