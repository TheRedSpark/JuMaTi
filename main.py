from machine import Pin
import time

led = Pin("LED", Pin.OUT)
rotAuto = Pin(2, Pin.OUT)
gruenAuto = Pin(4, Pin.OUT)
gelbAuto = Pin(6, Pin.OUT)
taster = Pin(12, Pin.IN, Pin.PULL_DOWN)

led(0)
rotAuto(0)
time.sleep(0.1)
gruenAuto(0)
time.sleep(0.1)
gelbAuto(0)

while True:
    if taster.value() == 1:
        led(1)
        time.sleep(0.5)
        led(0)

    else:
        rotAuto(1)
        time.sleep(0.2)
        gruenAuto(1)
        time.sleep(0.2)
        gelbAuto(1)

        time.sleep(1)

        rotAuto(0)
        time.sleep(0.2)
        gruenAuto(0)
        time.sleep(0.2)
        gelbAuto(0)
