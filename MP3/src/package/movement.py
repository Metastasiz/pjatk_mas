from abc import ABC

class wheels(ABC):
    def __init__(self,numWheel, speed):
        self.numWheel = numWheel
        self.wheelSpd = speed

    def getLandSpeed(self):
        return self.wheelSpd

class rotor(ABC):
    def __init__(self,numRotor, speed):
        self.numRotor = numRotor
        self.rotorSpd = speed

    def getAirSpeed(self):
        return self.rotorSpd

class wheel_rotor(wheels,rotor):
    def __init__(self,numWheel, wheelSpd, numRotor, rotorSpd):
        super().__init__(numWheel,wheelSpd)
        self.numRotor = numRotor
        self.rotorSpd = rotorSpd

    def getLandSpeed(self):
        return super().getLandSpeed() + self.getAirSpeed()*0.6