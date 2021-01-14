# DOTA数据集处理 #


选取需要类别 → 图片裁剪 → 标签数据自动抓取 → 格式转换txt2xml → 修改图片和标签文件名称 → 生成各类数据集索引文件

**1. SelectShip.py**
  
从有15种类别的DOTA数据集中筛选出需要的类别

`catogory = ['ship']  # 指定类别的名称`

**2.ImgSplit.py**
  
数据集影像切割为1000*1000

不足1000的高或宽在在下或右方向补齐（左上角不动，因为标签数据原点为左上角）

**3.txtGrab.py**
  
标签数据自动抓取

第14行 `name = im_list[:-4]`

如果图像后缀为.png .jpg等则为-4，若图像后缀为.tiff则为-5

**4.txt2xml.py**

数据格式转换 / 两种矩形框的xml可选

hbb(水平矩形框)：xmin ymin xmax ymax

obb(旋转矩形框)：x0 y0 x1 y1 x2 y2 x3 y3 

根据需要选择（如果生成obb,修改260行和266行的hbb=True为False）

**5.Rename.py**

批量修改文件夹中文件名为（000000）格式，方便直接替换VOC数据集进行训练

**6.ImageSets.py**

制作ImageSets文件夹下Main文件夹中的4个文件（test.txt、train.txt、trainval.txt、val.txt）

test.txt 测试集 **/** 
train.txt 训练集 **/** 
val.txt 验证集 **/** 
trainval.txt：训练和验证集

在原始VOC2007数据集中，trainval大约占整个数据集的50%，test大约为整个数据集的50%；train大约是trainval的50%，val大约为trainval的50%，按照此标准生成txt文件

  
