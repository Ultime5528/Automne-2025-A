import wpilib
from rev import SparkMaxConfig, SparkBase

from ultime.autoproperty import autoproperty
from ultime.subsystem import Subsystem
import ports
import rev


class Drive(Subsystem):
    speed_left = autoproperty(0.1)
    speed_right = autoproperty(-0.1)

    def __init__(self):
        super().__init__()
        self.moteur = rev.SparkMax(
            ports.drive_motor, rev.SparkMax.MotorType.kBrushless
        )  # Si branché PWM : wpilib.PWMSparkMax
        config = SparkMaxConfig()
        config.setIdleMode(SparkMaxConfig.IdleMode.kBrake)
        self.moteur.configure(config, SparkBase.ResetMode.kResetSafeParameters, SparkBase.PersistMode.kPersistParameters)

    def rotateLeft(self):
        self.moteur.set(self.speed_left)

    def rotateRight(self):
        self.moteur.set(self.speed_right)

    def stop(self):
        self.moteur.stopMotor()
