import random

# Generate a random number between 1 and 10
secret_number = random.randint(1, 10)
num_found = False

while num_found == False:
    guess = int(input("Guess the number between 1 and 10: "))

    if guess < 1 or guess > 10:
        print("Invalid guess. Please enter a number between 1 and 10.")
    elif guess == secret_number:
        print("You guessed it! Great job!")
        num_found = True
    elif guess > secret_number:
        print("Too high!")
    elif guess < secret_number:
        print("Too low!")
