import random

# ASCII Art for Hangman Stages
STAGES = [
    """
       ------
       |    |
       |    O
       |   /|\\
       |   / \\
       |
    --------
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |   / 
       |
    --------
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |    
       |
    --------
    """,
    """
       ------
       |    |
       |    O
       |   /|
       |    
       |
    --------
    """,
    """
       ------
       |    |
       |    O
       |    |
       |    
       |
    --------
    """,
    """
       ------
       |    |
       |    O
       |    
       |    
       |
    --------
    """,
    """
       ------
       |    |
       |    
       |    
       |    
       |
    --------
    """
]

WORD_LIST = [
    "python", "javascript", "developer", "computer", "algorithm",
    "keyboard", "monitor", "software", "database", "network",
    "internet", "security", "variable", "function", "interface",
    "terminal", "compiler", "debugging", "hardware", "programming"
]

def get_word():
    return random.choice(WORD_LIST).lower()

def play_game():
    word = get_word()
    word_letters = set(word)
    alphabet = set("abcdefghijklmnopqrstuvwxyz")
    used_letters = set()
    lives = 6

    print("\n🎮 Welcome to HANGMAN 🎮")

    while len(word_letters) > 0 and lives > 0:
        # Display current status
        print(STAGES[lives])
        print(f"Lives left: {lives}")
        print("Used letters:", " ".join(sorted(used_letters)))

        # Display word progress
        word_list = [letter if letter in used_letters else "_" for letter in word]
        print("Current word:", " ".join(word_list))

        user_letter = input("\nGuess a letter: ").lower().strip()

        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print(f"✅ Yes! '{user_letter}' is in the word.")
            else:
                lives -= 1
                print(f"❌ No, '{user_letter}' is not in the word.")
        elif user_letter in used_letters:
            print("⚠️  You already guessed that letter. Try again.")
        else:
            print("❌ Invalid character. Please enter a single letter (a-z).")

    # End of game
    if lives == 0:
        print(STAGES[0])
        print(f"\n💀 GAME OVER 💀")
        print(f"The word was: {word}")
    else:
        print(f"\n🎉 YOU WIN! 🎉")
        print(f"The word was: {word}")

if __name__ == "__main__":
    while True:
        play_game()
        play_again = input("\nDo you want to play again? (y/n): ").lower().strip()
        if play_again != 'y':
            print("Thanks for playing! 👋")
            break
