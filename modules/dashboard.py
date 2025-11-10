import commands2
import wpilib
from commands2 import CommandScheduler

from commands.launcher.launch import Launch
from commands.pivot.rotate_left import RotateLeft
from commands.pivot.rotate_right import RotateRight
from commands.drive.slide_left import SlideLeft
from commands.drive.slide_right import SlideRight
from modules.hardware import HardwareModule
from subsystems.drive import Drive
from subsystems.pivot import Pivot
from ultime.module import Module, ModuleList


class DashboardModule(Module):
    def __init__(
        self,
        hardware: HardwareModule,
        module_list: ModuleList,
    ):
        super().__init__()
        self._hardware = hardware
        self._module_list = module_list
        self.setupCopilotCommands(hardware)
        self.setupCommands(hardware)

    def setupCopilotCommands(self, hardware: HardwareModule):
        pass
        # putCommandOnDashboard

    def setupCommands(self, hardware):
        putCommandOnDashboard("Launcher", Launch(hardware.launcher))
        putCommandOnDashboard("Pivot-L" , RotateLeft(hardware.pivot))
        putCommandOnDashboard("Pivot-R" , RotateRight(hardware.pivot))
        putCommandOnDashboard("Drive-R", SlideRight(hardware.drive))
        putCommandOnDashboard("Drive-L" , SlideLeft(hardware.drive))

    def robotInit(self) -> None:
        for subsystem in self._hardware.subsystems:
            wpilib.SmartDashboard.putData(subsystem.getName(), subsystem)

        wpilib.SmartDashboard.putData(
            "CommandScheduler", CommandScheduler.getInstance()
        )

        for module in self._module_list.modules:
            if module.redefines_init_sendable:
                """
                If a module keeps a reference to a subsystem or the HardwareModule,
                it should be wrapped in a weakref.proxy(). For example,
                self.hardware = proxy(hardware)
                """
                print("Putting on dashboard:", module.getName())
                wpilib.SmartDashboard.putData(module.getName(), module)


def putCommandOnDashboard(
    sub_table: str, cmd: commands2.Command, name: str = None, suffix: str = " commands"
) -> commands2.Command:
    if not isinstance(sub_table, str):
        raise ValueError(
            f"sub_table should be a str: '{sub_table}' of type '{type(sub_table)}'"
        )

    if suffix:
        sub_table += suffix

    sub_table += "/"

    if name is None:
        name = cmd.getName()
    else:
        cmd.setName(name)

    wpilib.SmartDashboard.putData(sub_table + name, cmd)

    return cmd
