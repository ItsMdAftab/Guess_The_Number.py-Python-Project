
## 🎮 Number Guessing Game

### Description:
This Python-based Number Guessing Game is a simple yet engaging console game where players are challenged to guess a randomly generated number between 1 and 10. The game is designed to test the player's intuition and number-picking strategy. With only four chances to guess the correct number, players must think carefully before each guess. The game provides instant feedback after each guess, letting players know how many attempts they have left.

### How to Play:
1. **Starting the Game**: The game begins by generating a random number between 1 and 10. This number is kept hidden from the player.
2. **Game Rules**:
   - The player is given 4 chances to guess the correct number.
   - After each guess, the game will tell the player if their guess is correct or incorrect.
   - If the guess is incorrect, the player will be informed of the number of remaining chances.
3. **Input Validation**: The game includes input validation to ensure that the player enters a valid number between 1 and 10. If the input is invalid, the game prompts the player to enter a valid number.

### Example of Input and Output:

**Game Start:**
```
Game Condition's:
1.You are give 4 Chances
You have to Guess the Number Correct
```

**First Attempt:**
```
Enter Your Guess Number form (1-10): 5
You Guessed it Wrong
Your Have 3 Chances Left
```

**Second Attempt:**
```
Enter Your Guess Number form (1-10): 7
You Guessed it Wrong
Your Have 2 Chances Left
```

**Third Attempt:**
```
Enter Your Guess Number form (1-10): 3
Congratulation You Guessed It Right
```

**OR**

**Game Over:**
```
Enter Your Guess Number form (1-10): 4
You Guessed it Wrong
Your Have 0 Chances Left
```

### Game Features:
- **Random Number Generation**: The game uses Python’s `random.randint()` function to generate a random number between 1 and 10.
- **Input Validation**: The game ensures that the player's input is a valid number within the specified range.
- **Limited Attempts**: The game provides a limited number of guesses (4) to add a layer of challenge.
- **Immediate Feedback**: After each guess, the game informs the player whether they guessed correctly or how many attempts are left.

### Code Highlights:
- **Random Number Generation**: The game utilizes `random.randint(Starting_value, Ending_value)` to generate a number between 1 and 10.
- **User Input Handling**: The `rollo()` function ensures the player's input is valid, prompting them to re-enter a guess if necessary.
- **Game Loop**: A `for` loop iterates through the player's attempts, checking the guess against the generated number and providing feedback.

This project is an excellent demonstration of basic Python programming concepts, including loops, conditionals, functions, and input validation. It also serves as a fun exercise for beginners looking to build simple games.

---

This description provides a clear and detailed overview of your game, highlighting its functionality, gameplay mechanics, and educational value. It’s suitable for including in the `README.md` file of your GitHub repository.
