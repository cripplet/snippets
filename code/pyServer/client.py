import socket, sys

# match server settings
host = 'localhost'
port = 8080

# data from command line
data = ' '.join(sys.argv[1:])

# create a socket, with SOCK_STREAM referring to a TCP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def buffer(sock):
	buffer = sock.recv(1024)
	while(True):
		tmp = sock.recv(1024)
		if(not(tmp)):
			break
		buffer += tmp
	return(buffer)

try:
	sock.connect((host, port))
	sock.sendall(data + '\n')

	received = buffer(sock)
finally:
	sock.close()

print('Sent:     %s' % (data))
print('Received: %s' % (received))
