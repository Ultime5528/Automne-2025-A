import wpilib
from ultime.subsystem import Subsystem
import ports


class Launcher(Subsystem):
    def __init__(self):
        super().__init__()
        self.piston = wpilib.DoubleSolenoid(
            wpilib.PneumaticsModuleType.CTREPCM,
            ports.launcher_piston_forward,
            ports.launcher_piston_backward,
        )
        self.motor = wpilib.PWMSparkMax(ports.launcher_motor)
        self.switch = wpilib.DigitalInput(ports.launcher_switch)
        self.addChild("piston", self.piston)

    def extend(self):
        self.piston.set(wpilib.DoubleSolenoid.Value.kForward)

    def retract(self):
        self.piston.set(wpilib.DoubleSolenoid.Value.kReverse)

    def stop(self):
        self.piston.set(wpilib.DoubleSolenoid.Value.kOff)
