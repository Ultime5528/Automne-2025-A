import wpilib

from ultime.autoproperty import autoproperty
from ultime.subsystem import Subsystem
import ports


class Pivot(Subsystem):
    speed_right = autoproperty(0.3)
    speed_left = autoproperty(-0.3)
    speed_maintain = autoproperty(-0.1)

    def __init__(self):
        super().__init__()
        self.moteur = wpilib.VictorSP(ports.pivot_motor)
        self.addChild("motor", self.moteur)
        self.switch = wpilib.DigitalInput(ports.pivot_switch)
        self.addChild("switch", self.switch)

    def moveDown(self):
        self.moteur.set(self.speed_right)

    def moveUp(self):
        self.moteur.set(self.speed_left)

    def maintain(self):
        self.moteur.set(self.speed_maintain)

    def stop(self):
        self.moteur.stopMotor()

    def isUp(self) -> bool:
        return self.switch.get()
