from commands.drive.slide_left import SlideLeft
from commands.drive.slide_right import SlideRight
from commands.pivot.move_down import MoveDown
from commands.pivot.move_up import MoveUp
from commands.slingshot.charge import Charge
from commands.slingshot.unlock import Unlock
from modules.hardware import HardwareModule
from ultime.module import Module


class ControlModule(Module):
    def __init__(
        self,
        hardware: HardwareModule,
    ):
        super().__init__()

        """
        Pilot's buttons
        """
        hardware.controller.a().onTrue("SlingShot", Charge(hardware.slingshot, hardware.pivot))
        hardware.controller.y().onTrue("Slingshot", Unlock(hardware.slingshot))
        hardware.controller.x().onTrue("Pivot", MoveUp(hardware.pivot))
        hardware.controller.x().onTrue("Pivot", MoveDown(hardware.pivot))
        hardware.controller.leftBumper().onTrue("Drive", SlideLeft(hardware.drive))
        hardware.controller.rightBumper().onTrue("Drive", SlideRight(hardware.drive))

        """
        Copilot's panel
        """
