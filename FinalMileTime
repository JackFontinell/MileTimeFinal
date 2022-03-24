from djitellopy import tello
import numpy as np
from time import sleep
import math

tello = tello.Tello()
tello.connect()
print(tello.get_battery())


tello.takeoff()

tello.move_up(90)
sleep(2)

tello.move_forward(500)
sleep(0.1)

tello.move_forward(500)
sleep(0.1)

#stop forward command
tello.send_rc_control(0,0,0,0)
sleep(2)

#rotate while turning x and y direction
tello.send_rc_control(0, 50, 0, 38)
sleep(8)

#stop turn and rotation
tello.send_rc_control(0, 0, 0, 0)
sleep(2)

tello.move_forward(500)
sleep(0.1)

tello.move_forward(500)
sleep(0.1)

#stop forward command
tello.send_rc_control(0,0,0,0)
sleep(2)

#rotate while turning x and y direction
tello.send_rc_control(0, 50, 0, 38)
sleep(8)

#stop turn and rotation
tello.send_rc_control(0, 0, 0, 0)
sleep(2)

tello.land()
#610 cm sideways
