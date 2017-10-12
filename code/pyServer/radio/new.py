from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler
import SocketServer

from classes.server import Server, RequestHandler

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
		fp.seek(0)
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
