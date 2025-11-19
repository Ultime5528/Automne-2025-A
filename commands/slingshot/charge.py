from commands2 import SequentialCommandGroup

from commands.slingshot.movedown import MoveDown
from commands.slingshot.moveup import MoveUp
from commands.slingshot.unlock import Unlock
from commands.slingshot.lock import Lock
from subsystems.slingshot import Slingshot


class Charge(SequentialCommandGroup):
    def __init__(self, slingshot: Slingshot):
        super().__init__(
            Unlock(slingshot),
            MoveUp(slingshot),
            MoveDown(slingshot),
            Lock(slingshot),
            MoveUp(slingshot),
            MoveUp(slingshot)
        )