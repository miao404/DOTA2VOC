# -*- coding: utf-8 -*-
import cv2
import os
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
category_set = ['ship']

def tqtxt(path,path_txt,path_out,size_h=1000,size_w=1000):
    ims_list=os.listdir(path)
    # print(ims_list)
    for im_list in ims_list:
        # name_list = []
        name = im_list[:-4]
        name_list = name.split('_')
        # print(name_list)
        # print(len(name_list))
        if len(name_list)<2:
            continue
        h = int(name_list[1])
        w = int(name_list[2])
        txtpath = path_txt + name_list[0] + '.txt'
        txt_outpath = path_out + name + '.txt'
        f = open(txt_outpath,'a')
        with open(txtpath, 'r') as f_in:   #打开txt文件
             i = 0
             lines = f_in.readlines()
             #print(len(lines))
             #splitlines = [x.strip().split(' ') for x in lines]  #根据空格分割
             for line  in lines:
                 if i in [0,1]:
                     f.write(line)#txt前两行直接复制过去
                     i = i+1
                     continue
                 splitline = line.split(' ')
                 label = splitline[8]
                 kunnan = splitline[9]
                 if label not in category_set:#只书写指定的类别
                     continue
                 x1 = int(float(splitline[0]))
                 y1 = int(float(splitline[1]))
                 x2 = int(float(splitline[2]))
                 y2 = int(float(splitline[3]))
                 x3 = int(float(splitline[4]))
                 y3 = int(float(splitline[5]))
                 x4 = int(float(splitline[6]))
                 y4 = int(float(splitline[7]))
                 if w<=x1<=w+size_w and w<=x2<=w+size_w and w<=x3<=w+size_w and w<=x4<=w+size_w and h<=y1<=h+size_h and h<=y2<=h+size_h and h<=y3<=h+size_h and h<=y4<=h+size_h:
                     f.write('{} {} {} {} {} {} {} {} {} {}'.format(float(x1-w),float(y1-h),float(x2-w),float(y2-h),float(x3-w),float(y3-h),float(x4-w),float(y4-h),label,kunnan))
        f.close()

if __name__ == '__main__':
    ims_path='D:/Code/DOTA/DOTAship/imageSplit/'# 图像数据集的路径
    txt_path = 'D:/Code/DOTA/DOTAship/labelTxt/'#原数据集标签文件
    path = 'D:/Code/DOTA/DOTAship/labelTxtSplit/'#切割后数据集的标签文件存放路径
    tqtxt(ims_path,txt_path,path,size_h=1000,size_w=1000)