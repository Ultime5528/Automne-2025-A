from commands2 import SequentialCommandGroup
from commands2.cmd import waitSeconds

from commands.launcher.extend import Extend
from commands.launcher.retract import Retract
from subsystems.launcher import Launcher


class Launch(SequentialCommandGroup):
    def __init__(self, launcher: Launcher):
        super().__init__(
           Extend(launcher),
            waitSeconds(1.0),
            Retract(launcher)
        )

