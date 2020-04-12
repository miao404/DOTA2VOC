# -*- coding: utf-8 -*-
import cv2
import os
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt


def tianchong_you(img):
    size = img.shape
    #if size[0]>=1000 and size[1]<1000:
    constant = cv2.copyMakeBorder(img,0,0,0,1000-size[1],cv2.BORDER_CONSTANT,value=(107,113,115))#填充值为数据集均值
    #else:
     #    print('图像不符合要求')
      #   return 0
    return constant

def tianchong_xia(img):
    size = img.shape
   # if size[0]<1000 and size[1]>=1000:
    constant = cv2.copyMakeBorder(img,0,1000-size[0],0,0,cv2.BORDER_CONSTANT,value=(107,113,115))
    #else:
     #    print('图像不符合要求')
      #   return 0
    return constant

def tianchong_xy(img):
    size = img.shape
    #if size[0]<1000 and size[1]<1000:
    constant = cv2.copyMakeBorder(img,0,1000-size[0],0,1000-size[1],cv2.BORDER_CONSTANT,value=(107,113,115))
   #else:
   #      print('图像不符合要求')
   #      return 0
    return constant

def caijian(path,path_out,size_w=1000,size_h=1000,step=800):#重叠度为200
    ims_list=os.listdir(path)
    #print(ims_list)
    count = 0
    for im_list in ims_list:
        number = 0
        name = im_list[:-4]#去处“.png后缀”
        print(name)
        img = cv2.imread(ims_path+im_list)
        size = img.shape
        if size[0]>=1000 and size[1]>=1000:
           count = count + 1
           for h in range(0,size[0]-1,step):
               star_h = h
               for w in range(0,size[1]-1,step):
                   star_w = w
                   end_h = star_h + size_h
                   if end_h > size[0]:
                      star_h = size[0] - size_h
                      end_h = star_h + size_h
                   end_w = star_w + size_w
                   if end_w > size[1]:
                      star_w = size[1] - size_w
                   end_w = star_w + size_w
                   cropped = img[star_h:end_h, star_w:end_w]
                   name_img = name + '_'+ str(star_h) +'_' + str(star_w)#用起始坐标来命名切割得到的图像，为的是方便后续标签数据抓取
                   cv2.imwrite('{}/{}.png'.format(path_out,name_img),cropped)
                   number = number + 1
        if size[0]>=1000 and size[1]<1000:
            print('图片{}需要在右面补齐'.format(name))
            count = count + 1
            img0 = tianchong_you(img)
            for h in range(0,size[0]-1,step):
               star_h = h
               star_w = 0
               end_h = star_h + size_h
               if end_h > size[0]:
                  star_h = size[0] - size_h
                  end_h = star_h + size_h
               end_w = star_w + size_w
               cropped = img0[star_h:end_h, star_w:end_w]
               name_img = name + '_'+ str(star_h) +'_' + str(star_w)
               cv2.imwrite('{}/{}.png'.format(path_out,name_img),cropped)
               number = number + 1
        if size[0]<1000 and size[1]>=1000:
            count = count + 1
            print('图片{}需要在下面补齐'.format(name))
            img0 = tianchong_xia(img)
            for w in range(0,size[1]-1,step):
               star_h = 0
               star_w = w
               end_w = star_w + size_w
               if end_w > size[1]:
                  star_w = size[1] - size_w
                  end_w = star_w + size_w
               end_h = star_h + size_h
               cropped = img0[star_h:end_h, star_w:end_w]
               name_img = name + '_'+ str(star_h) +'_' + str(star_w)
               cv2.imwrite('{}/{}.png'.format(path_out,name_img),cropped)
               number = number + 1
        if size[0]<1000 and size[1]<1000:
            count = count + 1
            print('图片{}需要在下面和右面补齐'.format(name))
            img0 = tianchong_xy(img)
            cropped = img0[0:1000, 0:1000]
            name_img = name + '_'+ '0' +'_' + '0'
            cv2.imwrite('{}/{}.png'.format(path_out,name_img),cropped)
            number = number + 1
        print('图片{}切割成{}张'.format(name,number))
        print('共完成{}张图片'.format(count))

if __name__ == '__main__':
    ims_path='D:/Code/DOTA/DOTAship/images/'# 图像数据集的路径
   # txt_path = '/home/***/data/VOCdevkit/mydataset/Annotations/txt/'
    path = 'D:/Code/DOTA/DOTAship/imageSplit/' #切割得到的数据集存放路径
    caijian(ims_path,path,size_w=1000,size_h=1000,step=800)