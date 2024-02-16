# IMPORTING LIBRARIES

from machine import Pin
from  utime import sleep

# INITIAZING THE LEDs

myLED_0 = Pin(15 , Pin.OUT)
myLED_1 = Pin(14 , Pin.OUT)
# PROGRAM BY FASIH ULLAH SALEEM
while True:
    print('--- BINARY COUNTER BY FASIH ULLAH SALEEM ---')
    #00
    myLED_0.value(0)
    myLED_1.value(0)
    print('00')
    sleep(0.5)
    #01
    myLED_0.value(1)
    myLED_1.value(0)
    print('01')
    sleep(0.5)
    #10
    myLED_0.value(0)
    myLED_1.value(1)
    print('10')
    sleep(0.5)
    #11
    myLED_0.value(1)
    myLED_1.value(1)
    print('11')
    sleep(0.5)
    
    
    