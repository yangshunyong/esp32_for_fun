from machine import Pin
import time

buzzer = Pin(5, Pin.OUT)

buzzer.value(1)
time.sleep_ms(500)      #延时 1ms(毫秒)
buzzer.value(0)

