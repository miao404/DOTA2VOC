import os

#建立train.txt 索引文件
dir = 'D:/Code/DOTA_test/trainXML'
lis = os.listdir(dir)
for i in range(0,len(lis)):
	(shotname,ext) = os.path.splitext(lis[i])
	f=open('D:/Code/DOTA_test/train.txt','r+')
	f.read()
	f.write(shotname+'\n')
	f.close()