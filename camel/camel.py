camelCase = input("camelCase: ")

n = 0
snake_case = camelCase

for symbol in camelCase:
    if symbol.isupper():
        snake_case = snake_case[:n]+"_"+snake_case[n:]
        n += 1
    n += 1

print("snake_case: ",snake_case.lower())