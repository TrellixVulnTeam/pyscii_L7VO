import os
import sys
import time
import requests
import subprocess

import termcolor
import selenium
from selenium import webdriver


CURRENT_VERSION = 'v0.31.0'
LINK = f"https://github.com/mozilla/geckodriver/releases/download/{CURRENT_VERSION}"



print("""
██╗███╗   ██╗███████╗████████╗ █████╗ ██╗     ██╗        ██████╗ ██╗   ██╗
██║████╗  ██║██╔════╝╚══██╔══╝██╔══██╗██║     ██║        ██╔══██╗╚██╗ ██╔╝
██║██╔██╗ ██║███████╗   ██║   ███████║██║     ██║        ██████╔╝ ╚████╔╝ 
██║██║╚██╗██║╚════██║   ██║   ██╔══██║██║     ██║        ██╔═══╝   ╚██╔╝  
██║██║ ╚████║███████║   ██║   ██║  ██║███████╗███████╗██╗██║        ██║   
╚═╝╚═╝  ╚═══╝╚══════╝   ╚═╝   ╚═╝  ╚═╝╚══════╝╚══════╝╚═╝╚═╝        ╚═╝   
""")



def isGeckoInstalled():
    try:
        driver = webdriver.Firefox()
        return True
    except selenium.common.exceptions.WebDriverException:
        return False
    


if isGeckoInstalled():
    print("Geckodriver is already installed on your system, exiting...")
    sys.exit()


linuxDistributionName = subprocess.check_output(['uname', '-r']).decode()


geckodriverLink = {
    "Debian" : (f'{LINK}/geckodriver-{CURRENT_VERSION}-linux64.tar.gz', f'geckodriver-{CURRENT_VERSION}-linux64.tar.gz'),
    "Kali linux" : (f'{LINK}/geckodriver-{CURRENT_VERSION}-linux64.tar.gz', f'geckodriver-{CURRENT_VERSION}-linux64.tar.gz'),
    "Parrot OS" : (f'{LINK}/geckodriver-{CURRENT_VERSION}-linux64.tar.gz', f'geckodriver-{CURRENT_VERSION}-linux64.tar.gz'),
    "Ubuntu" : (f'{LINK}/geckodriver-{CURRENT_VERSION}-linux64.tar.gz', f'geckodriver-{CURRENT_VERSION}-linux64.tar.gz'),
    "Arch" : (f'{LINK}/geckodriver-{CURRENT_VERSION}-linux64.tar.gz', f'geckodriver-{CURRENT_VERSION}-linux64.tar.gz'),
    "Manjaro" : (f'{LINK}/geckodriver-{CURRENT_VERSION}-linux64.tar.gz', f'geckodriver-{CURRENT_VERSION}-linux64.tar.gz'),
    "Endeavour" : (f'{LINK}/geckodriver-{CURRENT_VERSION}-linux64.tar.gz', f'geckodriver-{CURRENT_VERSION}-linux64.tar.gz'),
    "Garuda" :(f'{LINK}/geckodriver-{CURRENT_VERSION}-linux64.tar.gz', f'geckodriver-{CURRENT_VERSION}-linux64.tar.gz'),

    "Mac OS" : ('{LINK}/geckodriver-{CURRENT_VERSION}-macos.tar.gz', f'geckodriver-{CURRENT_VERSION}-macos.tar.gz'),
}


for distro in geckodriverLink.keys():
    link, filename = geckodriverLink[distro]
    
    if distro.lower() in linuxDistributionName.lower():
        subprocess.run(['wget', link])
        subprocess.run(['sudo', 'tar', '-C', '/usr/local/bin/', '-xf', filename])
        break
else:
    time.sleep(2)
    errorText = termcolor.colored("[/!\\] Your OS has not been recognized, please see manually_install_geckodriver.txt\n", 'red')
    print(errorText)
    sys.exit()


try:
    os.remove('geckodriver.log')
    os.remove(filename)
except FileNotFoundError:
    pass


print("\n[+] Geckodriver has successfully been installed on your system\n")
