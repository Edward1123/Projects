import random

def play():
    user = input('R for Rock, P for Paper and S for Scissors: ')
    computer = random.choice(['R','P','S'])
    if user == computer:
        return "it's a tie!!"

    if is_win(user,computer):
        return 'You won!'

    return "You lost"

def is_win(player,opponent):
    if (player == 'r' and opponent == 's') or (player == 'p' and opponent == 'r') or ([player == 's' and opponent == 'p']):
        return True
    return False


is_win('1','2')

