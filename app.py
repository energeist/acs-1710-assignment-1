
# TODO: Follow the assignment instructions to complete the required routes!
# (And make sure to delete this TODO message when you're done!)

from flask import Flask
import random

app = Flask(__name__)

@app.route('/')
def homepage():
    """Shows a greeting to the user."""
    return 'Are you there, world? It\'s me, Ducky!'

@app.route('/animal/<users_animal>')
def favorite_animal(users_animal):
    """Display a message to the user that changes based on their favorite animal."""
    return f'Wow, {users_animal} is my favorite animal, too!'

@app.route('/dessert/<users_dessert>')
def favorite_dessert(users_dessert):
    """Display a message to the user that changes based on their favorite dessert."""
    return f'How did you know I liked {users_dessert}?'

@app.route('/madlibs/<adjective>/<noun>')
def generate_madlib(adjective, noun):
    """Display a message to the user that changes based on their madlib inputs."""
    return f"That's a real {adjective} {noun} you've got there!"

@app.route('/multiply/<number1>/<number2>')
def multiply_numbers(number1, number2):
    """takes in 2 numbers, multiplies them, and displays the results."""
    if number1.isdigit() and number2.isdigit():
        result = f'{number1} times {number2} is {int(number1) * int(number2)}'
    else:
        result = "Invalid inputs. Please try again by entering 2 numbers!"
    return result

@app.route('/sayntimes/<word>/<n>')
def say_n_times(word, n):
    if word.isalpha() and str(n).isdigit():
        output =  (word + " ") * (int(n)-1) + word
    else:
        output = "Invalid input. Please try again by entering a word and a number!"
    return output

@app.route('/dicegame')
def play_dice_game():
    dice_roll = random.randint(1,6)
    if dice_roll > 3:
        output = f"You rolled a {dice_roll}. You won!"
    else:
        output = f"You rolled a {dice_roll}. You lost!"
    return output

if __name__ == '__main__':
    app.run(debug=True)