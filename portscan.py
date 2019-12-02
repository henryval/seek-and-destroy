#Third party imports
import nmap

#Python imports

#Local imports
import utils

default_ports = '440-443'

def nmap_scan(site, ports=default_ports):
	nm = nmap.PortScanner()
	host = utils.is_alive(site)
	result = {}
	if host:
		nm.scan(host, ports)
		for proto in nm[host].all_protocols():
			for port in nm[host][proto].keys():
				if nm[host][proto][port]['state'] == "open":
					product = nm[host][proto][port]['product']
					version = nm[host][proto][port]['version']
					result[port] = str(product + " " + version)
				elif nm[host][proto][port]['state'] == "filtered":
					result[port] = "filtered"
				else:
					result[port] = "closed"
	else:
		print("[!] Host {} is down!".format(site))
	return result

print(nmap_scan("scanme.nmap.org", '0-500'))

