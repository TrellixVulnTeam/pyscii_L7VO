import urlGenerator as uG
from selenium import webdriver

def getASCII(siteURL : str):
    driverOptions = webdriver.FirefoxOptions()
    driverOptions.headless = True
    
    """try:
        driverOptions.set_headless(headless=True)
    except AttributeError:
        driverOptions.add_argument("--headless")"""
    
    driver = webdriver.Firefox(options=driverOptions)
    
    driver.get(siteURL)
    asciiArt = driver.find_element_by_id("taag_output_text")

    if not asciiArt:
        return ""
        
    return asciiArt.text


a = getASCII("https://patorjk.com/software/taag/#p=display&f=Big&t=Type%20Something")
print(a)
