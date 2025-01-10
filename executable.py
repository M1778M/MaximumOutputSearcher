import os, colorama,sys
from bs4 import BeautifulSoup
import random
import time
from evpn import ExpressVpnApi
import fake_useragent
import urllib3
import requests
import hashlib
import wget
from pathlib import Path
import platform
import zipfile
import base64
import argparse
import urllib.parse
from threading import Thread
from bs4 import UnicodeDammit
import subprocess


os.system('title MaximumOutputSearcher by Infinity')
debug = True

FOUND_URL = 0
LINKS = []
ERRORS = 0

print("MADE WITH LOVE :)")
def print_error(text):
    print(f"{colorama.Fore.RED}M.O.S ERROR: "+text+colorama.Fore.RESET)

artch = 64 if '64' in platform.machine() else 32
if artch == 32:
    python_download = "https://raw.githubusercontent.com/M1778M/ToolsVerify/master/Pyvers/Python3912_32bit.zip"
    py3912_file = Path(str(Path.home().parent)+Path().home().root+Path().home().name+Path().home().root+'AppData\\Local\\temp_data1778\\Python3912_32bit\\python.exe')
    py3912_folder = Path(str(Path.home().parent)+Path().home().root+Path().home().name+Path().home().root+'AppData\\Local\\temp_data1778\\Python3912_32bit')
else:
    py3912_file = Path(str(Path.home().parent)+Path().home().root+Path().home().name+Path().home().root+'AppData\\Local\\temp_data1778\\Python3912\\python.exe')
    python_download = "https://raw.githubusercontent.com/M1778M/ToolsVerify/master/Pyvers/Python3912.zip"
    py3912_folder = Path(str(Path.home().parent)+Path().home().root+Path().home().name+Path().home().root+'AppData\\Local\\temp_data1778\\Python3912')

temp_folder=Path(str(Path.home().parent)+Path().home().root+Path().home().name+Path().home().root+'AppData\\Local\\temp_data1778\\')

if not temp_folder.exists():
    temp_folder.mkdir()

if not py3912_folder.exists() or not py3912_file.exists():
    print('Downloading python...')
    try:
        download_=wget.download(python_download,str(temp_folder.absolute())+'\\downloaded_py.zip')
    except:
        print_error("Failed to download python. Please try again and check your internet connection.")
        sys.exit(1)
    print('Python download completed.')
    print('Installing python...(extracting files)')
    try:
        with zipfile.ZipFile(str(Path(download_).absolute()),'r') as zip_ref:zip_ref.extractall(str(temp_folder.absolute()))
    except:
        print_error("Failed to install python. try again or create an issue in this github page: https://github.com/M1778M/ToolsVerify/issues")
        sys.exit(1)
os.system('cls')
print("CHECKING PYTHON PACKAGES")
if os.system(str(py3912_file.absolute()) + ' -m pip') != 0:
    get_pip = "https://raw.githubusercontent.com/M1778M/ToolsVerify/master/Pyvers/get-pip.py"
    print("Downloading pip...")
    pip_file = wget.download(get_pip,str(temp_folder.absolute())+'\\get_pip.py')
    print('Pip download completed.')
    print("Installing pip...")
    if os.system(str(py3912_file.absolute())+f' "{pip_file}"') != 0:
        print('Installing pip failed!')
        print('Please try again or create an issue in this github page: https://github.com/M1778M/ToolsVerify/issues')
        time.sleep(5)
        pip_install = 0
    else:
        pip_install = 1
os.system("CLS")
requirements = "requests"
st = os.system(str(py3912_file.absolute()) + ' -m pip install '+ requirements)
if st!=0:
    if pip_install:
        print_error("Could not install required packages, please try again or create an issue in this github page: https://github.com/M1778M/ToolsVerify/issues")
        sys.exit(st)
    print_error("Could not install pip, please try again or create an issue in this github page: https://github.com/M1778M/ToolsVerify/issues")
    sys.exit(st)
os.system("CLS")


os.system('cls')

infinity=True

urllib3.PoolManager()

b=colorama.Back.BLUE
bb=colorama.Back.CYAN
r=colorama.Back.RESET
rr=colorama.Fore.RESET
br=colorama.Fore.LIGHTCYAN_EX
ra=colorama.Style.RESET_ALL
blue = f"""{colorama.Style.BRIGHT}
                   {bb}*#################*{r}
               {bb}*####{r}{b}@@@@@            {r}{bb}####*{r}{br}~~~~~~~~~~~~{rr}
           {bb}*####{r}{b}@@@@@@@ Made by          {r}{bb}####*{r}{br}--------------{rr}
        {bb}*####{r}{b}@@@@@@@@   {colorama.Fore.BLACK}M1778{rr}               {r}{bb}####*{r}{br}~~~~~~~~~~~~~~~~~{rr}
      {bb}*####{r}{b}@@@@@@@@                           {r}{bb}####*{r}{br}-------------------------------{rr}
    {bb}*####{r}{b}@@@@@@@@@                              {r}{bb}####*{r}{br}~~~~~~~~~~~~~~~~~~~~~~~{rr}
   {bb}*####{r}{b}@@@@@@@@    {colorama.Fore.GREEN}t.me/TheSyntax3{rr}              {r}{bb}####*{r}{br}-------------------------------{rr}
  {bb}*####{r}{b}@@@@@@@@                                   {r}{bb}####*{r}{br}~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~{rr}
 {bb}*####{r}{b}@@@@@@@@                                     {r}{bb}####*{r}{br}----------------------{rr}
 {bb}*####{r}{b}@@@@@@@@   {colorama.Fore.MAGENTA}M{rr}.     {colorama.Fore.GREEN}O{rr}.    {colorama.Fore.LIGHTRED_EX}S{rr}                    {r}{bb}####*{r}{br}~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~{rr}
 {bb}*####{r}{b}@@@@@@@@   {colorama.Fore.LIGHTCYAN_EX}MaximumOutputSearcher{rr}             {r}{bb}####*{r}{br}----------------------------------------{rr}
 {bb}*####{r}{b}@@@@@@@@       M.O.S Tool                    {r}{bb}####*{r}{br}~~~~~~~~~~~~~~~~~~~~~~~~~{rr}
 {bb}*####{r}{b}@@@@@@@@                                     {r}{bb}####*{r}{br}--------------{rr}
  {bb}*####{r}{b}@@@@@@@@     {colorama.Fore.RED}ExpressVPN-Edition{rr}            {r}{bb}####*{r}{br}~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~{rr}
   {bb}*####{r}{b}@@@@@@@@                                 {r}{bb}####*{r}{br}-----------------------{rr}
    {bb}*####{r}{b}@@@@@@@@                               {r}{bb}####*{r}{br}~~~~~~~~~~~~~~~~~{rr}
      {bb}*####{r}{b}@@@@@@@@    {colorama.Fore.MAGENTA}Launcher:{rr}                {r}{bb}####*{r}{br}-----------{rr}
        {bb}*###{r}{b}@@@@@@@@         {colorama.Style.DIM}Infinity{ra}{b}        {r}{bb}####*{r}{br}~~~~~~~~~~~~~~~~~{rr}
           {bb}*####{r}{b}@@@@@@                   {r}{bb}####*{r}{br}-------{rr}
               {bb}*####{r}{b}@@@@               {r}{bb}####*{r}{br}~~~~~~~~~~~~{rr}
                    {bb}*#################*{ra}"""

colorama.init()

def relaunch():
    if getattr(sys, 'frozen', False):
        os.system(sys.executable)
        sys.exit()
    elif __file__:
        sys.exit()

def banner():
    os.system('cls')
    renge = reversed(range(20))
    for s in renge:
        
        time.sleep(0.001)
        sp=s
        for i in blue.split("\n"):
            print((sp*' ')+i)
        time.sleep(0.001)
        os.system('cls')
    print(blue)
    print(f"{colorama.Fore.YELLOW}This tool is used to mass search dorks. The overall speed of process depends on your PC/RDP CPU, Network Speed and other possible factors.{rr}")

banner()
def get_random_ua():
    return fake_useragent.UserAgent().random


def express_change_location(sleep):
    while True:
        time.sleep(sleep)
        _vpn.connect(random.choice(VPN_LOCATIONS)['id'])

restricted_websites = [
    "google.com", "youtube.com", "facebook.com", "baidu.com", "wikipedia.org",
    "qq.com", "amazon.com", "yahoo.com", "vk.com", "apple.com",
    "netflix.com", "whatsapp.com", "microsoft.com", "instagram.com", "twitter.com",
    "ebay.com", "mail.ru", "yandex.ru", "amazon.co.jp", "360.cn", "jd.com",
    "weibo.com", "espn.com", "reddit.com", "telegram.org", "twitch.tv",
    "bbc.com", "pinterest.com", "pornhub.com", "xhamster.com", "dropbox.com",
    "zoom.us", "cnn.com", "imgur.com", "blogspot.com", "wordpress.com",
    "tiktok.com", "office.com", "playstation.com", "mediafire.com", "stackoverflow.com",
    "imgur.com", "alibaba.com", "dailymotion.com", "mozilla.org", "imgur.com", 
    "fandom.com", "bbc.co.uk", "adobe.com", "t.co", "theguardian.com",
    "chase.com", "bankofamerica.com", "wellsfargo.com", "nintendoswitch.com", "uol.com.br",
    "disneyplus.com", "apple.com.cn",  
    "cnbc.com", "dropbox.com",'en.wikipedia.org']

__r = restricted_websites.copy()
for i in __r:
    restricted_websites.append('www.'+i)

def get_domain_name(url):
  try:
    parsed_url = urllib.parse.urlparse(url)
    if parsed_url.netloc:
      return parsed_url.netloc.split(":")[0]
    else:
      return None
  except ValueError:
    return None

def google_search_page(dork,page):
    page1 = search(0,dork).data
    page1 = UnicodeDammit(page1, ["windows-1252"], smart_quotes_to="html").unicode_markup
    soup = BeautifulSoup(page1,'html.parser',from_encoding="iso-8859-1")
    links = []
    for i in get_google_links(page1):
        links.append(i)
    nexts = []
    current_page = 2
    pgs=soup.find_all(attrs={'class':'fl'})
    for j in pgs:
        if current_page == page:
            break
        if j.get('aria-label') is not None:
            if str(current_page) in j.get('aria-label'):
                nexts.append(j.get('href'))
                current_page+=1
    for i in nexts:
        for link in get_google_links(search(0,dork,i)):
            links.append(link)
    return links

def pgoogle_search_page(dork,page,proxy):

    page1 = psearch(0,dork,proxy)
    if page1 == False:
        return False
    page1=page1.data
    page1 = UnicodeDammit(page1, ["windows-1252"], smart_quotes_to="html").unicode_markup
    soup = BeautifulSoup(page1,'html.parser',from_encoding="iso-8859-1")
    links = []
    for i in get_google_links(page1):
        links.append(i)
    nexts = []
    current_page = 2
    pgs=soup.find_all(attrs={'class':'fl'})
    for j in pgs:
        if current_page == page:
            break
        if j.get('aria-label') is not None:
            if str(current_page) in j.get('aria-label'):
                nexts.append(j.get('href'))
                current_page+=1
    for i in nexts:
        for link in get_google_links(psearch(0,dork,proxy,i)):
            links.append(link)
    return links

def search(which,dork,nex=None):
    if which == 0:
        which = "https://www.google.com/search?client=firefox-b-d&q="
    else:
        which = "https://www.google.com/search?client=firefox-b-d&q="
    if nex is not None:
        which = "https://www.google.com"+nex
    headers = {
"User-Agent": get_random_ua(),
"Accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/png,image/svg+xml,*/*;q=0.8",
"Accept-Encoding": "gzip, deflate, br, zstd",
"Accept-Language": "en-US,en;q=0.5",
"Connection": "keep-alive"}
    return urllib3.request("GET",which+dork,headers=headers)

def psearch(which,dork,proxy,nex=None):
    if which == 0:
        which = "https://www.google.com/search?client=firefox-b-d&q="
    else:
        which = "https://www.google.com/search?client=firefox-b-d&q="
    if nex is not None:
        which = "https://www.google.com"+nex
    headers = {
"User-Agent": get_random_ua(),
"Accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/png,image/svg+xml,*/*;q=0.8",
"Accept-Encoding": "gzip, deflate, br, zstd",
"Accept-Language": "en-US,en;q=0.5",
"Connection": "keep-alive"}
    try:
        return urllib3.ProxyManager('http://'+proxy,timeout=urllib3.Timeout(connect=15,read=None)).request("GET",which+dork,headers=headers)
    except Exception as err:
        print(err)
        return False

def get_google_links(data):
    soup = BeautifulSoup(UnicodeDammit(data, ["windows-1252"], smart_quotes_to="html").unicode_markup,'html.parser',from_encoding="iso-8859-1")
    links = []
    if soup.find('div',id='search') == None:
        return []
    for a in soup.find('div',id='search').find_all('a'):
        try:
            href = a['href']
            assert type(href) == str

            if href.startswith('http') and 'www.google.com' not in href:
                if not get_domain_name(href.strip()) in restricted_websites:
                    links.append(href.strip())
        except:
            continue
    return list(set(links))

def search_dork(dorks,page):
    global FOUND_URL,ERRORS,LINKS
    for dork in dorks:
        try:
            for link in google_search_page(dork,page):
                LINKS.append(link)
                FOUND_URL += 1
        except:
            ERRORS += 1
def psearch_dork(dorks,page,proxylist):
    global FOUND_URL,ERRORS,LINKS
    max_len = len(proxylist)
    current = 0
    for dork in dorks:
        try:
            for link in pgoogle_search_page(dork,page,proxylist[current]):
                if current+1 > max_len:
                    current = 0
                else:
                    current+=1
                LINKS.append(link)
                FOUND_URL += 1
        except:
            ERRORS += 1

def auto_file_saver():
    global LINKS
    time.sleep(5)
    while True:
        with open(str(Path().home().joinpath('Desktop').joinpath('MaximumOutput.txt').absolute()),'w') as file:
                out = ''
                for link in LINKS:
                    out+=str(link)+'\n'
                file.write(out)
                file.close()
        time.sleep(5)

def str_to_int_possible(st):
    try:
        int(st)
        return True
    except:
        return False

if not infinity:
    print_error("This program is not launched through infinity launcher.")
    x = input("Do you still wanna continue?")
    if "n" in x.lower():
        ...

mode = 0
print(f"{colorama.Fore.GREEN}[INFO]:{colorama.Fore.YELLOW} The output file is saved in desktop/MaximumOutput.txt{colorama.Fore.RESET}")
def ask_with_options(description:str,ask_:str,options:dict):
    print(description)
    # {1:"Valid",2:"Invalid"}
    for i in options.keys():
        print(str(i)+": "+options[i])
    return input(ask_)
try:
    ask_mode = ask_with_options(f"{colorama.Fore.LIGHTGREEN_EX}Choose mode:{rr}",f"{colorama.Fore.GREEN}Please choose M.O.S mode: {colorama.Fore.CYAN}",{1:"Terminal/CMD mode",2:"GUI mode"})
    print(end=rr)
    if ask_mode == '':
        ask_mode = 1
    mode = int(ask_mode)
    print(f"{colorama.Back.WHITE}{colorama.Fore.BLACK}Selected [{mode}]{ra}")
except:
    print_error("There was an error caused by user's input, please try again.")
    print("RESTARTING...")
    time.sleep(1)
    relaunch()

if mode == 1:
    method = ask_with_options(f"{colorama.Fore.LIGHTGREEN_EX}Choose method: {rr}",f"{colorama.Fore.CYAN}Please choose the searching method: {colorama.Fore.GREEN}",{1:f"{colorama.Fore.RED}ExpressVPN (VIP/Proxyless){rr}",2:"Proxylist",3:"Normal/Proxyless (Not Recommended)"})
    print(end=rr)
    if method == '':
        method = 1
    try:
        method = int(method)
        print(f"{colorama.Back.WHITE}{colorama.Fore.BLACK}Selected [{method}]{ra}")
    except:
        print_error("There was an error caused by user's input, please try again.")
        print("RESTARTING...")
        time.sleep(1)
        relaunch()
    while True:
        file_path = input(colorama.Fore.GREEN+"Please enter the file path: "+colorama.Fore.BLUE)
        print(end=colorama.Fore.RESET)
        if not Path(file_path).exists() or not Path(file_path).is_file():
            print_error("File doesn't exists, please enter the path correctly.")
        else:
            break
    dorks=open(file_path,'r').readlines()
    while True:
        page = input(colorama.Fore.GREEN+"Please enter the number of pages you want to search for each dork (default->5): "+colorama.Fore.BLUE)
        if page == '':
            page = 5
            break

        elif str_to_int_possible(page):
            page = int(page)
            break
        print_error("Page number entered is incorrect, please enter a number or hit enter if you want the default number to be used.")
    if method == 1:
        print("Connecting to ExpressVPN api (this method requires expressvpn)\nNote: please run expressvpn and be sure that it works just fine.")
        try:
            _vpn = ExpressVpnApi()
            VPN_LOCATIONS = _vpn.locations
        except:
            print_error("Could not connect to Expressvpn, please install express vpn and login to it, this method requires ExpressVPN.")
        
        while True:
            vpn_timeout = input(colorama.Fore.GREEN+"Please enter a number in seconds for changing vpn location after that time (default->30): "+colorama.Fore.BLUE)
            if vpn_timeout == '':
                vpn_timeout = 30
                break

            elif str_to_int_possible(vpn_timeout):
                vpn_timeout = int(vpn_timeout)
                break
            print_error("vpn timein number entered is incorrect, please enter a number or hit enter if you want the default number to be used.")
        dork_count_for_process = round(len(dorks)/8 - 1)
        c = 1
        first = True
        for i in range(1,9):
            IN_DORK = dorks[0 if first else (c-1)*dork_count_for_process:c*dork_count_for_process]
            Thread(target=search_dork,args=(IN_DORK,page)).start()
            c+=1
            first = False
        last_dork = dorks[c*dork_count_for_process:]
        Thread(target=search_dork,args=(last_dork,page)).start()
        os.system('cls')
        banner()
        Thread(target=auto_file_saver).start()
        Thread(target=express_change_location,args=(vpn_timeout,)).start()
        ti = 0
        while True:
            try:
                vp=_vpn.get_status()['data']['info']['selected_location']['name']
            except:
                vp="Unavailable"
            os.system('cls')
            print(f"Links : [{FOUND_URL}]\tErrors : [{ERRORS}]\tvpn location [{vp}]\ttime: [{ti}]",end='\r')
            time.sleep(1)
            ti+=1
    elif method == 2:
        while True:
            proxy_path = input(colorama.Fore.GREEN+"Please enter the proxylist file path: "+colorama.Fore.BLUE)
            print(end=colorama.Fore.RESET)
            if not Path(file_path).exists() or not Path(file_path).is_file():
                print_error("File doesn't exists, please enter the path correctly.")
            else:
                break
        
        proxylist=open(proxy_path,'r').readlines()
        if len(proxylist) < 10:
            print_error("Proxylist too short...")
            print_error("Please use more proxies in your proxylist. NOTE: you can use proxyscrape.com to get free proxies.")
            relaunch()
        if 'http' in proxylist[1] or 'https' in proxylist[1] or 'socks' in proxylist[1] or not str_to_int_possible(proxylist[1][0]):
            for i in range(len(proxylist)):
                for j in proxylist[i]:
                    if str_to_int_possible(proxylist[i][j]):
                        break
                proxylist[i] = proxylist[i][j:]
        
        dork_count_for_process = round(len(dorks)/8 - 1)
        c = 1
        first = True
        for i in range(1,9):
            IN_DORK = dorks[0 if first else (c-1)*dork_count_for_process:c*dork_count_for_process]
            Thread(target=psearch_dork,args=(IN_DORK,page,proxylist)).start()
            c+=1
            first = False
        last_dork = dorks[c*dork_count_for_process:]
        Thread(target=psearch_dork,args=(last_dork,page,proxylist)).start()
        os.system('cls')
        banner()
        Thread(target=auto_file_saver).start()
        ti = 0
        while True:
            print(f"Links : [{FOUND_URL}]\tErrors : [{ERRORS}]\tProxies: [{len(proxylist)}]\ttime: [{ti}]",end='\r')
            time.sleep(1)
            ti+=1
    elif method == 3:
        ...
    else:
        print_error("Selected method is not available or doesn't exists.")
        print("RESTARTING...")
        relaunch()
elif mode == 2:
    print_error("Sorry but GUI mode is not available for now wait for the updates...")
    print("RESTARTING...")
    relaunch()
else:
    print_error("Selected mode is not available or doesn't exists.")
    print("RESTARTING...")
    relaunch()
