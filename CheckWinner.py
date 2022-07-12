from isWinner import *

def CheckWinner(gameboard3, player3,  userCol3):

    for i in range (0,3):

        for j in range(0,4):

            if (gameboard3[i][j] == player3) and (gameboard3[i+1][j] == player3) and (gameboard3[i+2][j] == player3) and (gameboard3[i+3][j] == player3):
                isWinner(player3, gameboard3 )

            elif (gameboard3[i][j] == player3) and (gameboard3[i][j+1] == player3) and (gameboard3[i][j+2] == player3) and (gameboard3[i][j+3] == player3):
                isWinner(player3,gameboard3)

            elif (gameboard3[i][j] == player3) and (gameboard3[i + 1][j + 1] == player3) and (gameboard3[i + 2][j + 2] == player3) and (gameboard3[i + 3][j + 3] == player3):
                isWinner(player3, gameboard3)

            elif (gameboard3[i][j] == player3) and (gameboard3[i - 1][j - 1] == player3) and (gameboard3[i - 2][j - 2] == player3) and (gameboard3[i - 3][j - 3] == player3):
                isWinner(player3, gameboard3)


