# Import the Library to Interact with GPIOs of the Raspberry Pi Pico
from machine import Pin

# Importing the create the Delay
from time import sleep

# Initializing the LED
myLED = Pin('LED' , Pin.OUT)

# Creating the Function for testing
def myFunction():
    temp = 34
    return f'Hello Fasih Ullah'

while True:
    # We have two method we can use 'myLED.on()' or 'myLED.value(1)'
    # Vice versa for off
    myLED.on()
    sleep(1)
    myLED.off()
    sleep(1)
    print(myFunction())
    # WE CAN ALSO USE 'myLED.toggle()'
