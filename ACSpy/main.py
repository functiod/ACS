import time
import matplotlib as plt
import numpy as np
from acspy import acsc

hcomm = acsc.openCommEthernetTCP()

axis_1 = 1
axis_0 = 0
transverse_angle = 90
start_ax_0 = 90
start_ax_1 = 0
end_ax_0 = start_ax_0 + transverse_angle
end_ax_1 = 360
steps = 3
velocity = 200
flag = 1


#Initialize axis
def init_hcomm(hcomm, axis):
    acsc.enable(hcomm, axis)
    time.sleep(1)
    acsc.commutate(hcomm, axis)
    acsc.waitCommutated(hcomm, axis)
    time.sleep(1)
    #print(acsc.getMotorState(hcomm, axis), acsc.getAxisState(hcomm, axis))

#logical (initial) position
def logical_position(hcomm, axis, angle_start, angle_end):
    if (angle_end < 0):
        if (angle_start <= angle_end):
            while angle_start <= angle_end:
                angle_start = acsc.getFPosition(hcomm, axis)
                time.sleep(0.03)
        else:
            while angle_start >= angle_end:
                angle_start = acsc.getFPosition(hcomm, axis)
                time.sleep(0.03)
    elif (angle_end > 0):
        if (angle_start <= angle_end):
            while angle_start <= angle_end:
                angle_start = acsc.getFPosition(hcomm, axis)
                time.sleep(0.03)
        else:
            while angle_start >= angle_end:
                angle_start = acsc.getFPosition(hcomm, axis)
                time.sleep(0.03)
    else:
        while angle_start != angle_end:
                angle_start = acsc.getFPosition(hcomm, axis)
                time.sleep(0.03)

#Axis motion from start angle to end angle
def event_orient_motion(hcomm, axis, angle_start, angle_end, velocity):
    acsc.setVelocity(hcomm, axis, velocity)
    acsc.toPoint(hcomm, 0, axis, angle_end)
    time.sleep(0.03)
    logical_position(hcomm, axis, angle_start, angle_end)

#Axis 1 step by step motion
def step_by_step_axis_1(hcomm, axis, angle_start, angle_end, velocity):
    while angle_start < angle_end - 10:
        angle_start = acsc.getFPosition(hcomm, axis)
        event_orient_motion(hcomm, axis, angle_start, angle_start + 10, velocity)
        print(acsc.getFPosition(hcomm, axis))
        time.sleep(0.01)

#axis initialization 
init_hcomm(hcomm, axis_0)
init_hcomm(hcomm, axis_1)
print(acsc.getFPosition(hcomm, 0))
print(acsc.getFPosition(hcomm, 1))

acsc.setFPosition(hcomm, axis_0, 0.00000)


'''
if (round(acsc.getFPosition(hcomm, axis_0)) != start_ax_0) or round(acsc.getFPosition(hcomm, axis_1)) != start_ax_1:
    event_orient_motion(hcomm, axis_0, acsc.getFPosition(hcomm, axis_0), start_ax_0, velocity)
    event_orient_motion(hcomm, axis_1, acsc.getFPosition(hcomm, axis_1), start_ax_1, velocity)
print(acsc.getFPosition(hcomm, axis_0), acsc.getFPosition(hcomm, axis_1))

while flag:
    for step in list(range(-3, 3, 1)):
        event_orient_motion(hcomm, axis_0, acsc.getFPosition(hcomm, axis_0), acsc.getFPosition(hcomm, axis_0) - step * transverse_angle / steps, velocity)
        step_by_step_axis_1(hcomm, axis_1, acsc.getFPosition(hcomm, axis_1), acsc.getFPosition(hcomm, axis_1) + end_ax_1, velocity)
    if acsc.getFPosition(hcomm, axis_0) <= end_ax_0:
        flag = 1
    else:
        flag = 0
'''

acsc.disable(hcomm, axis_0)
acsc.disable(hcomm, axis_1)
acsc.closeComm(hcomm)