# -*- coding: utf-8 -*-

from gpiozero import DistanceSensor
from time import sleep

sensor = DistanceSensor(echo=24, trigger=23)

while True:
    
    dst = "%.1f" % (sensor.distance * 100)
    
    print('Distance ', dst, 'Cm')
    sleep(1)




