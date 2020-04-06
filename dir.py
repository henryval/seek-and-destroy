# -*- coding: utf-8 -*-


import requests
import random

 
requests.packages.urllib3.disable_warnings()

words = list(open('C:\\2020\CiberExternas\SnD\seek-and-destroy\directory-list-1.0.txt'))       
codes = [200,301,302,401,403] 
common_ext = ['php','aspx','asp','cgi','pl','txt','html']

#Usage found_dir(wordlist, url, [optional] ext)

#The function return a dictionary with the directories and files found and their response codes

def found_dir(wordlist: list, domain: str, ext = common_ext):
    
    results = dict()
    for word in wordlist:
        useragent = random.choice(['Mozilla/5.0 (Windows NT 6.1; Win64;'\
                 'x64; rv:47.0) Gecko/20100101 Firefox/47.0',
                 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '\
                 '(KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36',
                 'Mozilla/5.0 (Linux; Android 7.0; SM-G892A Build/NRD90M; wv) AppleWebKit/537.36 '\
                 '(KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.107 Mobile Safari/537.36',
                 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.75.14 '\
                 '(KHTML, like Gecko) Version/7.0.3 Safari/7046A194A'])
      
        headers=[]
        r = requests.get(domain+"/"+word, verify = False, allow_redirects = False, headers = headers.append(useragent))
        if r.status_code in codes:
            
            results[word]=r.status_code
            print("\033[0;32m[+]\033[0m"+domain+"/"+word)
        else:
            print("\033[0;31m[-]\033[0m"+domain+"/"+word)
        if ext:
            for item in ext:
                if requests.get(domain+"/"+word+"."+item, verify = False, allow_redirects = True).status_code in codes:
                    results[word+"."+ext]=r.status_code
                    print("\033[0;32m[-]\033[0m"+domain+"/"+word+"."+item)
                else:
                    print("\033[0;31m[-]\033[0m"+domain+"/"+word+"."+item)
            
                
    
                
      
    return results
        



final = found_dir(words[:100],'https://udea.edu.co',[])
