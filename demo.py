#!/usr/bin/env python3
from ev3dev2.motor import *
from time import sleep
import os


os.system('setfont Lat15-TerminusBold14')
mM = MediumMotor('outA')
mL = LargeMotor('outB')
mR = LargeMotor('outC')
tank_pair= MoveTank('outB', 'outC', motor_class=LargeMotor)
spped_val_tank = 25
rotation_val_tank = 0.065
time_val_tank = 0.2
sleeptime = 2
spped_val_mV = 15
rotation_val_mM = 0.032


iter_tank = 4
for i in range(iter_tank):
    tank_pair.on_for_rotations(left_speed=spped_val_tank, right_speed=spped_val_tank, rotations=rotation_val_tank, brake=True, block=True)
    tank_pair.wait_until_not_moving()
    sleep(sleeptime)  



iter_mM = 2
for i in range(iter_mM):
    mM.on_for_rotations(speed=-spped_val_mV, rotations=rotation_val_mM, brake=True, block=True)
    mM.wait_until_not_moving()
    sleep(sleeptime)    

for i in range(iter_tank):
    tank_pair.on_for_rotations(left_speed=-spped_val_tank, right_speed=-spped_val_tank, rotations=rotation_val_tank, brake=True, block=True)
    tank_pair.wait_until_not_moving()
    sleep(sleeptime)      

for i in range(iter_mM):
    mM.on_for_rotations(speed= spped_val_mV, rotations=rotation_val_mM, brake=True, block=True)
    mM.wait_until_not_moving()
    sleep(sleeptime)   
# for i in range(4):
#     mM.on_for_seconds(speed = spped_val, seconds=time_val)
#     mM.wait_until_not_moving()
#     sleep(1)

# for i in range(4):
#     mM.on_for_seconds(speed = -spped_val, seconds=time_val)
#     mM.wait_until_not_moving()
#     sleep(1)   

