
months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

def main():
    while True:
        date = input("Date: ").strip(" ")
        if "/" in date:
            try:
                year=int(date.split("/")[2])
                month=int(date.split("/")[0])
            except ValueError:
                continue
            else:
                if 0 <month< 13:
                    try:
                        day=int(date.split("/")[1])
                    except ValueError:
                        continue
                    else:
                        if 0 <day< 32:
                            break
                        else:
                            continue
                else:
                    continue
        elif "," in date:
            try:
                year=int(date.split(",")[1])
                month=date.split(" ")[0]
            except ValueError:
                continue
            else:
                if month in months:
                    month = months.index(month)+1
                    try:
                        day=int(date.split(" ")[1].split(",")[0])
                    except ValueError:
                        continue
                    else:
                        if 0 <day< 32:
                            break
                        else:
                            continue
                else:
                    continue

    print(f"{year}-{int(month):02d}-{int(day):02d}")


main()