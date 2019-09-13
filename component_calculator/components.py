from math import log
from math import pi

def duty_cycle(v_led, vin):
    return (v_led/(vin*0.9))
def off_time(switching_freq, duty_cycle):
    return (1/switching_freq)*(1-duty_cycle)
def off_time_resistor(off_time, v_led):
    denom = -470*log(1-1/v_led) #470pf is the capacitance of the inductor
    return off_time/denom
def min_inductance(v_led, t_off, current):
    return (v_led*t_off)/(current*0.4)#the 0.4 is a constant accounting for 40% inductor ripple
def inductor_peak(V_iadj, current, r_sense):
    return (V_iadj/10)/r_sense
def sense_resistance(v_iadj, current):
    num = v_iadj/10
    denom = current + ((current*0.40)/2)
    return num/denom
def input_capacitance(current, switching_freq, t_off):
    num = current*((1/switching_freq*1000)-t_off)
    denom = 2
    return num/denom
def initial_capacitance(led_current, led_ripple_curent, switching_freq, dynamic_resistance):
    inductance_ripple = led_current*0.45
    num = inductance_ripple-led_ripple_curent
    denom = led_ripple_curent*(2*pi*switching_freq)*dynamic_resistance
    return num/denom
    

V_LED = 3.4 #forward led voltage
n=1#number of lights in series
vin =36 #power supple voltage
switching_freq = 580 #580 kHz
led_current = 1.5 #1.5 amps
v_iadj = 2.4
dynamic_resistance = .0222*n #number is from data sheet
r2=54.9 #kOhms
r3=1964#kOhms
led_current_ripple = 0.15 #Not sure where this comes from


D = duty_cycle(V_LED, vin)
print("Duty Cycle: " + str(D))
t_off = off_time(switching_freq, D)*1000 #returns off time in microseconds
print("Off Time: " + str(t_off))
r_off = off_time_resistor(t_off, V_LED)*1000000 #the powers of ten fix the units
print("Off Time Resistor: " + str(r_off))
inductance = min_inductance(V_LED, t_off, led_current)#the units are in milli henrys
print ("inductance: "+ str(inductance))
sense_res= sense_resistance(v_iadj, led_current)
print ("Sense Resistance: " + str (sense_res))
input_cap = input_capacitance(led_current, switching_freq,t_off)*1000 #returns the result in nanofarads
print ("input capacitance: " + str(input_cap))
C_0= initial_capacitance(led_current, led_current_ripple, switching_freq, dynamic_resistance)*1000000
print ("initial_capacitance: "+ str(C_0))



