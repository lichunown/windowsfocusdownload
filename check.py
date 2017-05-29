import os
#import numpy as np
import filecmp 
from PIL import Image

datapath = '''./focus/'''
tranpath = '''./transverse'''#heng
vertical = '''./vertical'''

files = os.listdir(datapath)

def copy(path1,path2):
    f = open(path1,'rb')
    newf = open(path2,'wb')
    data = f.read(1024*1024*8)
    while(data):
        newf.write(data)
        data = f.read(1024*1024*8)
    newf.close()
    f.close()

for imgp in files:
    try:
        img = Image.open(os.path.join(datapath,imgp))
    except Exception,e:
        print '[error] Can NOT Open file: %s \n %s' % (os.path.join(datapath,imgp),e)
        continue
    size = img.size
    if size[0] > size[1]:
        if not os.path.exists(os.path.join(tranpath,imgp)):
            copy(os.path.join(datapath,imgp),os.path.join(tranpath,imgp))
            print 'rewrite '+ imgp
    else:
        if not os.path.exists(os.path.join(vertical,imgp)):
            copy(os.path.join(datapath,imgp),os.path.join(vertical,imgp))
            print 'rewrite '+ imgp
