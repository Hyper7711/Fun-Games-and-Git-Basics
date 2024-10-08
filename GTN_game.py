import random

number = random.randint(1, 100)
attempts = 0
max_attempts = 10  # Limit the number of attempts to 10

print(f"You have {max_attempts} attempts to guess the correct number.")

while attempts < max_attempts:
    guess = int(input("Guess a number between 1 and 100: "))
    attempts += 1
    
    if guess < number:
        print("Too low!")
    elif guess > number:
        print("Too high!")
    else:
        print(f"Congratulations! You've guessed the number in {attempts} attempts.")
        break
    
    # Provide a hint after 5 wrong guesses
    if attempts == 5:
        if number % 2 == 0:
            print("Hint: The number is even.")
        else:
            print("Hint: The number is odd.")
    
    # If max attempts are reached
    if attempts == max_attempts:
        print(f"Sorry! You've used all {max_attempts} attempts. The correct number was {number}.")
        break
