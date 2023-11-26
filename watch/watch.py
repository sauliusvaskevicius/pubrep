import re
import sys

def main():
    print(parse(input("HTML: ")))

def parse(s):
    match=re.search(r"(?<!<iframe)(?<=src=\")https?://(www.)?youtube.com/embed/\w{11}(?=\">)(?!/iframe>)",s)
    try:
        id=match.group()
    except AttributeError:
        return match
    else:
        return(f"https://youtu.be/{id[-11:]}")


if __name__ == "__main__":
    main()
