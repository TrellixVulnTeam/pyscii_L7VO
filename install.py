import os
import sys
import time
import shutil
import distro
import tarfile
import requests

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




def downloadFile(link : str, output : str):
    response = requests.get(link, allow_redirects=True)
    
    with open(output, 'wb') as f:
        fileContent = response.content
        f.write(fileContent)


def isGeckoInstalled():
    try:
        driverOptions = webdriver.FirefoxOptions()
        driverOptions.headless = True
        
        driver = webdriver.Firefox(options=driverOptions)
        return True
    except selenium.common.exceptions.WebDriverException:
        return False


def untarFile(file : str):
    with tarfile.open(file, 'r') as tarFile:
        tarFile.extractall('/usr/local/bin')
    


if isGeckoInstalled():
    print("Geckodriver is already installed on your system, exiting...")
    os.remove('geckodriver.log')
    sys.exit()


linuxDistributionName = distro.name()


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
        os.mkdir('Geckodriver')
        
        downloadFile(link, f"./Geckodriver/{filename}")
        untarFile(f'./Geckodriver/{filename}')
        break
else:
    time.sleep(2)
    errorText = termcolor.colored("[/!\\] Your OS has not been recognized, please see manually_install_geckodriver.txt\n", 'red')
    print(errorText)
    sys.exit()


try:
    shutil.rmtree('./Geckodriver')
    os.remove('geckodriver.log')
except FileNotFoundError:
    pass


print("\n[+] Geckodriver has successfully been installed on your system\n")
