import wpilib
from ultime.command import Command
from subsystems.slingshot import Slingshot
from ultime.autoproperty import autoproperty


class Lock(Command):
    duration = autoproperty(0.5)

    def __init__(self, slingshot: Slingshot):
        super().__init__()
        self.slingshot = slingshot
        self.timer = wpilib.Timer()
        self.addRequirements(self.slingshot)

    def initialize(self):
        self.timer.restart()

    def execute(self):
        self.slingshot.lock()

    def isFinished(self) -> bool:
        return self.timer.hasElapsed(self.duration)

    def end(self, interrupted: bool):
        pass

