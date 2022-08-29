"""
This program will check a tic tac toe board for a winner
board is preset and will not need to be played before checking
"""

def check_win(l: list):
    
    #checks horizontal
    for i in range(len(l)):
        if (l[i][0] == l[i][1]) and (l[i][0] == l[i][2]):
            return l[i][0]
    
    #checks vertical
    for i in range(len(l)):
        if (l[0][i] == l[1][i]) and (l[0][i] == l[2][i]):     
            print(l)
            print(l[0][i], l[1][i], l[0][i], l[2][i])
            return l[0][i]

    #check diagonal     
    if (((l[0][0] == l[1][1]) and (l[0][0] == l[2][2])) or
        ((l[0][2] == l[1][1]) and (l[0][2] == l[2][0]))):
        return l[1][1]
    
    return 0


if __name__ == "__main__":
    board = [[1, 2, 0], [2, 1, 0], [2, 1, 0]]
    print(check_win(board))