from machine import Pin, PWM
import time

red = Pin(14, Pin.OUT)
green = Pin(13, Pin.OUT)
yellow = Pin(12, Pin.OUT)

def init_leds():
    #程序开始，初始化所有灯为灭的状态
    red.value(0)
    yellow.value(0)
    green.value(0)

def toggle_led(led, delay) :
    led.value(1)
    time.sleep_ms(delay)
    led.value(0)


init_leds()

while True:				#死循环，代码不退出，一直循环后面的操作
    toggle_led(red, 3000)
    toggle_led(yellow, 500)
    toggle_led(green, 3000)
    toggle_led(yellow, 500)
   
        

