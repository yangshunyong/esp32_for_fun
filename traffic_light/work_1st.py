from machine import Pin, PWM
import time


Red = Pin(14, Pin.OUT)
Green = Pin(13, Pin.OUT)
Yellow = Pin(12, Pin.OUT)

#程序开始，初始化所有灯为灭的状态
Red.value(0)
Yellow.value(0)
Green.value(0)

while True:				#死循环，代码不退出，一直循环后面的操作
   Red.value(1)
   time.sleep_ms(3000)
   Red.value(0)
   
   Yellow.value(1)
   time.sleep_ms(500)
   Yellow.value(0)
   
   Green.value(1)
   time.sleep_ms(3000)
   Green.value(0)
   
   Yellow.value(1)
   time.sleep_ms(500)
   Yellow.value(0)
   
   
        
