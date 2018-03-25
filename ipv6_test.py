import socket

#script to check ipv6 connectivity
def ipv6_check(server, port):
	s = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
	try:
		s.connect((str(server), int(port)))
		print('IPv6 socket created to server %s on port %s' % (server,port))
	except:
		print('Server %s doesnt appear to support IPv6. Unable to create socket' % server)

def main():
	print("This script will check IPv6 connectivity")
	server = raw_input("Please enter server: ")
	port = raw_input("Please enter port number: ")
	ipv6_check(server, port)

if __name__ == '__main__':
	main()


