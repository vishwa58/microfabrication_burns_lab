#https://sourceforge.net/p/raspberry-gpio-python/wiki/PWM/

import RPi.GPIO as IO
import time

import time                            #calling time to provide delays in program
IO.setwarnings(False)           #do not show any warnings
IO.setmode (IO.BCM)         #we are programming the GPIO by BCM pin numbers. (PIN35 as ‘GPIO19’)
IO.setup(19,IO.OUT)           # initialize GPIO19 as an output.
p = IO.PWM(19,100)          #GPIO19 as PWM output, with 100Hz frequency
p.start(0)                              #generate PWM signal with 0% duty cycle
while 1: 
    p.start(25)                              #execute loop forever
    time.sleep(0.1)           #sleep for 100m second