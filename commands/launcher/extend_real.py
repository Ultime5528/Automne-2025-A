import wpilib
from ultime.command import Command
from subsystems.launcher import Laucher
from ultime.autoproperty import autoproperty


class RotateLeft(Command):
    duration = autoproperty(0.5)

    def __init__(self, laucher: Laucher):
        super().__init__()
        self.laucher = laucher
        self.timer = wpilib.Timer()
        self.addRequirements(self.laucher)

    def initialize(self):
        self.timer.restart()

    def execute(self):
        self.laucher.rotateLeft()

    def isFinished(self) -> bool:
        return self.timer.hasElapsed(self.duration)

    def end(self, interrupted: bool):
        self.laucher.stop()


