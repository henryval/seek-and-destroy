import sublist3r

subdomains = sublist3r.main('grupoexito.com.co',40,savefile=False,ports=None,silent=False,verbose=True,enable_bruteforce=True,engines='google,bing,yahoo,passivedns')
print(subdomains)



