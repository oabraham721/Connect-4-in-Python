from CheckWinner import *

def PlaceThePiece(gameboard2, player2,  userCol2):
    for x in range (0,6):
        if gameboard2[x][userCol2] == '*':
            gameboard2[x][userCol2] = player2
            break

    CheckWinner(gameboard2, player2,  userCol2)

