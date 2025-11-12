import wpilib

from ultime.autoproperty import autoproperty
from ultime.subsystem import Subsystem
import ports


class Spool(Subsystem):
    speed_right = autoproperty(0.1)
    speed_left = autoproperty(-0.1)

    def __init__(self):
        super().__init__()
        self.moteur = wpilib.VictorSP(
            ports.launcher_motor
        )
        self.addChild("moteur", self.moteur)

    def rotateRight(self):
        self.moteur.set(self.speed_right)

    def rotateLeft(self):
        self.moteur.set(self.speed_left)

    def stop(self):
        self.moteur.stopMotor()