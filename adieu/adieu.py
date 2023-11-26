names=[]

def main():
    while True:
        try:
            names.append(input("Name: ").strip())
        except EOFError:
            break

    print("Adieu, adieu, to ",end="")
    num=0
    for name in names:
        if len(names)>2:
            if 0<num<len(names)-1:
                print(", ",end="")
            elif 0<num==len(names)-1:
                print(", and ",end="")
        elif 0<num==len(names)-1:
                print(" and ",end="")
        print(name,end="")
        num+=1
    print("\n")

if __name__ == "__main__":
    main()