import tm1637   #导入TM1637芯片包，需要把tm1637.py保存到板子上
from machine import Pin
import time

tm = tm1637.TM1637(clk=Pin(2), dio=Pin(4))

# all LEDS off
tm.write([0, 0, 0, 0])

count = 0
while True:
    count = count + 1     #递增变量count
    if (count >= 9999) :  #大于9999返回0， 不然始终显示9999
        count = 0

    tm.number(count)
    time.sleep_ms(1)      #延时 1ms(毫秒)

