import os
import winshell 

def create_shortcut_to_startup(): 
    title = u'StartUp'
    s = os.path.basename(__file__) 
    fname = os.path.splitext(s)[0] 
    winshell.CreateShortcut( 
        Path = os.path.join(winshell.startup(), os.path.basename(__file__) + '.lnk'), 
        Target = __file__ , 
        Icon = (__file__ , 0), 
        Description = title
    )
create_shortcut_to_startup()

savepath = '''./WindowsFocus/'''
datapath = os.path.join(os.path.expandvars('''%USERPROFILE%'''),
    '''AppData/Local/Packages/Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy/LocalState/Assets''')
files = os.listdir(datapath)
if not os.path.exists('./WindowsFocus'):
    os.mkdir('WindowsFocus')
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