import os

#建立测试集的索引文件
dir = 'D:/Code/DOTA_test/testXML'
lis = os.listdir(dir)
for i in range(0,len(lis)):
	(shotname,ext) = os.path.splitext(lis[i])
	f=open('D:/Code/DOTA_test/test.txt','r+')
	f.read()
	f.write(shotname+'\n')
	f.close()