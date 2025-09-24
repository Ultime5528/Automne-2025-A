#!/usr/bin/env python3
from typing import Optional

import commands2
import wpilib
from commands2.button import CommandXboxController

from commands.drive import Drive
from subsystems.drivetrain import Drivetrain


class Robot(commands2.TimedCommandRobot):
    def __init__(self):
        super().__init__()
        wpilib.LiveWindow.enableAllTelemetry()
        wpilib.LiveWindow.setEnabled(True)
        wpilib.DriverStation.silenceJoystickConnectionWarning(True)

        self.xboxremote = CommandXboxController(0)
        self.stick = commands2.button.CommandJoystick(1)

        self.drivetrain = Drivetrain()
        self.drivetrain.setDefaultCommand(Drive(self.drivetrain, self.xboxremote))

        self.autoChooser = wpilib.SendableChooser()
        self.autoCommand: Optional[commands2.CommandBase] = None

        self.setupButtons()

    #copilote

    def setupButtons(self):
        pass
        #self.xboxremote.button(1).onTrue(BougerUrgence(self.drivetrain, 0.4, 1.2, 0.5))
        #self.stick.button(8).onTrue(ResetProtocol(self.arm))
        #self.stick.button(5).onTrue(MoveArm.toLevel1(self.arm))
        #self.stick.button(3).onTrue(MoveArm.toLevel2(self.arm))
        #self.stick.button(4).onTrue(MoveArm.toLevel3(self.arm))


    def autonomousInit(self) -> None:
        self.autoCommand: commands2.CommandBase = self.autoChooser.getSelected()
        if self.autoCommand:
            self.autoCommand.schedule()

    def teleopInit(self) -> None:
        if self.autoCommand:
            self.autoCommand.cancel()

    def setupDashboard(self):

        self.autoCommand = None


if __name__ == "__main__":
    wpilib.run(Robot)
