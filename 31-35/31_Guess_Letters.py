"""
For the second part of the hangman game, the user is now going to get to guess letters

"""
def intro_message():
    print("\nWhen Prompted to, you guess a letter and try to guess the word correctly.")
    print("If you guess incorrectly 6 times you will lose.")
    input("Please press enter when you are ready to play: ")
    return

def get_blank_string(w: str):
    blank_string = ('_' * len(w))
    return blank_string

def get_user_guess():
    guess = input("Please enter your guess: ")
    return guess[0].upper()

def check_letter(g: str, w: str):
    if g in w:
        return True
    return False

def place_letter(letter: str, word: str, board: str, check: bool):
    if check == False:
        return board
    
    board = list(board)
    for i in range(len(board)):
        if word[i] == letter:
            board[i] = letter
    return "".join(board)

def continue_check(a: int, b: str):
    if (a >= 6) or ('_' not in b):
        return False
    return True

def check_win(b: str):
    if '_' not in b:
        return True
    return False

def end_message(win: bool, w: str, a: int):
    if win == False:
        print(f"Sorry, you were not able to guess the word, {w} correctly.")
        return
    
    print(f"Congratulations, you guessed {w} in {a} attempts")
    return

def play_loop():
    word = "APPLE"
    board = get_blank_string(word)
    play = True
    win = False
    wrong_attempts = 0
    attempts = 0
    print(board)
    while play == True:
        attempts += 1
        guess = get_user_guess()
        check = check_letter(guess, word)
        board = place_letter(guess, word, board, check)
        if check == False:
            wrong_attempts += 1
        play = continue_check(wrong_attempts, board)
        print(board)

    win = check_win(board)
    end_message(win, word, attempts)
    return


if __name__ == "__main__":
    intro_message()
    play_loop()