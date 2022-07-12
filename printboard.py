
columns = [1,2,3,4,5,6,7]

def printboard(board1):

    for i in range (5,-1,-1):
        print('\n',end ="\t\t")

        for j in range(7):
            print(board1[i][j],end ="  ")

    print('\n\t  ',*columns,sep='  ')



