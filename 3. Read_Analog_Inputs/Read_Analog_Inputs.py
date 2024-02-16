# IMPORTING LIBRARIES

import machine
import utime

# INTIALIZATION

myPOT = 26 # GPIO 26 PIN OF ADC0
myPOT = machine.ADC(myPOT)

#PROGRAM BY FASIH ULLAH SALEEM

while True:
    potVal = myPOT.read_u16() # AS THE ADC OF RASPBERRY PI PICO IS '16 bit'
    # I USED 'round()' FUNCTION TO ROUND OF THE VALUE
    print(f'The voltages are {round(potVal/65535 * 3.3 , 2)} V.')
    utime.sleep(0.5)