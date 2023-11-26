from sys import argv
import sys

def main():
    n=len(argv)
    count=0
   # print(argv[1][-3:])
    if n<2:
        sys.exit('Too few command-line arguments')
    elif n>2:
        sys.exit('Too many command-line arguments')
    else:
        try:
            with open(argv[1], "r") as file:
                for line in file:
                    if line.strip()!="" and line.strip()[0]!="#":
                        count+=1
        except FileNotFoundError:
            sys.exit('File not found')
        else:
            if argv[1][-3:]=='.py':
                print(count)
            else:
                sys.exit('Not a Python file')


if __name__=="__main__":
    main()
