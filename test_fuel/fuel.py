def main():
    while True:
        fraction=input('Fraction: ')
        try:
            prcnt=convert(fraction)
        except (ZeroDivisionError , ValueError,IndexError) as e:
            continue
        else:
            print(gauge(prcnt))
            break

def convert(fractionstr):
    input_list = fractionstr.split("/")
    percentage = round(int(input_list[0])*100/int((input_list[1])))
    if int(input_list[0]) <= int(input_list[1]):
        return percentage
    else:
        raise ValueError("more than 100%")

def gauge(percentage):
    if 0 <= percentage <=1:
        return("E")
    elif percentage <99:
        return(f"{percentage:.0f}%")
    else:
        return("F")


if __name__ == "__main__":
    main()