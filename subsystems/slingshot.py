import wpilib
import rev
from ultime.autoproperty import autoproperty
from ultime.subsystem import Subsystem
import ports


class Slingshot(Subsystem):
    speed_up = autoproperty(-0.1)
    speed_down = autoproperty(0.1)
    angle_lock = autoproperty(85)
    angle_unlock = autoproperty(47.67)

    def __init__(self):
        super().__init__()
        self.moteur = self.moteur = rev.SparkMax(ports.slingshot_motor, rev.SparkMax.MotorType.kBrushless)
        self.servo = wpilib.Servo(
            ports.slingshot_servo
        )
        self.switch = wpilib.DigitalInput(ports.slingshot_switch)
        self.addChild("servo" , self.servo)

    def push(self):
        self.moteur.set(self.speed_up)

    def pull(self):
        self.moteur.set(self.speed_down)

    def stop(self):
        self.moteur.stopMotor()

    def lock(self):
        self.servo.setAngle(self.angle_lock)

    def unlock(self):
        self.servo.setAngle(self.angle_unlock)

    def isPulled(self) -> bool:
        return self.switch.get()
