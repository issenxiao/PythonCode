import json
import socketserver
import os

from FTP.server.conf import settings
from FTP.server.core import views


class MyFTPServer(socketserver.BaseRequestHandler):

	logined_lst = {}

	def handle(self):
		print('-' * 20)
		global pickle_path, ret
		msg = self.my_recv()  # 调用派生方法
		print('已经登录的用户logined_lst')   # 记录已经登录的用户
		print(MyFTPServer.logined_lst)
		# 消息的转发 把任务转发给views文件中的对应的方法
		# 反射
		op_str = msg['operation']  # 获取操作 auth_client
		if msg['operation'] == 'login' or msg['operation'] == 'register':
			if hasattr(views, op_str):
				func = getattr(views, op_str)
				ret = func(msg)
			if ret:
				# 用户的pickle信息所在的文件地址 views
				MyFTPServer.logined_lst[self.client_address] = os.path.join(settings.pickle_path, msg['username'])
				self.my_send(ret)
		elif hasattr(views, op_str) and self.client_address in MyFTPServer.logined_lst:
			func = getattr(views, op_str)
			ret = func(msg, self.request)
			self.my_send(ret)
		else:
			self.my_send(False)

	# {'username','password','operation'}
	# msg
	# 登录 注册
	# 查看目录

	# 上传文件
	# 反射
	# 'login'
	def my_recv(self):  # 派生方法
		msg = self.request.recv(1024)
		msg = msg.decode(settings.code)
		# print('my_recv:\n'+msg, type(msg))
		msg = json.loads(msg)
		return msg

	def my_send(self, msg):
		msg = json.dumps(msg).encode(settings.code)
		self.request.send(msg)
