#Third party imports

#Python imports
import requests
from bs4 import BeautifulSoup

#Local imports

requests.packages.urllib3.disable_warnings()

def has_text(url : str, word : str):
	"""
	This function checks if word is in url
	Use word as lowercase
	"""
	flag = False
	r = requests.get(url, verify=False, allow_redirects=True)
	if word in r.text:
		flag = True
	return flag

def get_forms(site : str):
	"""
	This function extracts all forms and inputs
	-- Example --
	get_forms('http://wechall.net')
	[['/login', 'post', {'username': '', 'password': ''}]]
	"""
	redirects = []
	page = requests.get(site, verify=False, allow_redirects=True)
	soup = BeautifulSoup(page.content, 'html.parser')
	for tag in soup.find_all('form'):
		fields = tag.findAll('input')
		formdata = dict( (field.get('name'), field.get('value')) for field in fields)
		redirects.append([tag.get('action'), tag.get('method'), formdata])
	return redirects

def is_site(domain : str, port : int):
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

def c_or_t(site : str):
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

def get_urls(site : str):
	"""
	Function to parse subdomains
	from extracted a-href
	by a given url
	"""
	links = []
	page = requests.get(site, verify=False, allow_redirects=True)
	soup = BeautifulSoup(page.content, 'html.parser')
	for tag in soup.find_all('a', href=True):
		if "http" in tag['href']:
			links.append(tag['href'].split("/")[2])
	return links
