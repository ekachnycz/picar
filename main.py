from machine import Pin, PWM
from random import randint
from hcsr04 import HCSR04
import time

#// left motor
leftMotorSpeedPin = Pin(2, Pin.OUT)
leftMotorForwardPin = Pin(3, Pin.OUT)
leftMotorBackwardPin = Pin(4, Pin.OUT)

#// right motor
rightMotorSpeedPin = Pin(7, Pin.OUT)
rightMotorForwardPin = Pin(8, Pin.OUT)
rightMotorBackwardPin = Pin(9, Pin.OUT)

def getDistance():
    sensor = HCSR04(trigger_pin=17, echo_pin=16, echo_timeout_us=100000)
    distance = sensor.distance_cm()
    return distance

def goBackward():
    leftMotorSpeedPin(1)
    rightMotorSpeedPin(1)
    leftMotorForwardPin(0)
    leftMotorBackwardPin(1)
    rightMotorForwardPin(0)
    rightMotorBackwardPin(1)
    print("Going backward")
    return

def goForward():
    leftMotorSpeedPin(1)
    rightMotorSpeedPin(1)
    leftMotorForwardPin(1)
    leftMotorBackwardPin(0)
    rightMotorForwardPin(1)
    rightMotorBackwardPin(0)
    print("Going forward")
    return
    
def stop():
    leftMotorSpeedPin(0)
    rightMotorSpeedPin(0)
    leftMotorForwardPin(0)
    leftMotorBackwardPin(0)
    rightMotorForwardPin(0)
    rightMotorBackwardPin(0)
    print("stop")
    return
    
def goRight():
    leftMotorSpeedPin(1)
    rightMotorSpeedPin(1)
    leftMotorForwardPin(1)
    leftMotorBackwardPin(0)
    rightMotorForwardPin(0)
    rightMotorBackwardPin(1)
    print("going Right")
    return
    
def goLeft():
    leftMotorSpeedPin(1)
    rightMotorSpeedPin(1)
    leftMotorForwardPin(0)
    leftMotorBackwardPin(1)
    rightMotorForwardPin(1)
    rightMotorBackwardPin(0)
    print("GOing Left")
    return

while True:
    distance = getDistance()
    print(distance)
    goForward()
    if (distance > 0  and distance < 15):
        goBackward()
        time.sleep(5)
        goRight()
        time.sleep(3)
        stop()
    else:
        goForward()
    



