"""
This exercise will combine three of the previous exercises to create a fully playable two player tic tac toe game

"""

def draw_board(b: list):
    print("")
    for i in range(len(b)):
        for j in range(len(b[i])):
            if (j < (len(b[i]) - 1)):
                print(f" {b[i][j]} |", end = '')
            else:
                print(f" {b[i][j]} ")
        if (i < (len(b) - 1)):        
            print("-----------")
    return

def check_win(l: list):
    
    #checks horizontal and vertical
    for i in range(len(l)):
        if ((l[i][0] == l[i][1]) and (l[i][0] == l[i][2]) or         #horizontal
            (l[0][i] == l[1][i]) and (l[0][i] == l[2][i])):          #vertical
            return True

    #check diagonal     
    if (((l[0][0] == l[1][1]) and (l[0][0] == l[2][2])) or
        ((l[0][2] == l[1][1]) and (l[0][2] == l[2][0]))):
        return True
    
    return False

def change_player(pl: str):
    if pl == 'X':
        pl = 'O'
    else:
        pl = 'X'
    
    return pl

def place_marker(n: int, bd: list, mkr: str):    
    row = ((n - 1) // 3)
    col = ((n - 1) % 3)

    bd[row][col] = mkr
    return bd

def game():
    play_again = True
    p1_wins = 0
    p2_wins = 0
    
    while play_again == True:
        player = 'O'
        win = False
        board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        draw_board(board)
        turn = 0
        
        while (win == False) and (turn < 9):
            available = False
            turn += 1
            player = change_player(player)
            print(f"\nIt is now {player}'s turn") 
            
            while not available:
                spot = int(input("Please enter an available number on the board to continue: "))
                
                if ((spot < 1) or (spot > 9) or not (any(spot in row for row in board))):
                    print("Sorry, that is not a valid spot number")
                else:
                    available = True
            board == place_marker(spot, board, player)
            win = check_win(board)
            draw_board(board)
        
        if win:
            print(f"\n{player}'s win!\n")
        else:
            print("\nIts a draw!\n")
        
        ans = input("Would you like to play again?\nPlease enter yes or no: ").lower()
        if 'n' in ans:
            play_again = False
        
        if player == 'X' and win:
            p1_wins += 1
        elif win:
            p2_wins += 1
    
    print(f"\nWins:\nX's: {p1_wins}\nO's: {p2_wins}")

    return

if __name__ == "__main__":
    game()