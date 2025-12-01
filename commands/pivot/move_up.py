import wpilib
from ultime.command import Command
from subsystems.pivot import Pivot
from ultime.autoproperty import autoproperty


class MoveUp(Command):
    duration = autoproperty(0.5)

    def __init__(self, pivot: Pivot):
        super().__init__()
        self.pivot = pivot
        self.addRequirements(self.pivot)

    def execute(self):
        self.pivot.moveUp()

    def isFinished(self) -> bool:
        return False

    def end(self, interrupted: bool):
        self.pivot.stop()
