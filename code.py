import random

# Attractive Hangman 
print("🎮 Welcome to HANGMAN 🎮\n")

words = ["python", "coding", "laptop", "mobile", "hangman", "project"]
word = random.choice(words)
hint = ["_"] * len(word)
chances = 6
guessed = set()

stages = [
    "💀",
    "😵",
    "😨",
    "😟",
    "😐",
    "🙂",
    "😎"
]

while chances > 0:
    print("\n" + "="*30)
    print("Word:  " + " ".join(hint))
    print(f"Chances left: {chances}   {stages[chances]}")
    print("="*30)
    
    guess = input("\nGuess a letter: ").lower().strip()
    
    if len(guess) != 1 or not guess.isalpha():
        print("❌ Please enter only 1 letter!")
        continue
    
    if guess in guessed:
        print("⚠️  Already guessed!")
        continue
    
    guessed.add(guess)
    
    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                hint[i] = guess
        print("✅ Correct!")
    else:
        chances -= 1
        print("❌ Wrong guess!")
    
    if "_" not in hint:
        print("\n🎉 YOU WIN! 🎉")
        print(f"The word was: {word}")
        break

if chances == 0:
    print("\n💀 GAME OVER 💀")
    print(f"The word was: {word}")
