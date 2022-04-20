import requests

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By

import modules.urlGenerator as urlGenerator


def getAscii(siteURL : str):
    """Function to get ASCII art from a link

    Args:
        siteURL (str): the link where the function will take
                        the ASCII art

    Returns:
        str: the ASCII art the program got from the website
    """

    # Setting headless mode
    driverOptions = webdriver.FirefoxOptions()
    driverOptions.headless = True
    
    driver = webdriver.Firefox(options=driverOptions)
    driver.get(siteURL)
    
    # Getting the ASCII art
    asciiArt = driver.find_element(By.ID, "taag_output_text")

    # If no ASCII art has been got, the program will return an empty
    # string
    if not asciiArt:
        return ""
        
    # Returns ASCII art without HTML balises
    return asciiArt.text


def getFontList() -> str():
    """Function that returns all ASCII styles availible

    Returns:
        str: The ASCII styles list
    """

    with open('./modules/textPolices.txt', 'r') as f:
        fontList = f.read()
    
    return fontList


def styleExists(style : str) -> bool():
    fontList = getFontList().split('\n')

    return style in fontList


def generateAscii(style : str, text : str) -> str():
    """Function that use previouses to generate ASCII art

    Args:
        style (str): The style you want to generate you ASCII art
        text (str): The text you want to convert to ASCII art
    
    Returns:
        asciiArt (str): The ASCII art generated
    """

    link = urlGenerator.createUrl(textStyle=style, text=text)
    asciiArt = getAscii(link)

    return asciiArt


if __name__ == "__main__":
    asciiArt = getAscii("https://patorjk.com/software/taag/#p=display&f=Big&t=PyScii")
    print(asciiArt)
