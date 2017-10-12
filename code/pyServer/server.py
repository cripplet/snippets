import SocketServer

class TCPHandler(SocketServer.StreamRequestHandler):
	def handle(self):
		self.data = self.rfile.readline().strip()
		print('client %s sent:' % (self.client_address[0]))
		print(self.data)

		# send data
		fp = open('/usr/share/sounds/alsa/Front_Center.wav', 'r')
		self.wfile.write(fp.read())
#		self.wfile.write(self.data.upper())

if __name__ == '__main__':
	host = 'localhost'
	port = 8080

	# create a server with custom handler binding
	server = SocketServer.TCPServer((host, port), TCPHandler)

	# start server
	try:
		server.serve_forever()
	except KeyboardInterrupt:
		pass
	# httpd.server_close()
