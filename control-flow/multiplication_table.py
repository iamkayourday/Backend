# Multiplication Table Generator

while True:
    number = int(input("Enter a number to see its multiplication table:."))

    for i in range(1,13):
        result = number * i
        print(f"{number} * {i} = {result}")

# Didn't believe I'll get this right once!!!
# Decided to add a while loop to make it easier to generate another multiplication table