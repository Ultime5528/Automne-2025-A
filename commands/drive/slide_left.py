import wpilib
from ultime.command import Command
from subsystems.drive import Drive
from ultime.autoproperty import autoproperty


class SlideLeft(Command):
    duration = autoproperty(0.5)

    def __init__(self, drive: Drive):
        super().__init__()
        self.drive = drive
        self.timer = wpilib.Timer()
        self.addRequirements(self.drive)

    def initialize(self):
        self.timer.restart()

    def execute(self):
        self.drive.rotateLeft()

    def isFinished(self) -> bool:
        return self.timer.hasElapsed(self.duration)

    def end(self, interrupted: bool):
        self.drive.stop()



