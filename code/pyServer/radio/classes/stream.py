class Stream():
	def __init__(self):
		from io import BytesIO
		self.wpointer = 0
		self.rpointer = 0
		self.buffer = 16
		self.size = 2 * self.buffer
		self.stream = BytesIO()
	def play(self):
		self.stream.seek(self.rpointer)
		self.rpointer += self.buffer
		if(self.rpointer >= self.size):
			self.rpointer = 0
		print(self.stream.read(self.buffer))
		# return(self.stream.read(self.buffer))
	def load(self, data):
		self.stream.seek(0)
		self.wpointer += self.buffer
		if(self.wpointer >= self.size):
			self.wpointer = 0
		self.stream.write(data)
	def run(self):
		while(True):
			self.song = open('/home/mzhang/Downloads/renmd.mp3', 'r+b')
			data = self.song.read(self.buffer)
			while(data):
				self.load(data)
				data = self.song.read(self.buffer)
			print('end of song')
			self.song.close()
	def increment(self, pointer):
		pointer += self.buffer
		if(pointer > self.size):
			pointer = 0


from threading import Thread
radio = Stream()
Thread(target = radio.run()).start()
# while(True):
#	print(radio.wpointer)
#	print(radio.rpointer)
#	radio.play()
#
#		from os import mkfifo, unlink
#		mkfifo('stream', 0777)
#		song = open('/home/mzhang/Downloads/renmd.mp3', 'rb')
