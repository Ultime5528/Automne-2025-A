import wpilib
from ultime.subsystem import Subsystem
import ports


class Drive(Subsystem):
    def __init__(self):
        super().__init__()
        self.moteur = wpilib.VictorSP(
            ports.drive_motor
        )
        self.addChild("moteur", self.moteur)

    def rotate(self):
        self.moteur.set(0.1)

    def stop(self):
        self.moteur.stopMotor()