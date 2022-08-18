#cows and bull game
#in this game you have to guess a four digit number
#if a digit is in the number but not in the right place then you have +1 bull
#if a digit is right and in the right place then you have +1 cow

#generate random 4 digit number (0-9)
def number_generate():
    from random import sample
    from string import digits
    return sample(digits, 4)

#check guess and number
#compute cows and bulls
def check_guess(ans, guess):
    cows = 0
    bulls = 0

    for i in range(len(ans)):
        if ans[i] == guess[i]:
            cows += 1
        elif guess[i] in ans:
            bulls += 1
        
    print("Cows: {}    Bulls: {}".format(cows, bulls))
    return

def you_win(a):
        print("congratualtions, you won in {} attempts".format(a))
        s = input("Would you like to play again? \n").lower()

        if 'y' in s:
            return True
        return False

def game():
    ans = number_generate()
    attempts = 0
    play_again = True
    
    #gameloop
    while play_again == True:
        attempts += 1
        temp = input("Please enter a four digit number: ")
        guess = list(temp)
        check_guess(ans, guess)
        
        if ans == guess:
            play_again = you_win(attempts)
            ans = number_generate()
            attempts = 0
        
    return

if __name__ == "__main__":
    game()