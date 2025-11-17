import commands2

from subsystems.drive import Drive
from subsystems.slingshot import Slingshot
from subsystems.pivot import Pivot
from ultime.module import Module
from ultime.subsystem import Subsystem


class HardwareModule(Module):
    def __init__(self):
        super().__init__()
        self.controller = commands2.button.CommandXboxController(0)
        self.slingshot = Slingshot()
        self.pivot = Pivot()
        self.drive = Drive()
        self.subsystems: list[Subsystem] = []