import random

while True:
    try:
        lvl=int(input("Level: "))
    except ValueError:
        continue
    else:
        if lvl not in range(1,100+1):
            continue
        else:
            break
        
x=int(random.choice(range(lvl)))

while True:
    try:
        guess = int(input("Guess: "))
    except ValueError:
        continue
    else:
        if 100<guess or guess<1:
            continue
        else:
            if guess == x:
                print("Just right!")
                break
            else:
                if guess < x:
                    print("Too small!")
                else:
                    print("Too large!")


