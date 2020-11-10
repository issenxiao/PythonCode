import json
import socket
from FTP.client.conf import settings


class MySocketClient:
	def __init__(self):
		self.MySk = socket.socket()
		self.MySk.connect(settings.addr)

	def mysend(self, msg):
		ret_json = json.dumps(msg)
		self.MySk.send(ret_json.encode(settings.code))
