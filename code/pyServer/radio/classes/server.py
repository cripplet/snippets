from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler
import SocketServer

class Server(HTTPServer):
	def __init__(self):
		self.host = 'localhost'
		self.port = 8080

		# create a server with custom handler binding
		SocketServer.TCPServer.__init__(self, (self.host, self.port), RequestHandler)

class RequestHandler(BaseHTTPRequestHandler):
	def do_GET(self):
		self.send_response(200)
		self.send_header('Content-Type', 'audio/mpeg')
		self.end_headers()
		fp = open('stream', 'r+b')
		a = fp.read(1024)
		while(a):
			self.wfile.write(a)
			a = fp.read(1024)
		return
