from FTP.client.core.socket_client import MySocketClient


class Auth:
	__instance = None

	def __new__(cls, *args, **kwargs):
		# 单例模式，防止重复创建链接
		if not cls.__instance:
			obj = object.__new__(cls)
			cls.__instance = obj
		return cls.__instance

	def __init__(self):
		self.sk = MySocketClient()
		self.username = None
		
	def login(self):
		username = input('username:')
		password = input('password')
		if username.strip() and password.strip():
			# send
			self.sk.mysend({'username':username, 'password': password,
			                'operation':'login'})
		ret = self.sk.MySk.recv(1024)  # 登录结果
		print('登录成功')

	def register(self):
		username = input('username:')
		password1 = input('password')
		password2 = input('password_ensure:')
		if username.strip() and password1.strip() and password1 == password2:
			self.sk.mysend({'username':username, 'password':password1,
			                'operation':'register'})
		ret = self.sk.MySk.recv(1024)  # 注册结果
		print(ret)
