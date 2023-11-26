from pathlib import Path
import pickle

main_dir = "MP2"
from package.path import *
from package.utils import *
path_to_target_extent = "data/robotEngineerExtent.pickle"

class engineerRobot():
    def __init__(self, engineerID, robotID, schedule):
        self.id_ = None
        self.setID()
        self.engineerID = None
        self.setEngineerID(engineerID)
        self.robotID = None
        self.setRobotID(robotID)
        self.schedule = None
        self.setSchedule(schedule)

        engineerRobotExtent.addInstance(self)

    def setID(self):
        assignID = idGenerator(8)
        extent = engineerRobotExtent.getExtent()
        while assignID in extent:
            assignID = idGenerator(8)
        self.id_ = assignID
    def setEngineerID(self,engineerID):
        self.engineerID = engineerID
    def setRobotID(self,robotID):
        self.robotID = robotID
    def setSchedule(self,schedule):
        self.schedule = schedule

    def getID(self):
        return self.id_
    def getEngineerID(self):
        return self.engineerID
    def getRobotID(self):
        return self.robotID
    def getSchedule(self):
        return self.schedule

    def __str__(self):
        out = f"Link: {self.getID()} - {self.getSchedule()}\
        \n- Engineer ID: {self.getEngineerID()}\
        \n- Robot ID: {self.getRobotID()}"
        return out

    @classmethod
    def addLink(cls,engineerID, robotID, schedule):
        from package.robot import robot, robotExtent
        from package.engineer import engineer, engineerExtent
        #checks if exist
        if engineerID not in engineerExtent.getExtent():
            print("engineer ID not found")
            return
        if robotID not in robotExtent.getExtent():
            print("robot ID not found")
            return

        #adding link
        link = engineerRobot(engineerID,robotID,schedule)

        #reverse link
        engineer = engineerExtent.getInstance(engineerID)
        engineer.addScheduleID(link.getID())
        robot = robotExtent.getInstance(robotID)
        robot.addScheduleID(link.getID())
        return link.getID()

    @classmethod
    def removeLink(cls,linkID):
        from package.robot import robot, robotExtent
        from package.engineer import engineer, engineerExtent
        #check if exist
        if linkID not in engineerRobotExtent.getExtent():
            return

        #get ref
        link = engineerRobotExtent.getInstance(linkID)
        engineerID = link.getEngineerID()
        robotID = link.getRobotID()

        #reverse first
        engineerExtent.getInstance(engineerID).removeScheduleID(linkID)
        robotExtent.getInstance(robotID).removeScheduleID(linkID)

        #removing link
        engineerRobotExtent.removeInstance(linkID)

class engineerRobotExtent():
    extent = {}
    @classmethod
    def addInstance(cls,instance: engineerRobot):
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
            for engineerRobot in cls.getExtent().values():
                pickle.dump(engineerRobot, file)

    @classmethod
    def read(cls):
        path_ = getPath(main_dir,path_to_target_extent)
        with open(path_,"rb") as file:
            size = pickle.load(file)
            for _ in range(size):
                cls.addInstance(pickle.load(file))

