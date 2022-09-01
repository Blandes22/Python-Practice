"""
Full playable game of hangman
"""
from random import randint

def intro_message():
    print("\nWhen Prompted to, you guess a letter and try to guess the word correctly.")
    print("If you guess incorrectly 6 times you will lose.")
    input("Please press enter when you are ready to play: ")
    return

def get_word(s: str):
    with open(s, 'r') as file:
        word_list = file.read().split('\n')
    
    n = randint(0, len(word_list))
    word = word_list[n]
    return word

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

def adjust_attempts(check: bool, guessed_letters: set, guess: str, wrong_attempts: int):
    if (check == False) and (guess not in guessed_letters):
        wrong_attempts -= 1
    return wrong_attempts

def continue_check(a: int, b: str):
    if (a <= 0) or ('_' not in b):
        return False
    return True

def draw_hangman(w: int):
    match w:
        case 6:
            print("\n     _____\n    |     |   \n    |          \n    |          \n    |     \n____|___________")
        case 5:
            print("\n     _____\n    |     |   \n    |     O     \n    |          \n    |     \n____|___________")
        case 4:
            print("\n     _____\n    |     |   \n    |     O     \n    |     |      \n    |     \n____|___________")
        case 3:
            print("\n     _____\n    |     |   \n    |     O     \n    |    /|      \n    |     \n____|___________")
        case 2:
            print("\n     _____\n    |     |   \n    |     O     \n    |    /|\      \n    |     \n____|___________")
        case 1:
            print("\n     _____\n    |     |   \n    |     O     \n    |    /|\      \n    |    /  \n____|___________")
        case 0:
            print("\n     _____\n    |     |   \n    |     O     \n    |    /|\      \n    |    / \ \n____|___________")

def display_board(w: int, b: str, gl: set):
    gl = list(gl)
    
    draw_hangman(w)
    print('\n', b)
    if gl:
        print("\nGuessed letters: ", end='')
    else:
        print("\nGuessed letters: \n", end='')

    for i in range(len(gl)):
        if (i == (len(gl) - 1)):
            print(gl[i])
            break
        print(gl[i], end=', ' )

    print(f"You have {w} wrong guesses left")

def check_win(b: str):
    if '_' not in b:
        return True
    return False

def end_message(win: bool, w: str, a: int):
    if win == False:
        print(f"\nSorry, you were not able to guess the word, {w} correctly.")
        return
    
    print(f"\nCongratulations, you guessed {w} in {a} attempts")
    return

def play_again():
    s = input("Would you like to play again?\nPlease enter yes or no: ")
    if 'y' in s:
        return True
    return False

def game():
    file_name = "sowpods.txt"
    game_loop = True
    
    while game_loop == True:
        word = get_word(file_name).upper()
        board = get_blank_string(word)
        play = True
        win = False
        wrong_attempts = 6
        attempts = 0
        guessed_letters = set()
        
        while play == True:
            display_board(wrong_attempts, board, guessed_letters)            
            attempts += 1
            guess = get_user_guess()
            check = check_letter(guess, word)
            board = place_letter(guess, word, board, check)
            wrong_attempts = adjust_attempts(check, guessed_letters, guess, wrong_attempts)
            guessed_letters.add(guess)
            play = continue_check(wrong_attempts, board)

        draw_hangman(wrong_attempts)
        win = check_win(board)
        end_message(win, word, attempts)
        game_loop = play_again()
    return


if __name__ == "__main__":
    intro_message()
    game()