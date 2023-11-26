import re

def main():
    print(count(input("Text: ")))

def count(s):
    #LOOKING FOR A MATCH
    if matches:=re.findall(r'(\W|^)um(\W|$)',s.lower()):
        A=len(matches)
    else: A=0

    return A


if __name__ == "__main__":
    main()
