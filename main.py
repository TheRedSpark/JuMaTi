from machine import Pin
import time

led = Pin("LED", Pin.OUT)
rotAuto = Pin(2, Pin.OUT)
gruenAuto = Pin(6, Pin.OUT)
gelbAuto = Pin(4, Pin.OUT)
rotMensch = Pin(21, Pin.OUT)
gruenMensch = Pin(19, Pin.OUT)
taster = Pin(12, Pin.IN, Pin.PULL_DOWN)

led(0)
rotAuto(0)
time.sleep(0.1)
gruenAuto(0)
time.sleep(0.1)
gelbAuto(0)
time.sleep(0.1)
gruenMensch(0)
time.sleep(0.1)
rotMensch(0)

haltewunsch = False


def normal():
    gruenAuto(1)
    time.sleep(0.1)
    rotMensch(1)


def auto():
    gelbAuto(1)
    gruenAuto(0)
    time.sleep_ms(300)
    rotAuto(1)
    gelbAuto(0)
    time.sleep(1)

    time.sleep(2)  # The Rote Zeit

    time.sleep_ms(300)
    gelbAuto(1)
    time.sleep_ms(500)
    rotAuto(0)
    gelbAuto(0)
    gruenAuto(1)


def fussganger():
    gelbAuto(1)
    gruenAuto(0)
    time.sleep_ms(300)
    rotAuto(1)
    gelbAuto(0)
    time.sleep(1)
    rotMensch(0)
    gruenMensch(1)

    time.sleep(2)  # The Grüne Zeit

    gruenMensch(0)
    rotMensch(1)
    time.sleep_ms(300)
    gelbAuto(1)
    time.sleep_ms(500)
    rotAuto(0)
    gelbAuto(0)
    gruenAuto(1)


normal()

i = 0
#
while True:
    # Checking if the button is pressed. If it is, it will run the function fussganger() and reset the counter i to 0.
    if taster.value() == 1:
        fussganger()
        i = 0


    # Checking if the counter i is greater than 400. If it is, it will reset the counter to 0 and run the function auto().
    elif i > 400: # Anzahl der Minigrünphase
        i = 0
        auto()

    # The time between the green light for the cars and the green light for the pedestrians.
    else:
        time.sleep_ms(10)#Länge der Minigrünphase
        i += 1
