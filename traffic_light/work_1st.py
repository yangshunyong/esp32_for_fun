from machine import Pin, PWM
import time


red = Pin(14, Pin.OUT)
green = Pin(13, Pin.OUT)
yellow = Pin(12, Pin.OUT)

#程序开始，初始化所有灯为灭的状态
red.value(0)
yellow.value(0)
green.value(0)

while True:				#死循环，代码不退出，一直循环后面的操作
   red.value(1)
   time.sleep_ms(3000)
   red.value(0)
   
   yellow.value(1)
   time.sleep_ms(500)
   yellow.value(0)
   
   green.value(1)
   time.sleep_ms(3000)
   green.value(0)
   
   yellow.value(1)
   time.sleep_ms(500)
   yellow.value(0)
   
   
        
