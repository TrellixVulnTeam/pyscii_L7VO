class String:
    
    def __init__(self, stringContent : str):
        self.stringContent = stringContent
    
    
    def replace(self, toReplace : str, replacing : str):
        return replacing.join(self.stringContent.split(toReplace))
    
    
    def getString(self):
        return self.stringContent


def createUrl(textStyle : str, text : str):
    url = f"https://patorjk.com/software/taag/#p=display&f={textStyle}&t={text}"
    urlModified = String(url)
    urlModified.replace(" ", "%20")
    
    return urlModified.getString()


if __name__ == "__main__":
    import sys
    import webbrowser
    
    style = input("Enter text style : ")
    content = input("Enter text : ")
    
    testUrl = createUrl(textStyle=style, text=content)
    
    print(testUrl)
    webbrowser.open(testUrl)
