# -*- coding:utf-8 -*-
# Author : Funhity

import sys
from IPy import IPy
import eventlet
import re
requests = eventlet.import_patched('requests.__init__')
import time

port_list = ['80','6379', '7001','7002','9002']
for port in range(8000,8090):
    port_list.append(str(port))



def scan(url):
    title = ''
    status = [200,403,404,503]
    try:
        resp = requests.get(url,timeout=2)
        if resp.status_code in status :
            pattern = re.compile(r'<title>(.*?)</title>')
            match = pattern.search(resp.text)
            title = match.group(1) if match else ''
            print "*     %-29s  %-30s" % (url,title)                   
    except Exception as e:
        pass

def run(ip,thread):
    port_pool = eventlet.GreenPool(thread)
    for port in port_list:
        url = "http://%s:%s" % (str(ip),port)
        port_pool.spawn(scan,url)

    port_pool.waitall()

if __name__=="__main__":
    if len(sys.argv) < 2:
        sys.exit("python http5can 192.168.1.1/24 -t10")
    else:
        try:
            ip_list = IPy.IP(sys.argv[1])
        except Exception as e:
            sys.exit('Invalid /MASK, %s' % e)
        if len(sys.argv) is 3:
            thread = int(sys.argv[2].replace('-t', ''))
        else:
            thread = 10
    print   "     _   _ _   _        ____                             ____"
    print   "    | | | | |_| |_ _ __/ ___|  ___ _ ____   _____ _ __  / ___|  ___ __ _ _ __"
    print   "    | |_| | __| __| '_ \___ \ / _ \ '__\ \ / / _ \ '__| \___ \ / __/ _` | '_ \\"
    print   "    |  _  | |_| |_| |_) |__) |  __/ |   \ V /  __/ |     ___) | (_| (_| | | | |"
    print   "    |_| |_|\__|\__| .__/____/ \___|_|    \_/ \___|_|    |____/ \___\__,_|_| |_|"
    print   "                  |_|"
    print   ""
    print "* Scan Start . . . ."
    print " "
    print "* IP/MASK :  " + sys.argv[1]
    print
    print "****************  URL  *******************   TITLE   ****************"
    ip_pool = eventlet.GreenPool(thread)
    for ip in ip_list:
        ip_pool.spawn(run, ip, thread)
    ip_pool.waitall()
    print "*********************************************************************"
