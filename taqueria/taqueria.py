menu = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

def main():
    price=0
    total=0
    while True:
        try:
            price = menu[input("Item: ").title()]
        except KeyError:
            continue
        except EOFError:
            print(f"Total: ${total:.2f}")
            break
        else:

            total =total+float(price)
            print(f"Total: ${total:.2f}")








if __name__ == "__main__":
    main()
