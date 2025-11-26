import wpilib

from ports import slingshot_motor
from ultime.command import Command
from subsystems.slingshot import Slingshot
from ultime.autoproperty import autoproperty


class Pull(Command):

    def __init__(self, slingshot: Slingshot):
        super().__init__()
        self.slingshot = slingshot
        self.addRequirements(self.slingshot)


    def execute(self):
        self.slingshot.pull()

    def isFinished(self) -> bool:
        return False

    def end(self, interrupted: bool):
        self.slingshot.stop()


