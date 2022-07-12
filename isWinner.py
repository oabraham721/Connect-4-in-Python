import sys
from printboard import *

def isWinner(player4, gameboard4):

    printboard(gameboard4)
    if player4 == 'X':
        print('\nCongrats player 1, you\'ve won, Game Over')

    else:
        print('\nCongrats player 2, you\'ve won, Game Over')

    sys.exit()