import commands2

from commands.drive.slide_left import SlideLeft
from commands.drive.slide_right import SlideRight
from subsystems.drive import Drive
from subsystems.spool import Spool
from subsystems.pivot import Pivot
from ultime.module import Module
from ultime.subsystem import Subsystem


class HardwareModule(Module):
    def __init__(self):
        super().__init__()
        self.controller = commands2.button.CommandXboxController(0)
        self.spool = Spool()
        self.pivot = Pivot()
        self.drive = Drive()
        self.subsystems: list[Subsystem] = []