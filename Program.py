"""
Kaun Banega Crorepati

This script simulates a quiz game with multiple levels. In each level,
a set of questions is randomly selected and presented to the user.
Answering correctly adds the corresponding prize money to the total prize;
a wrong answer ends the game and displays the prize accumulated so far.
"""

# Import required modules and question levels from the "Question" module.
from Questions import (
    Level_1, Level_2, Level_3, Level_4, Level_5,
    Level_6, Level_7, Level_8, Level_9, Level_10
)
import random

# Dictionary mapping each level name to its prize amount.
level_prizes = {
    "Level 1": 1000,
    "Level 2": 5000,
    "Level 3": 10000,
    "Level 4": 25000,
    "Level 5": 50000,
    "Level 6": 100000,
    "Level 7": 500000,
    "Level 8": 1000000,
    "Level 9": 5000000,
    "Level 10": 10000000
}

# Global variable to store the user's total prize money.
total_prize = 0

def ask_questions(level, count, level_name):
    """
    Ask the user a series of questions for a particular quiz level.
    """
    global total_prize

    # Print the header for the current level.
    print(f"\n--- {level_name} ---\n")

    # Randomly select the specified number of questions from the level.
    questions = random.sample(level, count)
    i = 1  # Counter for question numbering

    # Iterate over each selected question.
    for question in questions:
        # Display the question number and text.
        print(f"{i}: {question[0]}")
        # Display each of the four answer options.
        for option in question[1:5]:
            print(f"{option}\n")  # Using an f-string to correctly display the option.
        # Prompt the user for an answer and clean up the input.
        answer = input("Enter your answer: ").strip()
        
        # Check if the user's answer is incorrect (ignoring case).
        if answer.lower() != question[5].lower():
            # Notify the user about the wrong answer and display the correct one.
            print(f"\n❌ Wrong! The correct answer was: {question[5]}\n")
            # Display the total prize money won up to this point.
            print(f"💥 Game Over! You won ₹{total_prize}\n")
            exit()  # Terminate the game.
        else:
            # Confirm the correct answer.
            print("\n✅ Correct!\n")
            i += 1  # Increment the question counter.
            # Add the prize money for the current level to the total.
            total_prize += level_prizes[level_name]

# Begin the quiz by asking questions level-by-level.
ask_questions(Level_1, 2, "Level 1")
ask_questions(Level_2, 2, "Level 2")
ask_questions(Level_3, 2, "Level 3")
ask_questions(Level_4, 2, "Level 4")
ask_questions(Level_5, 2, "Level 5")
ask_questions(Level_6, 1, "Level 6")
ask_questions(Level_7, 1, "Level 7")
ask_questions(Level_8, 1, "Level 8")
ask_questions(Level_9, 1, "Level 9")
ask_questions(Level_10, 1, "Level 10")

# Upon successful completion of all levels, display a congratulatory message.
print(f"🏆 Congratulations! You won ₹{total_prize}")
