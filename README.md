# 自动下载WindowsFocus图片

## 原理

其实原理很简单，就是Windows的focus图片缓存在了`C:\Users\%USERPROFILE%\AppData\Local\Packages\Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy\LocalState\Assets`目录下，这个脚本只是把缓存目录的文件找出来，加一个`.jpg`的后缀名。

嗯，用bat写了个运行的脚本，vbe保证不弹窗运行。本地电脑我是自己建了个计划任务，每天定时执行一遍。到目前为止，我这里已经有157个横屏图片和144个竖屏图片了。

### 有啥用

**看着好看，做屏保不行？**
## 其他人
目录里的那个是我个人用的，至于通用性的脚本，请访问[通用型脚本](toAllUser/main.pyw)。
嗯，我好像打包了一个exe，不知道效果如何[打包exe](toAllUser/dist/main.exe)