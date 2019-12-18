#Third party imports
import nmap

#Python imports
import random

#Local imports
import utils
import sites

top_ports_tcp = '21-25,53,80,88,110-143,389,443,445,995,993,1723,3306,3389,5900,8080'
top_ports_udp = '53,67-69,88,161,162,3389,5353'

def nmap_scan(site : str, ports=top_ports_tcp, arguments='-sV -T4'):
	"""
	Simple nmap scan to check on common ports
	No special flags, no scripts, no udp
	-- Example --
	print(nmap_scan("scanme.nmap.org")
	{22: 'OpenSSH 6.6.1p1 Ubuntu 2ubuntu2.13', 25: ' ', 80: 'Apache httpd 2.4.7'}
	"""
	nm = nmap.PortScanner()
	host = utils.is_alive(site)
	result = {}
	if host:
		nm.scan(host, ports, arguments=arguments)
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
		print("\n[!] Host {} is down!".format(site))
	return result

def nmap_long_scan(site : str):
	"""
	Long nmap scan to check on all ports
	Noisy, no scripts, no udp
	"""
	long_args = '-Pn -p- --max-retries=1 --min-rate=1000 -A'
	return nmap_scan(site, ports='', arguments=long_args)

def nmap_agressive(site : str):
	"""
	Long agressive nmap scan to check on all ports
	Pretty noisy, run all scripts, both TCP and UDP
	"""
	agres_args = '-Pn -sUT -p- --version-intensity 9 -A'
	return nmap_scan(site, ports='', arguments=agres_args)

def nmap_re_scan(site : str, scan: dict):
	"""
	Simple nmap re-scan on the open ports found
	Intensive version, run scripts
	"""
	mdict = scan.items()
	opened = dict(filter(lambda elem: elem[1] != 'filtered' and elem[1] != 'closed', mdict))
	args = ','.join([str(i) for i in opened])
	return nmap_scan(site, arguments='-p' + args + ' --version-intensity 9 -sC -A')

def nmap_evasion(site : str):
	"""
	Nmap scan for WAS/IDS evasion
	Packet fragmentation
	Slow comprehensive
	Defined source port
	"""
	avoid_args = '-f 8 -T0 -g ' + str(random.choice(['80', '443', '53']))
	return nmap_scan(site, arguments=avoid_args)
