import random


words_with_hints = [
    # initial words
    ("python", "A popular programming language known for its simplicity."),
    ("computer", "An electronic device that can be programmed to carry out various tasks."),
    ("programming", "The process of designing and building an executable computer application."),
    ("algorithm", "A step-by-step procedure for solving a problem."),
    ("debugging", "The process of finding and fixing errors in code."),
    ("software", "A collection of data or computer instructions that tell the computer how to work."),
    ("function", "A block of organized, reusable code that is used to perform a single action."),
    ("variable", "A named location in memory that stores a value."),
    # Added new words
    ("asynchronous", "A type of programming where tasks do not happen in a linear order."),
    ("recursion", "A function calling itself, commonly used in algorithms."),
    ("polymorphism", "A concept where a function or object can take on multiple forms."),
    ("cryptography", "The art of encoding messages to keep them secure."),
    ("synchronization", "Coordinating actions so they happen at the same time or in a specific order."),
    ("inheritance", "An OOP concept where one class acquires properties of another."),
    ("abstraction", "Hiding complex implementation details and only showing the necessary parts."),
    ("encapsulation", "Bundling of data with methods that operate on the data, or restricting access to some components."),
    ("serialization", "The process of converting an object into a format that can be easily stored or transmitted."),
    ("decentralization", "The transfer of control and decision-making from a centralized entity."),
    ("multithreading", "A technique where multiple threads are used to execute tasks simultaneously."),
    ("artificial", "Something created by humans, often imitating nature."),
    ("intelligence", "The ability to acquire and apply knowledge and skills."),
    ("hexadecimal", "A base-16 number system commonly used in computing."),
    ("transformation", "A process of changing shape, structure, or appearance.")
]

# Function to scramble the word


def scramble_word(word):
    scrambled = list(word)
    random.shuffle(scrambled)
    return ''.join(scrambled)

# Main game function


def play_game():
    # Choose a random word and hint
    word, hint = random.choice(words_with_hints)
    scrambled = scramble_word(word)  # Scramble the chosen word
    attempts = 5  # Number of attempts allowed
    hints_used = False  # Track if the hint has been used

    print("Welcome to Jumble Jungle!")
    print(f"Scrambled word: {scrambled}")
    print("Type 'hint' if you're stuck and need a clue!")

    # Game loop
    while attempts > 0:
        guess = input("Guess the word: ").lower()

        if guess == "hint" and not hints_used:
            print(f"Hint: {hint}")
            hints_used = True
            continue
        elif guess == "hint" and hints_used:
            print("You’ve already used your hint!")
            continue

        if guess == word:
            print("Congratulations! You guessed it right!")
            break
        else:
            attempts -= 1
            print(f"Wrong guess! You have {attempts} attempts left.")

    if attempts == 0:
        print(f"Sorry, you’ve used all your attempts. The correct word was '{word}'.")

# Run the game


play_game()
