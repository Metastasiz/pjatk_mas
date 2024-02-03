from package.utils import *

from package.myClass import myClass
class engineerRobot(myClass):
    def __init__(self, engineerID, robotID, schedule):
        super().__init__({engineerRobotExtent})
        self.engineerID = None
        self.setEngineerID(engineerID)
        self.robotID = None
        self.setRobotID(robotID)
        self.schedule = None
        self.setSchedule(schedule)

        engineerRobotExtent.addInstance(self)

    def setID(self):
        assignID = "EGRB-"+idGenerator(8)
        extent = engineerRobotExtent.getExtent()
        while assignID in extent:
            assignID = "EGRB-"+idGenerator(8)
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

from package.classExtent import *
class engineerRobotExtent(classExtent):
    extent = {}
    className = set()

    @classmethod
    def getClass(cls):
        return engineerRobot
    
    @classmethod
    def getClassDescription(cls):
        from package.engineer import engineer
        from package.license import license
        classLink = {engineer,license}
        for class_ in classLink:
            cls.className.add(class_.__name__)
        return cls.className