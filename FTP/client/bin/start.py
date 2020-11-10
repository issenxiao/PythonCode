import os
import sys
from FTP.client.core import client

sys.path.append(os.path.dirname(os.getcwd()))

if __name__ == '__main__':
	client.main()
