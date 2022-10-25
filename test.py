# def say_n_times(word, n):
#     if word.isalpha() and str(n).isdigit():
#         output =  (word + " ") * (int(n)-1) + word
#     else:
#         output = "Invalid input. Please try again by entering a word and a number!"
#     return output

# print(say_n_times('hello', "6"))

import random

def play_dice_game():
    dice_roll = random.randint(1,6)
    if dice_roll > 3:
        output = f"You rolled a {dice_roll}. You won!"
    else:
        output = f"You rolled a {dice_roll}. You lost!"
    return output

print(play_dice_game())
