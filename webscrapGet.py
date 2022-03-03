import urlGenerator as uG
from selenium import webdriver

def getASCII(siteURL : str):
    driverOptions = webdriver.FirefoxOptions()
    driverOptions.headless = True
    
    driver = webdriver.Firefox(options=driverOptions)
    driver.get(siteURL)
    
    asciiArt = driver.find_element_by_id("taag_output_text")

    if not asciiArt:
        return ""
        
    return asciiArt.text


if __name__ == "__main__":
    asciiArt = getASCII("https://patorjk.com/software/taag/#p=display&f=Big&t=PyScii")
    print(asciiArt)
