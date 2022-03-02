import sys
import colorama
import webbrowser
import webscrapGet
import urlGenerator


# SI LA POLICE N'EXISTE PAS CA SERA 'Graffiti' PAR DEFAUT !!!


if len(sys.argv) == 1:
    print("IL MANQUE DES ARGUMENTS\n")
    sys.exit()


if sys.argv[1] in ['-h', '--help']:
    print("HERE WILL BE HELP DOC")
    sys.exit()


if len(sys.argv) < 3:
    # put color on text
    print("PAS BONS ARGUMENTS")


asciiStyle = sys.argv[1]

text = ""
for i in range(2, len(sys.argv)):
    text += f"{sys.argv[i]} "


url = urlGenerator.createUrl(asciiStyle, text)
asciiText = webscrapGet.getASCII(url)

print(f"{asciiText}")
