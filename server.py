import http.server
import socketserver
import json
import os
import urllib.parse

CONST_WORKING_FOLDER = r'D:\daniel\working_folder'

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
		else:
			super(myHTTPRequestHandler, self).do_POST()

def serve():
	PORT = 8000

	Handler = myHTTPRequestHandler

	httpd = socketserver.TCPServer(("", PORT), Handler)

	print("Serving at port", PORT)
	httpd.serve_forever()
	
serve()