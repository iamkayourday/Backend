import random

secret_number = random.randint(1, 10)
print("Welcome to the Number Guessing Game!")
guess = int(input("Guess a number btw 1-10 "))
num_of_guess = 0
match guess: 
    case guess if guess == secret_number: 
        print("Congratulations, you guessed it!") 
    case  guess if  guess > secret_number:
        print("Oops, your guess is a bit high. Try again!") 
    case  guess if  guess < secret_number:
        print("Nope, your guess is a bit low. Give it another shot!")
    