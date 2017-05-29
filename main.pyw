import os
savepath = '''./focus/'''
datapath = '''C:\Users\lichunyang\AppData\Local\Packages\Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy\LocalState\Assets'''
files = os.listdir(datapath)
for filename in files:
    if os.path.getsize(os.path.join(datapath,filename))<1024*100:
        continue
    fil = open(os.path.join(datapath,filename),'rb')
    savefile = open(os.path.join(savepath,filename+'.jpg'),'wb')
    data = fil.read(1024*1024)
    while(data):
        savefile.write(data)
        data = fil.read(1024 * 1024)
    savefile.close()
    fil.close()