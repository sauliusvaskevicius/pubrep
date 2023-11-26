from sys import argv
import sys
import csv

students=[]

def main():

    n=len(argv)

    if n<3:
        sys.exit('Too few command-line arguments')
    elif n>3:
        sys.exit('Too many command-line arguments')
    else:

        if argv[1][-4:]=='.csv':

                try:
                    with open(argv[1], "r") as file1:
                        reader = csv.DictReader(file1)
                        for row in reader:
                            students.append(row)
                except FileNotFoundError:
                    sys.exit('File not found')
                else:
                    with open(argv[2], "w") as file2:
                        writer = csv.DictWriter(file2,fieldnames=["first","last","house"])
                        writer.writeheader()
                        for student in students:
                            last,first=student["name"].split(",")
                            writer.writerow({"first":first.strip(),"last":last.strip(),"house":student["house"].strip()})
        else:
            sys.exit('Not a CSV file')

if __name__=="__main__":
    main()
