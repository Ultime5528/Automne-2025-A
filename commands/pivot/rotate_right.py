import wpilib
from ultime.command import Command
from subsystems.pivot import Pivot
from ultime.autoproperty import autoproperty


class RotateRight(Command):
    duration = autoproperty(0.5)


    def __init__(self, pivot: Pivot):
        super().__init__()
        self.pivot = pivot
        self.timer = wpilib.Timer()
        self.addRequirements(self.pivot)

    def initialize(self):
        self.timer.restart()

    def execute(self):
        self.pivot.rotateRight()

    def isFinished(self) -> bool:
        return self.timer.hasElapsed(self.duration)

    def end(self, interrupted: bool):
        self.pivot.stop()