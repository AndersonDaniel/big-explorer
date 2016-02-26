import http.server
import socketserver
import json
import os

CONST_WORKING_FOLDER = r'D:\daniel\working_folder'

class myHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
	def do_GET(self):
		if (self.path == '/files'):
			self.wfile.write(json.dumps(os.listdir(CONST_WORKING_FOLDER)).encode())
			#self.wfile.write(json.dumps(['אבג']).encode())
		else:
			super(myHTTPRequestHandler, self).do_GET()

def serve():
	PORT = 8000

	Handler = myHTTPRequestHandler

	httpd = socketserver.TCPServer(("", PORT), Handler)

	print("Serving at port", PORT)
	httpd.serve_forever()
	
serve()