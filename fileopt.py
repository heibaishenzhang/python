#read the whole file once time
filepath='D:/data.txt' #�ļ�·��

with open(filepath, 'r') as f:
    print f.read()
    
#Read fixed length files
# -*- coding: UTF-8 -*-

filepath='D:/data.txt' #�ļ�·��

f = open(filepath, 'r')
content=""
try:
    while True:
        chunk = f.read(8)
        if not chunk:
            break
        content+=chunk
finally:
    f.close()
    print content
    
    
#read file a line once time    
# -*- coding: UTF-8 -*-

filepath='D:/data.txt' #�ļ�·��

f = open(filepath, "r")
content=""
try:
    while True:
        line = f.readline()
        if not line:
            break
        content+=line
finally:
    f.close()
    print content
    
    
#Read the whole lines
# -*- coding: UTF-8 -*-

filepath='D:/data.txt' #�ļ�·��

with open(filepath, "r") as f:
    txt_list = f.readlines()

for i in txt_list:
    print i,
    
    
#write the files 
# -*- coding: UTF-8 -*-

filepath='D:/data1.txt' #�ļ�·��

with open(filepath, "w") as f: #w�Ḳ��ԭ�����ļ���a�����ļ�ĩβ׷��
    f.write('1234')
  
