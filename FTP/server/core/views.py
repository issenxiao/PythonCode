import os
import pickle
from FTP.server.core.user import User
from FTP.server.conf import settings


def login(msg):
	# 登录 用户名 密码
	# 获取到pickle_path
	print('当前登录的用户views_login:')
	print(msg)
	return True
	# return True,pickle_path


def register(msg):
	# username,password
	# 创建一个属于这个用户的家目录，并记录下来
	# 把用户名密码写进userinfo文件里，记录用户名
	# 记录用户的初始磁盘配额（可配置）
	# 记录文件大小
	# 记录用户当前所在的目录 
	user_obj = User(msg['username'])  # 记录用户信息在内存里
	pickle_path = os.path.join(settings.pickle_path, msg['username'])
	print('views_register:')
	print(pickle_path)
	with open(pickle_path, 'wb') as f1:
		pickle.dump(user_obj, f1)
	try:
		os.mkdir(user_obj.home)  # 创建一个属于这个用户的家目录
	except FileExistsError:
		print('文件已存在，无法创建')
	with open(settings.user_info, 'a') as f2:
		f2.write('%s|%s|%s' % (msg['username'], msg['password'], pickle_path))
	print('用户注册成功views_register')
	print(msg)
	return True


def upload(msg, request):
	# 如果这个过程 涉及到上传下载，sk
	print(msg)


def download(msg):
	print(msg)
