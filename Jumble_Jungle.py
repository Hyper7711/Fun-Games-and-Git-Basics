import random

# List of words to choose from
words = ["python", "computer", "programming", "algorithm", "debugging",
         "software", "function", "variable"]

# Function to scramble the word

def scramble_word(word):
    scrambled = list(word)
    random.shuffle(scrambled)
    return ''.join(scrambled)

# Main game function

def play_game():
    word = random.choice(words)  # Select a random word from the list
    scrambled = scramble_word(word)  # Scramble the selected word
    attempts = 3  # Number of attempts allowed

    print("Welcome to the Word Scramble Game!")
    print(f"Here is the scrambled word: {scrambled}")

    # Game loop
    while attempts > 0:
        guess = input("Guess the word: ")

        if guess.lower() == word:
            print("Congratulations! You guessed it right!")
            break
        else:
            attempts -= 1
            print(f"Wrong guess! You have {attempts} attempts left.")

    if attempts == 0:
        print(f"Sorry, you've used all your attempts.
              The correct word was '{word}'.")

# Run the game

play_game()
