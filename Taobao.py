#!/usr/bin/env python
# -*- encoding:utf-8 -*-
# author :insun
#http://yxmhero1989.blog.163.com/blog/static/112157956201311994027168/
import urllib, urllib2, re, sys, os

import tkinter as tk
from tkinter import ttk
from Tkinter import *
reload(sys)

lpath = '图片'
lpath = unicode(lpath,"utf-8")

if(os.path.exists(lpath) == False):
    os.mkdir(lpath)

def get_huaban_beauty(pid):
    if pid is None or pid == '':
        print 'none id'
        return
    board_id = pid
    print board_id

    if(os.path.exists(lpath+'/'+board_id) == False):
        os.mkdir(lpath+'/'+board_id)
    maxid = ''
    limit = 20 #他默认允许的limit为100
    while board_id != None:
        # url = 'http://huaban.com/boards/31435061/?max=' + str(pin_id) + '&limit=' + str(limit) + '&wfl=1'
        url = 'https://detail.tmall.com/item.htm?id='+board_id
        try:
            i_headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36",
                         "Connection":"keep-alive"
                         }
            req = urllib2.Request(url, headers=i_headers)
            html = urllib2.urlopen(req).read()
            # print html
            # reg = re.compile('"pin_id":(.*?),.+?"file":{"farm":"farm1", "bucket":"hbimg",.+?"key":"(.*?)",.+?"type":"image/(.*?)"', re.S)
            # (?<=<a href="#"><img src=")//(.*?)(?=_\d)|
            reg = re.compile('(?<=<a href="#"><img src=")//(.*?)(?=_\d)', re.S)
            groups = re.findall(reg, html)
            if(len(groups) == 0):
                reg = re.compile('(?<=<a href="#"><img data-src=")//(.*?)(?=_\d)', re.S)
                groups = re.findall(reg, html)
            print(len(groups))
            if len(groups) <= 0:
                print('图片下载完毕！')#图片下载完毕
                return
            # for att in groups:
            for index in range(len(groups)):
                img_url = 'http://' + groups[index]
                if(urllib.urlretrieve(img_url, lpath+'/'+board_id+'/'+str(index)+'.jpg')):
                    print img_url + ' download success!'
                else:
                    print img_url + '.jpg save failed'
                if(index == 4):
                    return
            # if toEnd is True:
            #     toEnd = False
            #     return
            # return
        except:
            print 'error occurs'

######################################GUI界面开始
win = tk.Tk()
win.title("淘宝主图下载")    # 添加标题
# frame = Frame(win, width=200,height = 500)
#
# frame.pack()
# frame.pack_propagate(0) # 使组件大小不变，此时width才起作用
frame = LabelFrame(win, text="输入宝贝地址", width=2000, fg='darkgray') # 信息区
frame.pack()
frame.grid(row=1,column=0, sticky=N+S, padx=100, pady=100)

frame.propagate(0) # 使组件大小不变，此时width才起作用

def clickMe():   # 当acction被点击时,该函数则生效
    reg = re.compile('(?<=id=)\d+', re.S)
    # 编码中文字符
    pathstr = name.get().encode("utf-8")
    board_id = re.findall(reg,pathstr)[0]
    action.configure(text=board_id+ ' 下载完成 ' )# name.get()+  设置button显示的内容
    print(board_id)
    get_huaban_beauty(board_id)

action = ttk.Button(frame, text="点击下载", command=clickMe)     # 创建一个按钮, text：显示按钮上面显示的文字, command：当这个按钮被点击之后会调用command函数
action.grid(column=1, row=1)

ttk.Label(frame, text="点击下载后等待下载完成").grid(column=0, row=0)

name = tk.StringVar()     # StringVar是Tk库内部定义的字符串变量类型，在这里用于管理部件上面的字符；不过一般用在按钮button上。改变StringVar，按钮上的文字也随之改变。
nameEntered = ttk.Entry(frame, width=50, textvariable=name)   # 创建一个文本框，定义长度为12个字符长度，并且将文本框中的内容绑定到上一句定义的name变量上，方便clickMe调用
nameEntered.grid(column=0, row=1)

win.mainloop()      # 当调用mainloop()时,窗口才会显示出来

# mainRun()

