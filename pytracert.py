#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author: tsunc & zadmine
@software: PyCharm Community Edition
@time: 2017/12/25 14:10
"""

#coding=utf-8

import re 
import urllib
import os,sys
from bs4 import BeautifulSoup as soup

reload(sys)
sys.setdefaultencoding('utf-8')


def get_ip(ip):
    a = []
    url = "http://www.ip138.com/ips138.asp?ip={0}&action=2".format(ip)
    #print url
    opurl = urllib.urlopen(url)
    o_data = opurl.read()
    opurl.close()
    c = soup(o_data,"lxml")
    data = c.find_all("table",{"width":"80%"})
    for x in  data:
        x_l = ''.join(re.findall(u'本站数据：(.*)', x.li.text))
        return  '    >>>>   %s \n' % (x_l)

def tracertIP(ip): 
	print u'访问%s 经过的路由如下：\n' % ip
	p = subprocess.Popen(['tracert', '-d', ip], stdout=subprocess.PIPE)
	while True:
		line = p.stdout.readline()
		if not line:
			break
		print line,
		b = re.compile(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})')
		d = b.findall(line)
		if d != []:
		    print (get_ip(d[0]))
		else:
			print u"     *        *        *     Request Timeout。"





if __name__ == '__main__':
	tracertIP(sys.argv[1])
