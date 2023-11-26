from datetime import date
import inflect
import sys



def main():
    print(mintowords(tominutes(input("Date of Birth: "))))


def tominutes(Date1):
    try:
        date1 = date.fromisoformat(Date1)
    except ValueError:
        sys.exit("Invalid date format")
    else:
        date2 =date.today()
        timedelta = date2 - date1
        return(timedelta.days*1440)

def mintowords(min):
    p = inflect.engine()
    return(f"{p.number_to_words(min).capitalize().replace(" and","")} minutes")


if __name__ == "__main__":
    main()
