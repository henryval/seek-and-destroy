# -*- coding: utf-8 -*-


import requests

requests.packages.urllib3.disable_warnings()

words = list(open('C:\\2020\CiberExternas\Módulos SnD\directory-list-1.0.txt'))       
codes = [200,301,302,401,403] 
common_ext = ['php','aspx','asp','cgi','pl','txt','html']
def found_dir(wordlist: list, domain: str, ext = common_ext):
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36"}
    
    directories = dict()
    files = []
    for word in wordlist:
    
        if requests.get(domain+"/"+word, verify = False, allow_redirects = False, headers = headers).status_code in codes:
            directories.append(word)
            print("\033[0;32m[-]\033[0m"+domain+"/"+word)
        else:
            print("\033[0;31m[-]\033[0m"+domain+"/"+word)
        if ext:
            for item in ext:
                if requests.get(domain+"/"+word+"."+item, verify = False, allow_redirects = True).status_code in codes:
                    files.append(word)
                    print("\033[0;32m[-]\033[0m"+domain+"/"+word+"."+item)
                else:
                    print("\033[0;31m[-]\033[0m"+domain+"/"+word+"."+item)
        
            

            
  
    return directories,files
        


#def select_wordlist()
words = list(open('C:\\2020\CiberExternas\Módulos SnD\directory-list-1.0.txt'))       

dire, file = found_dir(words,'https://udea.edu.co',[])
        bancolombiainternacional.com/login/init 
   