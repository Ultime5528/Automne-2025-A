from commands2 import SequentialCommandGroup

from commands.pivot.move_up import MoveUp
from commands.pivot.move_down import MoveDown
from commands.slingshot.pull import Pull
from commands.slingshot.push import Push
from commands.slingshot.unlock import Unlock
from commands.slingshot.lock import Lock
from subsystems.pivot import Pivot
from subsystems.slingshot import Slingshot


class Charge(SequentialCommandGroup):
    def __init__(self, slingshot: Slingshot, pivot: Pivot):
        super().__init__(
            Unlock(slingshot),
            MoveUp(pivot).until(lambda: not pivot.isUp()),
            Pull(slingshot),
            Lock(slingshot),
            Push(slingshot),
            Push(slingshot),
        )
