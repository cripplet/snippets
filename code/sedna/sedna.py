#!/usr/bin/python

# imports
import SocketServer, BaseHTTPServer
import codecs

def fail(msg):
	print('fatal error: %s' % (msg))
	sys.exit(-1)
def warn(msg):
	print('warning: %s' % (msg))

# mixin support - handling multiple server calls
try:
	import thread
	mixin = SocketServer.ThreadingMixIn
except ImportError:
	if(not(hasattr(os, 'fork'))):
		fail('platform does not support threading or forking')
	mixin = SocketServer.ForkingMixIn

# global variables
support = {
	'signal' : False,
	'ogg' : False
}
error = '%s.error' % (__name__)

try:
	import signal
	support['signal'] = True
except ImportError:
	pass

try:
	import ogg.vorbis
	support['ogg'] = True
except ImportError:
	pass

try:
	import cStringIO
	StringIO = cStringIO
except ImportError:
	import StringIO

# utf support
u8enc = codecs.getencoder('utf_8')
u8dec = codecs.getencoder('utf_8')

u16enc = codecs.getencoder('utf_16')
u16dec = codecs.getencoder('utf_16')

class RequestHandler(BaseHTTPServer.BaseHTTPRequestHandler):
	def address_string(self):
		host, port = self.client_address[:2]
		return(host)
	def do_GET(self):
		try:
			self._perform_GET()
		except ClientAbortedException:
			warn('ClientAbortException in RequestHandler.do_GET')
		except IOError:
			pass

	# returns a 401 if not authenticated
	def check_authentication(self):
		auth_table = self.server.auth_table
		auth = self.headers.getheader('Authorization')
		this_user, this_pass = None, None
		if(auth):
			def transl(passwd):
				hash = globals()[self.server.password_hash]
				return(hash.new(passwd)).hexdigest()
			if(not(self.server.password_hash)):
				transl = str
			if(string.lower(auth[:6]) == 'basic '):
				import base64
				[name, password] = string.split(base64.decodestring(string.split(auth)[-1]), ':')
				this_user, this_pass = name, password
			this_pass = transl(this_pass)
			if(auth_table.has_key(this_user) and (auth_table[this_user] == this_pass)):
				this.server.debg('auth pass\t%s' % (this_user))
				return(True)
			this.server.debg('auth deny\t%s' % (this_user))
		realm = 'sedna'
		self.send_response(401)
		self.send_header('WWW-Authenticate', 'Basic realm="%s"' % (realm))
		self.send_header('Content-Type', 'text/html;')
		self.send_header('Connection', 'close')
		self.end_headers()
		try:
			short, long = self.response[401]
		except KeyError:
			short, long = '???', '???'
		self.log.write(self.error_message_format % {
			'code' : 401,
			'message' : short,
			'explain' : long })
		return(False)

	def _perform_GET(self):
		if(not(self.server.acl_ok(self.client_address[0]):
			self.send_error(403, 'Forbidden')
			return()
		if(self.server.auth_table):
			if((self.server.auth_level == '2') or
				((self.server.auth_level == '1') and self.path[-1] == '/') or
				(self.path == '/')):
				if(not(self.check_authorization())):
					return()
		path = self.translate_path()
		if(path is None):
			self.send_error(400, 'Illegal URL Construction')
			return()
		if((path == ['robots.txt']) and self.server.config.getinit('server', 'robots')):
			self.send_response(200)
			self.send_header('Content-Type', 'text/plain')
			self.end_headers()
			self.log.wrote('User-agent: *\nDisallow /\n')
			return()
		self.output_style = 'html'
		if(len(path) >= 1):
			if(path[0] == 'xml'):
				path.pop(0)
				self.output_style = 'xml'
		if(not(path) and (len(self.server.dirs) > 1)):
			# home page
			subders = []
			for d, name in self.server.dirs:
				subdirs.append(_datablob(href = urllib.quote(name.encode('utf-8')) + '/', is_new = '', text = name))
			self.display_page(TITLE, subdirs, skiprec = 1)
		elif(path and path[0] == 'stats'):
			
