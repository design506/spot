# -*- coding: utf-8 -*-

from __future__ import division
import time

# Import the PCA9685 module.
import Adafruit_PCA9685


# Uncomment to enable debug output.cd 
#import logging
#logging.basicConfig(level=logging.DEBUG)

# Initialise the PCA9685 using the default address (0x40).
pwm = Adafruit_PCA9685.PCA9685()

# Alternatively specify a different address and/or bus:
#pwm = Adafruit_PCA9685.PCA9685(address=0x41, busnum=2)

# Configure min and max servo pulse lengths
servo_min = 150  # Min pulse length out of 4096
servo_max = 600  # Max pulse length out of 4096


rra = 0 #rear right arm 
rrm = 1 #rear right mid
rrw = 2 #rear right wrist 

rla = 4 #front left arm 
rlm = 5 #front left mid
rlw = 6 #front left wrist 

fra = 8 #front right arm 
frm = 9 #front right mid
frw = 10 #front right wrist 

fla = 12 #front left arm 
flm = 13 #front left mid
flw = 14 #front left wrist 


fra_center = 320 #front right arm # 위로 +
frm_center = 290 #front right mid  # 위로 -
frw_cneter = 460 #front right wrist # 위로 +

fla_center = 550 #front left arm  # 위로 -
flm_center = 500 #front left mid # 위로 +
flw_cneter = 230 #front left wrist # 위로 -

rra_center = 260 #rear right arm 
rrm_center = 490 #rear right mid   # 위로 -
rrw_cneter = 440 #rear right wrist  # 위로 +

rla_center = 530 #rear left arm # 위로 -
rlm_center = 330 #rear left mid # 위로 -
rlw_cneter = 350 #rear left wrist # 위로 -

# Helper function to make setting a servo pulse width simpler.
def set_servo_pulse(channel, pulse):
    pulse_length = 1000000    # 1,000,000 us per second
    pulse_length //= 60       # 60 Hz
    print('{0}us per period'.format(pulse_length))
    pulse_length //= 4096     # 12 bits of resolution
    print('{0}us per bit'.format(pulse_length))
    pulse *= 1000
    pulse //= pulse_length
    pwm.set_pwm(channel, 0, pulse)

# Set frequency to 60hz, good for servos.
pwm.set_pwm_freq(60)

print('Moving servo on channel 0, press Ctrl-C to quit...')


def stanbye():
    pwm.set_pwm(fla, 0, fla_center)
    pwm.set_pwm(flm, 0, flm_center)
    pwm.set_pwm(flw, 0, flw_cneter)
    
    pwm.set_pwm(fra, 0, fra_center)
    pwm.set_pwm(frm, 0, frm_center)
    pwm.set_pwm(frw, 0, frw_cneter)
   
    pwm.set_pwm(rla, 0, rla_center)
    pwm.set_pwm(rlm, 0, rlm_center)
    pwm.set_pwm(rlw, 0, rlw_cneter)

    pwm.set_pwm(rra, 0, rra_center)
    pwm.set_pwm(rrm, 0, rrm_center)
    pwm.set_pwm(rrw, 0, rrw_cneter)

    print("mode : stanbye ")

def sitdown():
    pwm.set_pwm(fla, 0, fla_center)
    pwm.set_pwm(flm, 0, 550)
    pwm.set_pwm(flw, 0, 150)
    
    pwm.set_pwm(fra, 0, fra_center)
    pwm.set_pwm(frm, 0, 270)
    pwm.set_pwm(frw, 0, 560)
   
    pwm.set_pwm(rla, 0, rla_center)
    pwm.set_pwm(rlm, 0, 370)
    pwm.set_pwm(rlw, 0, 270)

    pwm.set_pwm(rra, 0, rra_center)
    pwm.set_pwm(rrm, 0, 470)
    pwm.set_pwm(rrw, 0, 540)

    print("mode : sitdown ")

def standup():
    pwm.set_pwm(fla, 0, fla_center)
    pwm.set_pwm(flm, 0, 550 - 50)
    pwm.set_pwm(flw, 0, 150 + 100)
    
    pwm.set_pwm(fra, 0, fra_center)
    pwm.set_pwm(frm, 0, 270 + 50)
    pwm.set_pwm(frw, 0, 560 - 100)
   
    pwm.set_pwm(rla, 0, rla_center)
    pwm.set_pwm(rlm, 0, 370 - 50)
    pwm.set_pwm(rlw, 0, 270 + 100)

    pwm.set_pwm(rra, 0, rra_center)
    pwm.set_pwm(rrm, 0, 470 + 70)
    pwm.set_pwm(rrw, 0, 540 - 110)

    print("mode : standup ")

def motion(action):
    
    if(action == "forward"):

        pwm.set_pwm(fra, 0, fra_center)
        pwm.set_pwm(frm, 0, frm_center + 40)
        pwm.set_pwm(frw, 0, frw_cneter + 30)

        
        pwm.set_pwm(rla, 0, rla_center)
        pwm.set_pwm(rlm, 0, rlm_center - 40)
        pwm.set_pwm(rlw, 0, rlw_cneter - 40)
        
        
        pwm.set_pwm(fla, 0, fla_center)
        pwm.set_pwm(flm, 0, flm_center)
        pwm.set_pwm(flw, 0, flw_cneter)
        
        pwm.set_pwm(rra, 0, rra_center)
        pwm.set_pwm(rrm, 0, rrm_center)
        pwm.set_pwm(rrw, 0, rrw_cneter)

    
        time.sleep(3)
    
        
        pwm.set_pwm(fra, 0, fra_center)
        pwm.set_pwm(frm, 0, frm_center)
        pwm.set_pwm(frw, 0, frw_cneter)
    
        pwm.set_pwm(rla, 0, rla_center)
        pwm.set_pwm(rlm, 0, rlm_center)
        pwm.set_pwm(rlw, 0, rlw_cneter)
    
        
        pwm.set_pwm(fla, 0, fla_center)
        pwm.set_pwm(flm, 0, flm_center - 30)
        pwm.set_pwm(flw, 0, flw_cneter - 30)
        

        pwm.set_pwm(rra, 0, rra_center)
        pwm.set_pwm(rrm, 0, rrm_center + 40)
        pwm.set_pwm(rrw, 0, rrw_cneter + 40)
        
        
        time.sleep(3)


    if(action == "sitdown"):
       sitdown()
       time.sleep(3)
    
    if(action == "standup"):
       standup()
       time.sleep(3)


while True:    
    motion("sitdown")
    motion("standup")






    
    
    