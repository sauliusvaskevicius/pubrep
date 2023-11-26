expression = input("Expression: ").split(" ")

match expression[1]:
    case "+":
        print(f"{int(expression[0])+int(expression[2]):.1f}")
    case "-":
        print(f"{int(expression[0])-int(expression[2]):.1f}")
    case "*":
        print(f"{int(expression[0])*int(expression[2]):.1f}")
    case "/":
        print(f"{int(expression[0])/int(expression[2]):.1f}")