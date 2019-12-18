#Third party imports

#Python imports
import sys

#Local imports
import domain
import portscan
import ssl-check

if len(sys.argv) < 2:
	print("Usage: python3 {} TARGET".format(sys.argv[0]))

target = "nequi.com"

# Capture subdomains

print("[+] Target: {}".format(target))
print("[+] Getting sub-domains!")
print("[+][+] Subdomains!")
subs = domain.get_subs(target)
print(subs)
subs_brute = domain.brute_force(target, "docs/small.txt")
print(subs_brute)
print("[+][+] Possible subdomains!")
subs_by_name = domain.find_by_name(target.split(".")[0])
print(subs_by_name)

subsd = []

for item in subs + subs_brute + subs_by_name:
	if target.split(".")[0] in item:
		subsd.append(item)

print(subsd)

"""
print("[+] Port-Scanning!")
print("[+] Port-Scanning!")
for dom in subs + subs_brute:
	portscan.nmap_scan()
"""
#print("[+] Getting sub-domains!")

