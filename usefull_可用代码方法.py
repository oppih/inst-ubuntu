可用代码方法：
获得Ubuntu版本号：
def ubuntuVersion():
	"获得Ubuntu版本号"
	f = open("/etc/issue.net", "r")
	version = f.read()
	f.close()
	if '9.04' in version:
		return "9.04"
	else:
		notify('BUG!',"本程序还不支持此版本的Ubuntu，请联系作者 homer.xing@gmail.com 让他加上支持。抱歉,给您填麻烦了。")
		sys.exit(0)

为保证sudo的权限在默认事务分钟后不失效，使用命令“sudo -v”另延长15分钟

编写一个专门用于安装的函数，挺好的


其他的也建立符号链接吧
def removeUnnecessaryDirectories():
	"建立‘桌面’文件夹的英文符号链接，删除不必要的空目录"
	os.system("ln -s ~/桌面 ~/Desktop")
	os.system("rmdir ~/公共的 2>/dev/null")
	os.system("rmdir ~/模板 2>/dev/null")
	os.system("rmdir ~/视频 2>/dev/null")
	os.system("rmdir ~/图片 2>/dev/null")
	os.system("rmdir ~/文档 2>/dev/null")
	os.system("rmdir ~/音乐 2>/dev/null")
	os.system("rm ~/Examples -rf 2>/dev/null") #Examples链接因为工作时无用，也删除
	os.system("rm ~/examples.desktop -f 2>/dev/null") #9.04的Examples链接删除
	#把目录名改成英文
	fn = os.path.expanduser('~/.config/user-dirs.dirs')
	with open(fn,'w') as f:
		f.write("""XDG_DESKTOP_DIR="$HOME/Desktop/"
XDG_DOWNLOAD_DIR="$HOME/"
XDG_TEMPLATES_DIR="$HOME/"
XDG_PUBLICSHARE_DIR="$HOME/"
XDG_DOCUMENTS_DIR="$HOME/"
XDG_MUSIC_DIR="$HOME/"
XDG_PICTURES_DIR="$HOME/"
XDG_VIDEOS_DIR="$HOME/"
""")
	D.execute("xdg-user-dirs-gtk-update &")
