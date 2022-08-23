"""
This exercise requires a game board to be printed to the screen
the game board is X by X where X is determined by the user

"""

def get_board_size():
    x = 0
    while x < 1 or x > 25:
        x = int(input("Please enter a number in range 1 to 25 to determine the size of the game board: "))
        if x < 1 or x > 26:
            print(f"sorry {x} is not in range")
    
    return x

def create_board(i: int):
    i = 1
    while (i <= size):
        print(" ---" * size) 
        print("|   " * (size + 1))
        i += 1
    print(" ---" * size)
    return


if __name__ == "__main__":
    size = get_board_size()
    create_board(size)