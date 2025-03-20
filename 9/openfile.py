#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 文件读取

#打开文件
import sys
import os
    
a = os.getcwd()  # 这个  是获取当前工作目录 下面的文件路径依靠这个
print(a) 

print (sys.argv[0])#获得的是当前执行脚本的位置（若在命令行执行的该命令，则为空）


#   读取文件
f = open('./helloworld/9/helloworld.py', 'r' ,encoding='utf8')
print(f.read())
print(f.readline())

while True :
    data = f.readline()
    if len(data) == 0 :
        break
    print(data)


print(f.readlines())

# 关闭文件
f.close()

# 写文件 
with open('./helloworld/9/text.txt', 'w') as a: 

    a.write('asdf\n')
    a.write('ghjkl\n')

with  open('./helloworld/9/text.txt', 'a')  as a: #add 追加
    a.write('qwert\n')
    a.write('yuiop\n')

    # a.close()  #关闭文件 可以写入
    # while  True:
    #     pass


    # a.close()  #程序未结束 无法写入


with open('/home/bupt2122/Desktop/OIP-C.png', 'rb') as img:
    print(img.read())
    add = img.read()
    with open('/home/bupt2122/Desktop/OIP-C2.png', 'wb') as img2:
        img2.write(add)
