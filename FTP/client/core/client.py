from FTP.client.core.auth_client import Auth


def main():

	global func_str
	auth_obj = None
	start_l = [('登录', 'login'), ('注册', 'register'), ('退出', 'exit')]
	for index, item in enumerate(start_l, 1):
		print(index, item[0])
	while True:
		try:
			num = int(input('>>>'))
			func_str = start_l[num-1][1]
		except TypeError or ValueError:
			print('输入信息有误')
			# 字符串数据类型的方法 login register quit
		if hasattr(Auth, func_str):
			auth_obj = Auth()
			func = getattr(auth_obj, func_str)
			ret = func()
			if ret:
				break
		elif auth_obj:
			auth_obj.sk.MySk.close()
			exit()
		else:
			exit()
