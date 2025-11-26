import wpilib

from ultime.autoproperty import autoproperty
from ultime.subsystem import Subsystem
import ports


class Pivot(Subsystem):
    speed_right = autoproperty(0.1)
    speed_left = autoproperty(-0.1)

    def __init__(self):
        super().__init__()
        self.moteur = wpilib.VictorSP(
            ports.pivot_motor
        )
        self.switch = wpilib.DigitalInput(ports.pivot_switch)
        self.addChild("moteur", self.moteur)

    def moveDown(self):
        self.moteur.set(self.speed_right)

    def moveUp(self):
        self.moteur.set(self.speed_left)

    def stop(self):
        self.moteur.stopMotor()

    def isUp(self) -> bool:
        return self.switch.get()
