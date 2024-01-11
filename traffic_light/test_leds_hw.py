from machine import Pin 	# 从machine 包中导入Pin（管脚）模块
import time 				#导入time包


Red = Pin(14, Pin.OUT)		#定义红灯对应的管脚，并设置为输出
Green = Pin(13, Pin.OUT)	#定义绿灯对应的管脚，并设置为输出
Yellow = Pin(12, Pin.OUT)	#定义黄灯对应的管脚，并设置为输出

Red.value(1)				#红灯管脚输出1，高电平，亮红灯
Yellow.value(1)				#黄灯管脚输出1，高电平，亮红灯
Green.value(1)				#绿灯管脚输出1，高电平，亮红灯

time.sleep_ms(3000)			#延时等待3000ms（毫秒），也就是3秒

Red.value(0)				#红灯管脚输出0，低电平，关红灯
Yellow.value(0)				#黄灯管脚输出0，低电平，关红灯
Green.value(0)				#绿灯管脚输出0，低电平，关红灯
   
   
        

