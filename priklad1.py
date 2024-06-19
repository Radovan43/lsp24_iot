from neopixel import NeoPixel
from machine import Pin
from time import sleep

np = NeoPixel(Pin(40),12)

np.fill((0,0,0))
np.write()

red = Pin(33, Pin.OUT)
green = Pin(18, Pin.OUT)
blue = Pin(16, Pin.OUT)

def rgb(r, g, b):
    red.value(r)
    green.value(g)
    blue.value(b)

def blik(delay):
    while True:
        red.value(1)
        sleep(delay)
        red.value(0)
        green.value(1)
        sleep(delay)
        green.value(0)
        blue.value(1)
        sleep(delay)
        blue.value(0)
