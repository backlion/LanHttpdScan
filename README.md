# 内网C段 HTTP服务探测脚本

判断内网http服务存活脚本，存在http服务时获取网站title,有助快速查看内网http服务信息

## 使用说明

使用eventlet多携程遍历内网地址的端口服务开发状态

#### 1. `pip install eventlet`

#### 2. `python http5can 192.168.1.0/24 -t10`

```bash
└─[1] py lanhttpd5can.py 192.168.1.0/24
     _                  _   _ _   _             _   ____
    | |    __ _ _ __   | | | | |_| |_ _ __   __| | / ___|  ___ __ _ _ __
    | |   / _` | '_ \  | |_| | __| __| '_ \ / _` | \___ \ / __/ _` | '_ \
    | |__| (_| | | | | |  _  | |_| |_| |_) | (_| |  ___) | (_| (_| | | | |
    |_____\__,_|_| |_| |_| |_|\__|\__| .__/ \__,_| |____/ \___\__,_|_| |_|
                                     |_|

* Scan Start . . . .

* IP/MASK :  192.168.1.0/24

********  Url *************  Status *****  Server  ************  Title  **************
* http://192.168.1.*:80       200       httpd             None
* http://192.168.1.**:80      200       Apache            Apache2 Ubuntu Default Pa
* http://192.168.1.**:80      200       Apache            Pentester**
* http://192.168.1.**:80      200       Switch            Web ***
* http://192.168.1.**:80      200       Apache            None
* http://192.168.1.***:80     200       nginx             test
* http://192.168.1.***:80     200       Apache            None
* http://192.168.1.***:8080   200       Mrvl-R2_0         HP s***
* http://192.168.1.***:80     200       Mrvl-R2_0         HP ***
* http://192.168.1.***:80     200       Httpd             Web us***
* ......
****************************************************************************************
```
#### PS:线程数尽量不要超过100，太快的话会有扫不全的情况，基本在20-50就ok了。一个C段基本在一分钟内就跑完了。

