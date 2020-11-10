import os
import sys
import socketserver
from FTP.server.core.server import MyFTPServer
from FTP.server.conf import settings
sys.path.append(os.path.dirname(os.getcwd()))

if __name__ == '__main__':
	print('*'*10+'服务端启动'+'*'*10)
	server = socketserver.ThreadingTCPServer(settings.addr, MyFTPServer)
	server.serve_forever()

