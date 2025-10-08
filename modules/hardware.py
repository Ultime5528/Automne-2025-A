import commands2

from subsystems.launcher import Launcher
from ultime.module import Module
from ultime.subsystem import Subsystem


class HardwareModule(Module):
    def __init__(self):
        super().__init__()
        self.controller = commands2.button.CommandXboxController(0)
        self.launcher = Launcher()
        self.subsystems: list[Subsystem] = []
