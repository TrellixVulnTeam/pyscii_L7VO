def createUrl(textStyle : str, text : str):
    return f"https://patorjk.com/software/taag/#p=display&f={textStyle}&t={text}"


if __name__ == "__main__":
    import sys
    import webbrowser

    style = input("Enter text style : ")
    content = input("Enter text : ")
    
    testUrl = createUrl(textStyle=style, text=content)
    
    print(testUrl)
    webbrowser.open(testUrl)
