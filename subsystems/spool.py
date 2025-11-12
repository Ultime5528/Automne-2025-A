import wpilib

from ultime.autoproperty import autoproperty
from ultime.subsystem import Subsystem
import ports


class Spool(Subsystem):
    speed_right = autoproperty(0.1)
    speed_left = autoproperty(-0.1)
    lockAngle = autoproperty(0)
    unLockAngle = autoproperty(90)

    def __init__(self):
        super().__init__()
        self.moteur = wpilib.VictorSP(
            ports.launcher_motor
        )
        self.addChild("moteur", self.moteur)
        self.servo = wpilib.Servo(
            ports.servo
        )
        self.addChild("servo" , self.servo)
    def rotateRight(self):
        self.moteur.set(self.speed_right)

    def rotateLeft(self):
        self.moteur.set(self.speed_left)

    def stop(self):
        self.moteur.stopMotor()

    def positionLock(self):
        self.servo.setAngle(self.lockAngle)

    def positionUnlock(self):
        self.servo.setAngle(self.unLockAngle)