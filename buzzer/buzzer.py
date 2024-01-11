from machine import Pin
import time

TIME_BUZZ = 100
TIME_DELAY_FIRST = 200
TIME_DELAY_SECOND = 500

def buzzer_on(delay) :
    buzzer.value(1)
    time.sleep_ms(delay)
    buzzer.value(0)
    time.sleep_ms(delay)

#定义蜂鸣器管脚为D5
buzzer = Pin(5, Pin.OUT)

count = 0
while True:
    #蜂鸣器响三声，间隔200ms
    buzzer_on(TIME_BUZZ)
    buzzer_on(TIME_BUZZ)
    buzzer_on(TIME_BUZZ)
    #等待200ms
    time.sleep_ms(TIME_DELAY_FIRST)
    #蜂鸣器响两声，间隔200ms
    buzzer_on(TIME_BUZZ)
    buzzer_on(TIME_BUZZ)
    #等待500ms
    time.sleep_ms(TIME_DELAY_SECOND)
