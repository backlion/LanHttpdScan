# -*- coding:utf-8 -*-
# Author : Funhity

import sys
from IPy import IPy
import eventlet
import re
reload(sys)
sys.setdefaultencoding('utf-8')
requests = eventlet.import_patched('requests.__init__')
import time


port_list = ['80','6379', '7001','7002','9001','9002']
for port in range(8000,8090):
    port_list.append(str(port))
header = {'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.125 Safari/537.36','Connection':'close'}



def scan(url):
    title = ''
    banner= ''
    try:
        resp = requests.get(url,headers=header,timeout=2)
        pattern = re.compile(r'<title>(.*?)</title>')
        
        match = pattern.search(resp.content)
        title = match.group(1)[:25] if match else 'None'

        status = resp.status_code
        try:
            banner = resp.headers['Server'][:12]
        except:pass
        print "* %-25s   %-5d     %-15s   %-25s " % (url,status,banner,title)                   
    except:pass
        

def run(ip,thread):
    port_pool = eventlet.GreenPool(thread)
    for port in port_list:
        url = "http://%s:%s" % (str(ip),port)
        port_pool.spawn(scan,url)

    port_pool.waitall()

if __name__=="__main__":
    if len(sys.argv) < 2:
        sys.exit("python lanhttpscan 192.168.1.0/24 -t10")
    else:
        try:
            ip_list = IPy.IP(sys.argv[1])
        except Exception as e:
            sys.exit('Invalid/MASK, %s' % e)
        if len(sys.argv) is 3:
            thread = int(sys.argv[2].replace('-t', ''))
        else:
            thread = 10
    print   "     _                  _   _ _   _             _   ____"
    print   "    | |    __ _ _ __   | | | | |_| |_ _ __   __| | / ___|  ___ __ _ _ __"
    print   "    | |   / _` | '_ \  | |_| | __| __| '_ \ / _` | \___ \ / __/ _` | '_ \\"
    print   "    | |__| (_| | | | | |  _  | |_| |_| |_) | (_| |  ___) | (_| (_| | | | |"
    print   "    |_____\__,_|_| |_| |_| |_|\__|\__| .__/ \__,_| |____/ \___\__,_|_| |_|"
    print   "                                     |_|"
    print   ""
    print "* Scan Start . . . ."
    print " "
    print "* IP/MASK :  " + sys.argv[1]
    print
    print "********  Url *************  Status ******  Server  ************  Title  **************"
    ip_pool = eventlet.GreenPool(thread)
    for ip in ip_list:
        ip_pool.spawn(run, ip, thread)
    ip_pool.waitall()
    print "***************************************************************************************"
