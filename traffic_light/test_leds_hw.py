from machine import Pin, PWM
import time


Red = Pin(14, Pin.OUT)
Green = Pin(13, Pin.OUT)
Yellow = Pin(12, Pin.OUT)

Red.value(1)
Yellow.value(1)
Green.value(1)

time.sleep_ms(3000)

Red.value(0)
Yellow.value(0)
Green.value(0)
   
   
        

