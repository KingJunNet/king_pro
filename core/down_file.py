# -*- coding: utf-8 -*-
import os
from log import *
import requests
from bs4 import BeautifulSoup

request_header = {'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
            'Accept':"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            'Accept-Encoding':'gzip',
           }

user_agent_list = [
	"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
	"Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
	"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
	"Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
	"Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
	"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
	"Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
	"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
	"Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
	"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
	"Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
	"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
	"Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
	"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
	"Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
	"Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
	"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
	"Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"
]

# def download_img_file(img_url,file_path):
#     try:
#         # img_url="https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1510731843&di=dc1a96450da333fff562d80297cda7bd&imgtype=jpg&er=1&src=http%3A%2F%2Ff.hiphotos.baidu.com%2Fbaike%2Fw%253D268%253Bg%253D0%2Fsign%3D379b33558bd4b31cf03c93bdbfed4042%2F2cf5e0fe9925bc312116298e5edf8db1cb137058.jpg"
#         #img_url="http://p.vxotu.com/u/20171107/09214533.jpg"
#         request = requests.get(img_url, headers=request_header)
#         img_content = request.content
#         fp = open(file_path, 'wb')
#         fp.write(img_content)
#         print img_content
# 		  print 'jieshu'
#         fp.close()
#     except Exception, e:
#         print e
#
#     return file_path

def download_img_file(img_url,file_path):
	try:
		# img_url="https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1510731843&di=dc1a96450da333fff562d80297cda7bd&imgtype=jpg&er=1&src=http%3A%2F%2Ff.hiphotos.baidu.com%2Fbaike%2Fw%253D268%253Bg%253D0%2Fsign%3D379b33558bd4b31cf03c93bdbfed4042%2F2cf5e0fe9925bc312116298e5edf8db1cb137058.jpg"
		# img_url="http://p.vxotu.com/u/20171107/09214533.jpg"
		request = requests.get(img_url, headers=request_header)
		img_content = request.content
		file_path = file_path.decode('utf-8', 'ignore').encode('gbk')
		fp = open(file_path, 'wb')
		fp.write(img_content)
		print img_content
		fp.close()
		log_info("下载文件:%s"%(file_path))
	except Exception, e:
		print e

	return file_path


