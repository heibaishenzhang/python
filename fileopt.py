#read the whole file once time
filepath='D:/data.txt' #文件路径

with open(filepath, 'r') as f:
    print f.read()
    
#Read fixed length files
# -*- coding: UTF-8 -*-

filepath='D:/data.txt' #文件路径

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

filepath='D:/data.txt' #文件路径

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

filepath='D:/data.txt' #文件路径

with open(filepath, "r") as f:
    txt_list = f.readlines()

for i in txt_list:
    print i,
    
    
#write the files 
# -*- coding: UTF-8 -*-

filepath='D:/data1.txt' #文件路径

with open(filepath, "w") as f: #w会覆盖原来的文件，a会在文件末尾追加
    f.write('1234')
  
