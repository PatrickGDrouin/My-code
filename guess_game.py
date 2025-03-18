import random

# Generate a random number between 1 and 10
secret_number = random.randint(1, 10)
turn = 0

while turn < 4:
    turn += 1
    guess = input("Guess the number between 1 and 10: ")

    if not guess.isdigit():
        print("please enter a valide  number!")
        continue
    guess = int(guess)
    if guess < 1 or guess > 10:
        print("Invalid guess. Please enter a number between 1 and 10.")
        continue
    elif guess == secret_number:
        print(f"You guessed it in {turn}! Great job!")
        break
    elif guess > secret_number:
        print("Too high!")
    elif guess < secret_number:
        print("Too low!")
   
    if turn == 3:
        print(f"{turn} turn is too many, you loose!!")
        break

