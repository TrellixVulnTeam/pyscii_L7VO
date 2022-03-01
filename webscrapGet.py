import requests
import urlGenerator as uG
from bs4 import BeautifulSoup

def getASCII(siteURL : str):
    reponse = requests.get(siteURL, headers={"User-Agent" : "XY"})
    
    if not reponse.ok:
        return f"An error has occured (code error {reponse.status_code})"
    
    soup = BeautifulSoup(reponse.text, features='html.parser')
    
    asciiText = soup.find(class_='fig')
    
    if not asciiText:
        return None

    return asciiText.text
