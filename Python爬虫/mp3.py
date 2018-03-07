#!/usr/bin/python
# -*- coding: utf-8 -*-
import urllib2


f = urllib2.urlopen('http://m10.music.126.net/20180305154841/c7323810f7721c8975bf9b48666c91fc/ymusic/0c33/1150/e2d3/b9b635b937dde44e5eb651e03d7358f1.mp3')
data = f.read()

with open('./MP3/带你去旅行.mp3', 'wb') as code:
    code.write(data)



