# Simple Calculator with Match Case

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
operation = input("Choose the operation (+, -, *, /): ")

match operation:
    case "+":
        result = num1 + num2
        print(f"The sum of {num1} and {num2} is {result}")
    case "-":
        result = num1 - num2
        print(f"The difference {num1} and {num2} is {result}")
    case "*":
        result = num1 * num2
        print(f"The product of {num1} and {num2} is {result}")
    case "/":
        result = num1 - num2
        if num2 == 0:
            print(f"OPPS {num1} cannot be divided by {num2}")
        else:
            print(f"The division of {num1} by {num2} is {result}")