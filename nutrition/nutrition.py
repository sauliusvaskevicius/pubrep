fruits = {
    "apple":"130",
    "banana":"110",
    "avocado":"50",
    "cantaloupe":"50",
    "grapefruit":"60",
    "honeydew melon":"50",
    "grapes":"90",
    "kiwifruit":"90",
    "lemon":"15",
    "lime":"20",
    "nectarine":"60",
    "orange":"80",
    "peach":"60",
    "pear":"100",
    "pineapple":"50",
    "plums":"70",
    "strawberries":"50",
    "sweet cherries":"100",
    "tangerine":"50",
    "watermelon":"80"
}

def main():
    fruit = input("Item: ").lower()
    if fruit in fruits:
        print(f"Calories: {fruits[fruit]}")


main()