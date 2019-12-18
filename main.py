#Third party imports

#Python imports
import sys

#Local imports
import domain
import portscan
import sslcheck

#if len(sys.argv) < 2:
	#print("Usage: python3 {} TARGET".format(sys.argv[0]))

target = "nequi.com"

# Capture subdomains

print("[+] Target: {}".format(target))
print("[+] Getting sub-domains!")
print("\n[+][+] Subdomains!")
subs = domain.get_subs(target)
print(subs)
subs_brute = domain.brute_force(target, "docs/small.txt")
print(subs_brute)
print("\n[+][+] Possible subdomains! (google search)\n")
subs_by_name = domain.find_by_name(target.split(".")[0])
print(subs_by_name)

subsd = []

for item in subs + subs_brute + subs_by_name:
	if target.split(".")[0] in item:
		subsd.append(item)

print("\n[+][+] Subdomains found! Remember to check!\n")
print(subsd)

print("\n[+] Port-Scanning!")
for dom in subsd:
	print("\n[+] Scanning: {}".format(dom))
	#res = portscan.nmap_scan(dom)
	#for key in res:
		#if "filtered" not in res[key] and "closed" not in res[key]:
			#sites.is_site(res[key], key)
