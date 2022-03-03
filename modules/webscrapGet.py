from selenium import webdriver

with open('./modules/textPolices.txt', 'r') as f:
    fontList = f.read()


def getASCII(siteURL : str):
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
    asciiArt = driver.find_element_by_id("taag_output_text")

    # If no ASCII art has been got, the program will return an empty
    # string
    if not asciiArt:
        return ""
        
    # Returns ASCII art without HTML balises
    return asciiArt.text


if __name__ == "__main__":
    asciiArt = getASCII("https://patorjk.com/software/taag/#p=display&f=Big&t=PyScii")
    print(asciiArt)
