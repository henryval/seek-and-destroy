#Third party imports
import sublist3r

#Python imports
import requests
from bs4 import BeautifulSoup

#Local imports

requests.packages.urllib3.disable_warnings()

def get_forms(site):
	"""
	This function extracts all forms and inputs
	-- Example --
	get_forms('http://wechall.net')
	[['/login', 'post', {'username': '', 'password': ''}]]
	"""
	page = requests.get(site, verify=False, allow_redirects=True)
	soup = BeautifulSoup(page.content, 'html.parser')
	redirects = []
	for tag in soup.find_all('form'):
		fields = tag.findAll('input')
		formdata = dict( (field.get('name'), field.get('value')) for field in fields)
		redirects.append([tag.get('action'), tag.get('method'), formdata])
	return redirects

def is_site(domain, port):
	"""
	Function to determine if domain has
	an http service on determined port
	-- Example --
	is_site('scanme.nmap.org', 22) => False
	is_site('tls-v1-2.badssl.com', 1012) => True
	"""
	has_site = False
	if port == 443:
		url = "https://" + domain
	else:
		url = "http://" + domain + ":" + str(port)
	try:
		r = requests.get(url, verify=False, allow_redirects=True)
		has_site = True
	except:
		pass
	return has_site

def c_or_t(site):
	"""
	Function to determine if site is
	content-like or transactional
	-- Example --
	c_or_t('http://wechall.net') => T
	"""
	site_type = "C"
	if get_forms(site):
		site_type = "T"
	return site_type


