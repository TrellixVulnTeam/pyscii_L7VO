import os
import sys
import termcolor

import modules.webscrapGet as webscrapGet
import modules.urlGenerator as urlGenerator


if len(sys.argv) >= 2:
    if sys.argv[1] in ['-h', '--help']:
        print("HERE WILL BE HELP DOC\n")
        sys.exit()

if len(sys.argv) <= 3:
    errorText = "[!] ARGS MISSING"
    errorText = termcolor.colored(errorText, 'red')
    print(f"{errorText}\n")
    sys.exit()


asciiStyle = sys.argv[1].strip()

if asciiStyle not in webscrapGet.fontList:
    print(f"[!] POLICE STYLE '{asciiStyle}' IS NOT EXISTING !\n")
    sys.exit()


text = ""
for i in range(2, len(sys.argv)):
    text += f"{sys.argv[i]} "

url = urlGenerator.createUrl(asciiStyle, text)
asciiText = webscrapGet.getASCII(url)

print(f"{asciiText}\n")


if os.path.exists("./geckodriver.log"):
    os.remove("./geckodriver.log")
