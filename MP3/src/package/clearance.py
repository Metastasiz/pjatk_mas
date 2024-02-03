from abc import ABC

class clearance(ABC):
    def __init__(self, type):
        self.type = type

    def notCivilian(self):
        return self.type

class civilianClearance(clearance):
    def __init__(self,homeAddress):
        super().__init__(1)
        self.homeAddress = homeAddress
    
    def getAddress(self):
        return self.homeAddress

class militaryClearance(clearance):
    def __init__(self,badgeNumber):
        super().__init__(2)
        self.badge = badgeNumber

    def getBadgeNumber(self):
        return self.badge