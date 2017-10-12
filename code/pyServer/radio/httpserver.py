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
#		fp = open('/home/mzhang/Downloads/renmd.mp3', 'rb')
#		self.wfile.write(fp.read())
#		fp.close()
		return

def run():
	from os import mkfifo, unlink
	# start server
	try:
		Server().serve_forever()
	except KeyboardInterrupt:
#		fp.close()
		unlink('stream')
	# httpd.server_close()	

def pipe():
	from os import mkfifo, unlink
	mkfifo('stream', 0777)
	song = open('/home/mzhang/Downloads/renmd.mp3', 'rb')

	fp = open('stream', 'rwb+')
	a = song.read(1024)
	while(a):
		fp.write(a)
		fp.flush()
#		fp.seek(0)
		a = song.read(1024)


if __name__ == '__main__':

	from threading import Thread

	r = Thread(target = run)
	t = Thread(target = pipe)
	r.start()
	t.start()

#	from os import mkfifo, unlink

#	mkfifo('stream', 0777)
#	song = open('/home/mzhang/Downloads/renmd.mp3', 'rb')
#
#	fp = open('stream', 'rwb+')
#	a = song.read()
#	song.close()
#
#	fp.write(a)
#	fp.flush()
#
	# start server
#	try:
#		Server().serve_forever()
#	except KeyboardInterrupt:
#		fp.close()
#		unlink('stream')
	# httpd.server_close()
