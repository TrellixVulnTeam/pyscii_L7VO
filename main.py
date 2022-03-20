import os
import sys
import argparse

import termcolor

import modules.webscrapGet as webscrapGet


parser = argparse.ArgumentParser(
    description="A command that generates ascii art using https://patorjk.com/software/taag/#p=display&f=Graffiti&t=Type%20Something website"
)

parser.add_argument(
    'asciiStyle',
    metavar='style',
    type=str,
    help='The ASCII style you want, to see all styles run the command \'[command] stylelist\''
)

parser.add_argument(
    'asciiText',
    nargs='*',
    metavar='text',
    default='',
    help='The text you want to convert to ASCII art'
)

args = parser.parse_args()


# To get the ASCII style list, use the command '[command] stylelist'
if args.asciiStyle == 'stylelist' and not args.asciiText:
    print(f"{webscrapGet.getFontList()}\n")
    sys.exit()


if not webscrapGet.styleExists(args.asciiStyle):
    if args.asciiStyle == 'stylelist':
        errorText = termcolor.colored("[/!\\] To get the ASCII style list, use the command '[command] stylelist'\n", 'yellow')
        print(errorText)
        sys.exit(1)

    errorText = termcolor.colored(f"[!] The style '{args.asciiStyle}' doesn't exists\n", 'red')
    print(errorText)
    sys.exit(1)


if not args.asciiText:
    print()
    sys.exit()


asciiText = webscrapGet.generateAscii(style=args.asciiStyle, text=" ".join(args.asciiText))
print(asciiText)
print()


# After getting ASCII art, the file 'geckodriver.log' is created and we don't use it
# so we delete it after finishing, if you want it just delete what's under this comment
if os.path.isfile('geckodriver.log'):
    os.remove('geckodriver.log')
