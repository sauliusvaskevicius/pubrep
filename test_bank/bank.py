def main():
    greeting = input("Greeting: ")
    print(f"${value(greeting)}")



def value(greeting):
    if "hello" ==greeting.lower().replace(" ","")[0:5] : return 10
    elif "h"==greeting.lower().replace(" ","")[0] : return 20
    else: return 100



if __name__ == "__main__":
    main()






