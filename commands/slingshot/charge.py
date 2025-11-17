import wpilib

from ports import slingshot_motor
from ultime.command import Command
from subsystems.slingshot import Slingshot
from ultime.autoproperty import autoproperty


class Embobiner(Command):
    duration = autoproperty(0.5)


    def __init__(self, spool: Slingshot):
        super().__init__()
        self.spool = spool
        self.timer = wpilib.Timer()
        self.addRequirements(self.spool)

    def initialize(self):
        self.timer.restart()


    def execute(self):
        self.spool.moveUp()

    def isFinished(self) -> bool:
        return self.timer.hasElapsed(self.duration)

    def end(self, interrupted: bool):
        self.spool.stop()