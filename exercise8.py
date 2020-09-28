"""
Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input),
compare them, print out a message of congratulations to the winner, and ask if the players
want to start a new game)

Remember the rules:

    Rock beats scissors
    Scissors beats paper
    Paper beats rock
"""
def is_valid(string):
    if string in game_dict.keys():
        return True
    else:
        return False

def compare(first, second):
    first_value = game_dict.get(first)
    second_value = game_dict.get(second)
    dif = first_value - second_value

    if dif in [-1, 2]:
        return f"{first} beats {second}!"
    elif dif in [-2, 1]:
        return f"{second} beats {first}!"
    else:
        return "We have a tie!"

def reset_game():
    if input("Do you want to play again? (Y/N): ").upper() == 'Y':
        return True
    else:
        return False

game_on = True
game_dict = {'ROCK': 1, 'SCISSORS': 2, 'PAPER': 3}

while game_on:
    print("This is a game of Rock-Paper-Scissors!")
    first = input("Please, type in the first choice: ").upper()
    while not is_valid(first):
        print(f"{first} is not a valid choice for this game")
        first = input("Please, type in a valid choice: ").upper()
    second = input("Now, let's get to know the second one: ").upper()
    while not is_valid(second):
        print(f"{second} is not a valid choice for this game")
        second = input("Please, type in a valid choice: ").upper()

    print(compare(first, second))
    game_on = reset_game()

