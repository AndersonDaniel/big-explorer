import http.server
import socketserver
import json
import os
import urllib.parse
import datetime
import threading
import time

CONST_WORKING_FOLDER = r'C:\daniel\working_folder'

alive = datetime.datetime.now()
working = True

class myHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
	def do_GET(self):
		if (self.path == '/files'):
			data = [{'name': file.split('.')[0], 'type': file.split('.')[1]} for file in os.listdir(CONST_WORKING_FOLDER) if file != 'exec.bat']
			self.wfile.write(json.dumps(data).encode())
		else:
			super(myHTTPRequestHandler, self).do_GET()
			
	def do_POST(self):
		if (self.path.startswith('/open/')):
			file = urllib.parse.unquote(self.path.replace('/open/', ''))
			os.system('start "ook" "' + CONST_WORKING_FOLDER + '\\' + file + '"')
			self.wfile.write('ok'.encode())
		elif (self.path.startswith('/create/')):
			file = urllib.parse.unquote(self.path.replace('/create/', ''))
			f = open(CONST_WORKING_FOLDER + '\\' + file, 'w')
			f.close()
			self.wfile.write('ok'.encode())
		elif (self.path.startswith('/alive')):
			global alive
			alive = datetime.datetime.now()
			print('alive')
			self.wfile.write('ok'.encode())
		else:
			super(myHTTPRequestHandler, self).do_POST()

def check_alive():
	global working
	global alive
	while working:
		time.sleep(30)
		if ((datetime.datetime.now() - alive).seconds >= 29):
			os.system('start chrome http://localhost:8000/index.html')
			
def serve():
	PORT = 8000

	Handler = myHTTPRequestHandler

	httpd = socketserver.TCPServer(("", PORT), Handler)

	t = threading.Thread(target=check_alive)
	t.start()
	
	print("Serving at port", PORT)
	try:
		httpd.serve_forever()
	except:
		global working
		working = False

if (__name__ == "__main__"):
	serve()