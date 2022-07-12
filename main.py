import random

from printboard import *
from playerPiece import *
from CheckWinner import *

board = [ ['*','*','*','*','*','*','*'],
        ['*','*','*','*','*','*','*'],
        ['*','*','*','*','*','*','*'],
        ['*','*','*','*','*','*','*'],
        ['*','*','*','*','*','*','*'],
        ['*','*','*','*','*','*','*']]

move = random.randint(0,1)
p1 = 'X'
p2 = 'O'

while True:

    printboard(board)

    if (move == 1):
        playerPiece(board, p1 )
        move = 0

    elif (move == 0):
        playerPiece(board, p2)
        move = 1

