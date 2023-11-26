def main():
    while True:
        input_list = input("Fraction: ").split("/")
        try:
            percentage = int(input_list[0])*100/int((input_list[1]))
        except ( ZeroDivisionError , ValueError):
            continue
        if int(input_list[0]) <= int(input_list[1]) :
                if 0 <= percentage <=1:
                    print("E")
                    break
                elif percentage <99:
                    print(f"{percentage:.0f}%")
                    break
                else:
                    print("F")
                    break



if __name__ == "__main__":
    main()