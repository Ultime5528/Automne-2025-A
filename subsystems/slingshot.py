import wpilib

from ultime.autoproperty import autoproperty
from ultime.subsystem import Subsystem
import ports


class Slingshot(Subsystem):
    speed_up = autoproperty(0.1)
    speed_down = autoproperty(-0.1)
    angle_lock = autoproperty(0.0)
    angle_unlock = autoproperty(90.0)

    def __init__(self):
        super().__init__()
        self.moteur = wpilib.VictorSP(
            ports.slingshot_motor
        )
        self.addChild("moteur", self.moteur)
        self.servo = wpilib.Servo(
            ports.slingshot_servo
        )
        self.addChild("servo" , self.servo)

    def moveUp(self):
        self.moteur.set(self.speed_up)

    def moveDown(self):
        self.moteur.set(self.speed_down)

    def stop(self):
        self.moteur.stopMotor()

    def lock(self):
        self.servo.setAngle(self.angle_lock)

    def unlock(self):
        self.servo.setAngle(self.angle_unlock)