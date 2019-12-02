#Python imports
import socket

def is_alive(site):
	"""
	Function check if site has a public IP address
	A.K.A.: Public DNS resolution
	-- Example --
	print(check_if_alive("www.grupobancolombia.com"))
	print(check_if_alive("bancol.corp"))
	"""
	try:
		is_alive = socket.gethostbyname(site)
	except:
		is_alive = False
	return is_alive
