import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    if len(ip.split('.'))==4:
        for n in ip.split('.'):
            if int(n) in range(256):
                continue
            else:
                return False
        return True
    else:
        return False
if __name__ == "__main__":
    main()
