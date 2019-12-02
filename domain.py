#Third party imports
import sublist3r

#Python imports

#Local imports
import utils

def get_subs(domain):
	"""
	Uses sublist3r as domain 
	"""
	subdomains = sublist3r.main(target,
							40,
							savefile=False,
							ports=None,
							silent=True,
							verbose=False,
							enable_bruteforce=False,
							engines='google,bing,yahoo,passivedns')
	return subdomains

def brute_force(domain, wordlist):
	brute_list = []
	with open(wordlist, 'r') as f1:
		open_file = f1.read().splitlines()
		for sub in open_file:
			if utils.is_alive(sub + "." + domain):
				brute_list.append(sub + "." + domain)
	return brute_list
