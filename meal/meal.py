def main():
    timeT = convert(input("What time is it? "))
    if 7<= timeT <=8 :
        print("breakfast time")
    if 12<= timeT <=13 :
        print("lunch time")
    if 18<= timeT <=19 :
        print("dinner time")



def convert(time):
    if "p.m." in time :
        return float(time.split(" ")[0].split(":")[0])+float(time.split(" ")[0].split(":")[1])/60+12
    else:
        return float(time.split(" ")[0].split(":")[0])+float(time.split(" ")[0].split(":")[1])/60


if __name__ == "__main__":
    main()