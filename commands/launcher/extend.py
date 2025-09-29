import wpilib
from ultime.command import Command
from subsystems.launcher import Launcher
from ultime.autoproperty import autoproperty


class Extend(Command):
    duration = autoproperty(0.5)

    def __init__(self, launcher: Launcher):
        super().__init__()
        self.launcher = launcher
        self.timer = wpilib.Timer()
        self.addRequirements(self.launcher)

    def initialize(self):
        self.timer.reset()
        self.timer.start()

    def execute(self):
        self.launcher.extend()

    def isFinished(self) -> bool:
        return self.timer.get() >= self.duration

    def end(self, interrupted: bool):
        self.launcher.stop()
