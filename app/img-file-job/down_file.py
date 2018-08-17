# -*- coding: utf-8 -*-
import os
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

def get_html_content(url):
    html_content=''

    try:
        request = requests.get(url, headers=request_header)
        request.encoding = 'utf-8'
        html_content = request.text
    except Exception,e:
        print e


    return html_content

def download_img_file(img_url,file_path):
    try:
        # img_url="https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1510731843&di=dc1a96450da333fff562d80297cda7bd&imgtype=jpg&er=1&src=http%3A%2F%2Ff.hiphotos.baidu.com%2Fbaike%2Fw%253D268%253Bg%253D0%2Fsign%3D379b33558bd4b31cf03c93bdbfed4042%2F2cf5e0fe9925bc312116298e5edf8db1cb137058.jpg"
        #img_url="http://p.vxotu.com/u/20171107/09214533.jpg"
        request = requests.get(img_url, headers=request_header)
        img_content = request.content
        fp = open(file_path, 'wb')
        fp.write(img_content)
        print img_content
        fp.close()
    except Exception, e:
        print e

    return file_path

def createDir(dir):
    if not os._exists(dir):
        os.mkdir(dir)

def catch_img_urls_weimeixiezhen(url):
    img_urls = []

    #获取html内容
    html_content=get_html_content(url)
    if html_content=='':
        return False

    #解析html内容
    bs_obj=BeautifulSoup(html_content,"html.parser")
    a_objs=bs_obj.select('.tpc_content img ')
    print len(a_objs)
    for a_obj in a_objs:
        img_urls.append(a_obj.get('src'))
        print a_obj.get('src')

    return img_urls

def catch_img_topic_weimeixiezhen(url):
    img_urls = []

    #获取html内容
    html_content=get_html_content(url)
    if html_content=='':
        return False

    #解析html内容
    bs_obj=BeautifulSoup(html_content,"html.parser")
    topic_item_trs=bs_obj.select('tr.tr3.t_one')
    print len(topic_item_trs)
    for topic_item_tr in topic_item_trs:
        #获取单列
        topic_item_tds=topic_item_tr.children
        for child in topic_item_tds:
            print child
        # print topic_item_tds[0]
        # topic_item_url= topic_item_tds[0].contents[0].get('href')
        # topic_item_title_content=topic_item_tds[1].select('a')[0].string
        # topic_item_publish_time = topic_item_tds[4].select('a')[0].string
        # #解析title_content
        # print topic_item_url
        # print topic_item_title_content
        # print topic_item_publish_time

    return img_urls

class ImageSpider:
    """
            图片蜘蛛
            """

    # Const
    CONST_CAR_DATA_FILE_PATH = "data/Car.xml"
    CONST_DEFAULT_TIME_FOMAT = "%Y-%m-%d %H:%M:%S"

    def __init__(self):
        self.__file_root_path='E:/pythoncode/static/File/'
        pass

    def catch_img_urls_weimeixiezhen(self):
        url = 'http://1024.c2048ao.pw/pw/htm_data/14/1711/856566.html'
        img_urls= catch_img_urls_weimeixiezhen(url)
        return img_urls

    def catch_img(self,catalog,title,img_urls):
        #获取图片地址
        img_urls= self.catch_img_urls_weimeixiezhen()

        #创建目录
        createDir(self.__file_root_path+str(catalog))
        createDir(self.__file_root_path+str(catalog)+'/' +str(title))

        #下载图片
        index=1
        for img_url in img_urls:
            #确定扩展名
            # "D:/name.txt"
            extension='jpg'
            dir=self.__file_root_path+str(catalog)+'/' +str(title)+'/'
            file_path=dir+ str(index) + '.'+extension
            download_img_file(img_url,file_path)
            index+=1