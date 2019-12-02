#Third party imports
import sublist3r

#Python imports

#Local imports
import utils

target = "grupoexito.com.co"

def get_subs(domain):
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

#print(get_subs(target))
wordlist = "docs/small.txt"
print(brute_force(target, wordlist))

