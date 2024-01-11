This is a repository for kids to learning micropython on ESP32 board
# 通用学习课件：
[参考以下网站] https://doc.itprojects.cn/0006.zhishi.esp32/02.doc/index.html#/README
[视频地址] https://www.bilibili.com/video/BV1G34y1E7tE/?spm_id_from=333.337.search-card.all.click
# 环境搭建：
[参考以下网页] https://blog.csdn.net/Little_Carter/article/details/128597071
开发板已经烧好micropython image，无须烧录，只需要下载Thonny，配置解释器，链接板子即可
# 学习步骤
先学习交通灯，然后学习蜂鸣器，再学习数码管显示。最后把三个例子结合到一起做一个倒计时 + 声音提醒的交通灯
# 目录结构
|目录|内容|
|---|---|
|***traffic light***|交通灯|
|***buzzer***| 蜂鸣器 |
|***7_seg_led***| 数码管显示 |

# ESP32板子管脚解释
|名称|作用|
|---|---|
|***D0, D12, D13...***|GPIO（通用输入输出管脚）|
|***IO*** |Input/Output(输入/输出)|
|***3v3***|3.3V电源正极|
|***VCC*** |电源正极，输入的话一般接3.3V|
|***GND*** |电源负极|

