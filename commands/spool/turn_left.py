import wpilib

from ports import launcher_motor
from ultime.command import Command
from subsystems.spool import Spool
from ultime.autoproperty import autoproperty


class RollLeft(Command):
    duration = autoproperty(0.5)

    def __init__(self, spool: Spool):
        super().__init__()
        self.spool = launcher_motor
        self.timer = wpilib.Timer()
        self.addRequirements(self.spool)

    def initialize(self):
        self.timer.restart()

    def execute(self):
        self.spool.rotateLeft()

    def isFinished(self) -> bool:
        return self.timer.hasElapsed(self.duration)

    def end(self, interrupted: bool):
        self.spool.stop()


