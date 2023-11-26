import pyfiglet
import sys
import random

fonts="slant","3-d", "doh","letters","bubble","rectangles","alphabet"

def main():

    if len(sys.argv)>1:
        if len(sys.argv)==3 and sys.argv[1] in ("-f","--font") and sys.argv[2] in fonts:
            text=input("Input: ")
            ascii_banner = pyfiglet.figlet_format(text,font=str(sys.argv[2]))
        else:
            sys.exit("||||||||||||||||||||||||||||||||||||\nInvalid Command-line Arguments Error")
    else:
        text=input("Input: ")
        ascii_banner = pyfiglet.figlet_format(text,font=random.choice(fonts))

    print("Output: ")
    print(ascii_banner)

if __name__ == "__main__":
    main()