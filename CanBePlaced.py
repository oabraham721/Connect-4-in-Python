from PlaceThePiece import *

def CanBePlaced(gameboard1, player1,  userCol1):

    while gameboard1[5][userCol1] != '*':
        userCol1 =  int(input('That column is full, please pick another column:' ))
        userCol1 -=1

    PlaceThePiece(gameboard1, player1,  userCol1)





