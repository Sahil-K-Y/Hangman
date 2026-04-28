# 🎮 Hangman Game - Classic CLI Edition

[![Python Version](https://img.shields.io/badge/python-3.x-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A sleek, classic CLI-based Hangman game built with Python. Test your vocabulary and try to guess the hidden word before the hangman is complete!

---

## 🚀 Features

- **🎨 Classic ASCII Art**: Visual representation of the hangman stages that updates dynamically.
- **📚 Tech-Focused Word List**: Over 20+ programming and technology-related words to challenge your knowledge.
- **🛡️ Robust Input Handling**: Prevents duplicate guesses and handles invalid characters gracefully.
- **🔄 Instant Replay**: Play as many rounds as you want without exiting the program.
- **📊 Real-time Stats**: Displays lives remaining, letters used, and current word progress.

---

## 🕹️ Game Rules

1. The computer selects a random word from the tech-focused list.
2. You start with **6 lives**.
3. For every incorrect guess, the hangman moves one step closer to completion, and you lose a life.
4. Guessing a correct letter reveals its position(s) in the word.
5. You win if you guess all the letters in the word correctly.
6. You lose if you run out of lives before the word is complete.

---

## 🛠️ Technologies Used

- **Python 3**: The engine behind the game logic and CLI interaction.
- **Random Module**: Used for generating random word selections.

---

## 📂 Project Structure

```text
Hangman/
├── code.py      # Main game logic and entry point
└── README.md    # Project documentation
```

---

## 📖 How to Play

### Prerequisites
- Python 3.x installed on your system.

### Installation & Execution
1. **Clone the repository**:
   ```bash
   git clone https://github.com/Sahil-K-Y/Hangman.git
   ```
2. **Navigate to the directory**:
   ```bash
   cd Hangman
   ```
3. **Run the game**:
   ```bash
   python code.py
   ```

---

## 📸 Preview

```text
       ------
       |    |
       |    O
       |   /|\
       |    
       |
    --------
Lives left: 3
Used letters: a e i s t
Current word: p y t h _ n
```

---

## 🤝 Contributing

Contributions are welcome! If you have suggestions for new features or word lists, feel free to:
1. Fork the Project.
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`).
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`).
4. Push to the Branch (`git push origin feature/AmazingFeature`).
5. Open a Pull Request.

---

## 📄 License

Distributed under the MIT License. See `LICENSE` (if available) for more information.

---

## 👤 Author

**Sahil Kumar**
- GitHub: [@Sahil-K-Y](https://github.com/Sahil-K-Y)

---
*If you like this project, feel free to give it a ⭐!*
