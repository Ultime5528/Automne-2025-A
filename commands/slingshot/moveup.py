from ports import slingshot_motor
import wpilib
from ultime.command import Command
from subsystems.slingshot import Slingshot
from ultime.autoproperty import autoproperty


class MoveUp(Command):
    def __init__(self, slingshot: Slingshot):
        super().__init__()
        self.slingshot = slingshot_motor
        self.addRequirements(self.slingshot)

    def execute(self):
        self.slingshot.moveUp()

    def isFinished(self) -> bool:
        return False

    def end(self, interrupted: bool):
        self.slingshot.stop()

