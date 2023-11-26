
from tabulate import tabulate
from sys import argv
import sys
import csv

def main():
    n=len(argv)
    if n<2:
        sys.exit('Too few command-line arguments')
    elif n>2:
        sys.exit('Too many command-line arguments')
    else:
        try:
            with open(argv[1], "r") as file:
                reader = csv.reader(file)
                data = list(reader)
        except FileNotFoundError:
            sys.exit('File not found')
        else:
            if argv[1][-4:]=='.csv':
                print(tabulate(data, headers="firstrow", tablefmt="grid"))
            else:
                sys.exit('Not a CSV file')

if __name__=="__main__":
    main()
