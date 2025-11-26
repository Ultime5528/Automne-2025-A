from typing import Final

"""
Respect the naming convention : "subsystem" _ "component type" _ "precision"

Put port variables into the right category: CAN - PWM - DIO

Order port numbers, ex:
    drivetrain_motor_fl: Final = 0
    drivetrain_motor_fr: Final = 1
    drivetrain_motor_rr: Final = 2
"""

# CAN
drive_motor: Final = 1
slingshot_motor: Final = 2

# PWM
pivot_motor: Final = 0
slingshot_servo : Final = 1

# DIO
pivot_switch: Final = 0
slingshot_switch: Final = 1

# PCM

