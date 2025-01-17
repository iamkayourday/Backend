# Drawing Patterns with Nested Loops

pattern = 0
while pattern <= 0:
    pattern = int(input("Enter the pattern of the pattern: "))
    if pattern <= 0:
        print("Please enter a positive integer.")
        pattern = 0

row = 0
while row < pattern:
    for _ in range(pattern):
        print("*", end="")
    print()
    row += 1

    # Meta did this