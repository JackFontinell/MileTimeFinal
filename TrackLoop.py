from djitellopy import tello
import KeyPressModule as kp
import numpy as np
from time import sleep
import cv2
import math

#These are importing the python librarys.

#Parameters
fspeed = 117/10 # Forward Speed in cm/s   (15cm/s)
aSpeed = 350/10 # Angular Speed Degrees/s    (50d/s)
interval = 0.25

dInterval = fSpeed*interval
aInterval = aSpeed*interval
x, y = 500, 500
a = 0
yaw = 0


kp.init()
tello = tello.Tello()
tello.connect()
print(tello.get_battery())


tello.move_forward()
points = [(0,0), (0,0)]
#This all goes with tello itslef and connecting it.

def getKeyboardInput():
    lr, fb, ud, yv = 0, 0, 0, 0
    speed = 15
    aspeed = 50
    global x,y,yaw, a
    d = 0

    if kp.getKey("LEFT"):
        lr = -speed
        s = dInterval
        a = -180

    elif kp.getKey("RIGHT"):
        lr = speed
        s = -dInterval
        a = 180

    if kp.getKey("UP"):
        fb = speed
        s = dInterval
        a = -270

    elif kp.getKey("DOWN"):
        fb = -speed
        s = -dInterval
        a = -90

    if kp.getKey("w"): ud = speed

    elif kp.getKey("s"): ud = -speed

    if kp.getKey("a"):
        yv = -speed
        yaw -= aInterval

    elif kp.getKey("d"):
        yv = speed

    if kp.getKey("q"): tello.land(); time.sleep(3)
    if kp.getKey("e"): tello.takeoff()

    sleep(interval)
    a =+ yaw
    x += int(d* math.cos(math,radians(a)))
    y += int(d* math.sin(math,radians(a)))

    return [lr, fb, ud, yv, x, y]


    return [lr, fb, ud, yv]

def drawPoints(img, points):
    for point in points:
        cv2.circle(img,point, 5, (0,0,255), cv2.FILLED)

    cv2.circle(img, points[-1], 8, (0,255,255), cv2.FILLED)

    cv2.putText(img,f'({(points[-1][0]- 500 )/100}, {(points[-1][1]- 500) /100})m',
                (points[-1][0] + 10, points[-1][1] + 30), cv2.FONT_HERSHEY_PLAIN, 1
                (255, 0, 255), 1)

while True:
    vals = getKeyboardInput()
    tello.send_rc_control(vals[0], vals[1], vals[2], vals[3])

    img = np.zeros((1000, 1000, 3), np.uint8)
    if points[-1][0] == vals[4] and points[-1][1] == vals[5]:
        pass
    else:
        points .appemd((vaks[4], vals[5]))
    drawPoints(img, points)
    cv2.imshow("Output", img)
    cv2.waitKey(1)