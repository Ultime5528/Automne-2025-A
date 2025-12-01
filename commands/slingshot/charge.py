from commands2 import SequentialCommandGroup
from commands2.cmd import race, sequence

from commands.pivot.maintain import Maintain
from commands.pivot.move_up import MoveUp
from commands.pivot.move_down import MoveDown
from commands.slingshot.pull import Pull
from commands.slingshot.push import Push
from commands.slingshot.unlock import Unlock
from commands.slingshot.lock import Lock
from subsystems.pivot import Pivot
from subsystems.slingshot import Slingshot
from ultime.autoproperty import autoproperty
from ultime.command import WaitCommand


class Charge(SequentialCommandGroup):
    time_stretch = autoproperty(10)
    def __init__(self, slingshot: Slingshot, pivot: Pivot):
        super().__init__(
            MoveUp(pivot).until(lambda: pivot.isUp()),
            race(
                Maintain(pivot),
                sequence(
                    Unlock(slingshot),
                    Push(slingshot).until(lambda: not slingshot.isPulled()),
                    Pull(slingshot).until(lambda: slingshot.isPulled()),
                    Lock(slingshot),
                    Push(slingshot).raceWith(
                        WaitCommand(lambda: self.time_stretch)
                    )
                ),
            )

        )
