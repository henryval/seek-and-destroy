#Third party imports
import sublist3r
import googlesearch

#Python imports
import random

#Local imports
import utils
import sites

useragent = str(random.choice(['Mozilla/5.0 (Windows NT 6.1; Win64;'\
			 'x64; rv:47.0) Gecko/20100101 Firefox/47.0',
			 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '\
			 '(KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36',
			 'Mozilla/5.0 (Linux; Android 7.0; SM-G892A Build/NRD90M; wv) AppleWebKit/537.36 '\
			 '(KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.107 Mobile Safari/537.36',
			 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.75.14 '\
			 '(KHTML, like Gecko) Version/7.0.3 Safari/7046A194A']))

def get_subs(domain):
	"""
	Uses sublist3r to search for subdomains on several engines
	-- Example --
	get_subs('nequi.com') >> www.nequi.com ; api.nequi.com ; etc...
	"""
	subdomains = sublist3r.main(domain,
							40,
							savefile=False,
							ports=None,
							silent=True,
							verbose=False,
							enable_bruteforce=False,
							engines='google,bing,yahoo,passivedns')
	return subdomains

def brute_force(domain, wordlist):
	"""
	Simple subdomain bruteforcing by DNS reverse lookup
	working with a prefix wordlist
	"""
	brute_list = []
	with open(wordlist, 'r') as f1:
		open_file = f1.read().splitlines()
		for sub in open_file:
			if utils.is_alive(sub + "." + domain):
				brute_list.append(sub + "." + domain)
			if utils.is_alive(sub + domain):
				brute_list.append(sub + domain)
	return brute_list

def find_by_name(word : str):
	"""
	Search related subdomains on google given a word
	"""
	doms = []
	for url in googlesearch.search(word,
								   lang='es',
								   pause=3.0,
								   stop=20,
								   user_agent=useragent):
		doms.append(url.split('/')[2])
	return doms
