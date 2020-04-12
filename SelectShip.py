import os
import shutil
import cv2

catogory = ['ship']  # 指定类别的名称


def custombasename(fullname):
    return os.path.basename(os.path.splitext(fullname)[0])


def GetFileFromThisRootDir(dir, ext=None):
    allfiles = []
    needExtFilter = (ext != None)
    for root, dirs, files in os.walk(dir):
        for filespath in files:
            filepath = os.path.join(root, filespath)
            extension = os.path.splitext(filepath)[1][1:]
            if needExtFilter and extension in ext:
                allfiles.append(filepath)
            elif not needExtFilter:
                allfiles.append(filepath)
    return allfiles


if __name__ == '__main__':
    root1 = 'D:/Code/DOTA/train'
    pic_path = os.path.join(root1, 'images')  # 样本图片路径
    label_path = os.path.join(root1, 'labelTxt')  # DOTA标签的所在路径
    label_list = GetFileFromThisRootDir(label_path)
    ship_pic = 'D:/Code/DOTA/DOTAship/images'
    ship_label = 'D:/Code/DOTA/DOTAship/labelTxt'
    for labelpath in label_list:
        n = 0
        f = open(labelpath, 'r')
        lines = f.readlines()
        splitlines = [x.strip().split(' ') for x in lines]  # 根据空格分割
        for i, splitline in enumerate(splitlines):
            if i in [0, 1]:  # DOTA数据集前两行对于我们来说是无用的
                continue
            catogory_name = splitline[8]  # 类别名称
            if catogory_name in catogory:
                n = n + 1
                if n > 2:  # 样本包含两个及以上的再挑选出来
                    name = custombasename(labelpath)  # 名称
                    oldlabelpath = labelpath
                    oldimgpath = os.path.join(pic_path, name + '.png')
                    img = cv2.imread(oldimgpath)
                    newlabelpath = os.path.join(ship_label, name + '.txt')
                    newimage_path = os.path.join(ship_pic, name + '.png')  # 如果要改变图像的后缀，就采用重写的方法
                    cv2.imwrite(newimage_path, img)
                    # shutil.copyfile(oldimgpath, newimage_path)
                    shutil.copyfile(oldlabelpath, newlabelpath)
                    break