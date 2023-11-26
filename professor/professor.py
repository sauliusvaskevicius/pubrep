import random


def main():
    l=get_level()
    score=0
    for _ in range(10):
        error=0
        x=generate_integer(l)
        y=generate_integer(l)
        z=x+y
        while True:
            try:
                guess=int(input(f"{x} + {y} ="))
            except ValueError:
                continue
            else:
                if z==guess:
                    score+=1
                    break
                else:
                    error+=1
                    if error==3:
                        print(f"{x} + {y} = {z}")
                        break
                    else:
                        print(f"EEE")
                        continue
    print(f"Score: {score}")



def get_level():
    while True:
        try:
            lvl=int(input("Level: "))
        except ValueError:
            continue
        else:
            if lvl not in range(1,3+1):
                continue
            else:
                return lvl


def generate_integer(level):
    if level==1:
        return random.choice(range(1*10**(level-1)-1,10**level))
    else:
        return random.choice(range(1*10**(level-1),10**level))


if __name__ == "__main__":
    main()