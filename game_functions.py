import random

# function to be used by game_1: Guess the Number
def pick_value(poss_values):
    x = random.choice(poss_values)   
    return x

# function to be used in game_2: Higher or Lower
def check_higher_lower(current_val, next_val, user_input):
    user_input = user_input.lower()

    if current_val < next_val and user_input == 'h':
        return True
    if current_val > next_val and user_input == 'l':
        return True

    return False

# function to be used in game_3: Hangman
def process_guess(letter, board, word):
    correct = False
    for i in range(len(word)):
        if word[i] == letter:
            board[i] = letter
            correct = True
    return correct


