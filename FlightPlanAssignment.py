from djitellopy import Tello
from time import sleep

tello = Tello()
tello.connect()
sleep(2)
tello.takeoff()
sleep(.5)

tello.move_up(102)
sleep(.5)

tello.move_forward(152)
sleep(.5)

tello.rotate_counter_clockwise(90)
sleep(.5)

tello.move_forward(183)
sleep(.5)

tello.rotate_clockwise(90)
sleep(.5)

tello.move_down(91)
sleep(.5)

tello.move_forward(91)
sleep(.5)

tello.rotate_clockwise(90)
sleep(.5)

tello.move_up(30)
sleep(.5)

tello.move_forward(91)
sleep(.5)

tello.rotate_counter_clockwise(90)
sleep(.5)

tello.move_forward(183)
sleep(2)

tello.curve_xyz_speed()

tello.land()
tello.end()