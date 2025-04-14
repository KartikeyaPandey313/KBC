# KBC (Kaun Banega Crorepati)

## Overview
Welcome to **KBC (Kaun Banega Crorepati)** — a thrilling multi-level quiz game inspired by the iconic television quiz show. This game challenges you with a series of questions organized into 10 levels. With every correct answer, your winnings grow based on the prize for that level. One incorrect answer ends the game and awards you the accumulated winnings.

## Features
- **Multi-Level Gameplay:** Progress through 10 levels with increasing difficulty and prize amounts.
- **Randomized Questions:** Each level selects a random subset of questions, ensuring a unique experience every time.
- **Cumulative Prize:** Your total winnings accumulate with every correct answer.
- **Instant Feedback:** Get immediate feedback on your answers. A wrong answer immediately ends the game, awarding you your current total.

## File Descriptions

### `Program.py`
This script orchestrates the game flow:
- **Imports:** Imports questions from `Question.py`.
- **Winnings Management:** Keeps track of accumulated winnings using a global `total_prize` variable.
- **Question Handling:** Uses the `ask_questions()` function, which displays questions and options, processes user input, and verifies answers.
- **Game Termination:** Stops the game immediately upon any incorrect answer, or advances the player through levels upon correct responses.

### `Questions.py`
This module contains the quiz questions, divided into levels from `Level_1` to `Level_10`. Each question is represented as a list with the following format:
1. **Question Text**
2. **Option 1**
3. **Option 2**
4. **Option 3**
5. **Option 4**
6. **Correct Answer**

## Getting Started

### Prerequisites
- **Python 3.6+** is required.
- Use a command-line interface or terminal to run the scripts.