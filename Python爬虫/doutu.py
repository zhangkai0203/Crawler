#!/usr/bin/python
# -*- coding: utf-8 -*-
import requests
import re
import time
import random

'''
 # 这是一个图片的url
url = 'http://yun.itheima.com/Upload/Images/20170614/594106ee6ace5.jpg'
response = requests.get(url)
# 获取的文本实际上是图片的二进制文本
img = response.content
# 将他拷贝到本地文件 w 写  b 二进制  wb代表写入二进制文本
with open( './a.jpg','wb' ) as f:
    f.write(img)


'''

count = 1

def get_data(i):



    result = requests.get("http://www.doutula.com/article/list/?page={}".format(i))
    html = result.text

    reg = r'data-original="(.*?)".*?alt="(.*?)"'
    reg  = re.compile(reg,re.S)

    imageList = re.findall(reg,html)

    for u in imageList:

        #time.sleep(1)

        print u[0]

        img = requests.get(u[0]).content

        #imgname =  random.randint(10000,999999)

        global count


        print count
        with open("./images/{}.jpg".format(count),'wb') as f:
            f.write(img)

        count += 1



for i in range(4,100):
    print "爬取第{}页".format(i)
    get_data(i)
