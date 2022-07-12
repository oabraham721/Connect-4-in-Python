from CanBePlaced import *

columnInp = [1,2,3,4,5,6,7]

def playerPiece (gameboard, player):


    if player == 'X':
        while True:
            try:
                userCol = int(input('\n\nPlayer 1 please enter the column where you\'d like to place the chip: '))
                break
            except ValueError:
                print('\nPlease enter a NUMBER, not CHARACTER(S)',end ="  ")

    else:
        while True:
            try:
                userCol = int(input('\n\nPlayer 2 please enter the column where you\'d like to place the chip: '))
                break
            except ValueError:
                print('\nPlease enter a NUMBER, not CHARACTER(S)',end ="  ")

    while userCol not in columnInp :
        userCol = int(input('\nThe input was out of range, please try again: '))

    CanBePlaced(gameboard, player,  userCol-1)

