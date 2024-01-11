import tm1637   #导入TM1637芯片包，需要把tm1637.py保存到板子上
from machine import Pin
import time

tm = tm1637.TM1637(clk=Pin(2), dio=Pin(4))

# all LEDS off
tm.write([0, 0, 0, 0])

colon_on = True
count = 0
while True:
    count = count + 1  #设置技术，用来闪冒号
    sec_val = time.localtime()[5]  #获取系统时间的秒数
    min_val = time.localtime()[4]  #获取系统时间的分钟数

    if (count % 2 == 0):  #如果count能被2整除，比如0， 2， 4的时候 设置冒号显示为True
        colon_on = True
    else:                 #count不能被2整除，设置冒号显示为False
        colon_on = False

    tm.numbers(min_val, sec_val, colon_on) #显示分钟，描述和冒号
    time.sleep_ms(500)    #延时500毫秒
