import os
import sys
import argparse

import termcolor

import modules.webscrapGet as webscrapGet


parser = argparse.ArgumentParser(
    description="A command that generates ascii art using https://patorjk.com/software/taag/#p=display&f=Graffiti&t=Type%20Something website"
)

parser.add_argument(
    '-s',
    '--style',
    type=str,
    help='The ASCII style you want, to see all styles run the command \'[command] --style-list\''
)

parser.add_argument(
    '-t',
    '--text',
    nargs='*',
    metavar='text',
    default='',
    help='The text you want to convert to ASCII art'
)

parser.add_argument(
    '--style-list',
    action='store_true',
    help='Lists all availible ASCII styles'
)

args = parser.parse_args()


# To verify if we only have '--style-list' as parameters
if args.style_list and not (args.style or args.text):
    print(f"{webscrapGet.getFontList()}\n")
    sys.exit()
elif args.style_list and (args.style or args.text):
    errorText = termcolor.colored(f"[!] Invalid parameters\n", 'red')
    print(errorText)
    sys.exit()


if not webscrapGet.styleExists(args.style):
    if args.asciiStyle == 'stylelist':
        errorText = termcolor.colored("[/!\\] To get the ASCII style list, use the command '[command] stylelist'\n", 'yellow')
        print(errorText)
        sys.exit(1)

    errorText = termcolor.colored(f"[!] The style '{args.style}' doesn't exists\n", 'red')
    print(errorText)
    sys.exit(1)


if not args.text:
    print()
    sys.exit()


try:
    asciiText = webscrapGet.generateAscii(style=args.style, text=" ".join(args.text))
    print(asciiText)
    print()
except KeyboardInterrupt:
    pass


# After getting ASCII art, the file 'geckodriver.log' is created and we don't use it
# so we delete it after finishing, if you want it just delete what's under this comment
if os.path.isfile('geckodriver.log'):
    os.remove('geckodriver.log')
