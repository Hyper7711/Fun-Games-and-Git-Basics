import random

number = random.randint(1, 100)
attempts = 0

while True:
    guess = int(input("Guess a number between 1 and 100: "))
    attempts += 1

    if guess < number:
        print("Too low! Try again.")
    elif guess > number:
        print("Too high! Try again.")
    else:
        print(f"Congratulations! You've guessed the number in {attempts} attempts.")
        break

    if attempts == 5:
        if number % 2 == 0:
            print("HINT: The number is even.")
        else:
            print("HINT: The number is odd.")
