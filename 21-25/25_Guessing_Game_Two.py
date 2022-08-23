"""
This exercise is another game but instead of the user guessing the number the program will
tell user to think of a number from 1 to 100
program will guess a number then user will tell it if its too high, too low, or correct
this program will use binary search to find the users number

"""
def instructions():
    print("You will think of a number between 1 and 100 and I will attempt to guess your number.")
    print("after each guess you will enter higher, lower, or correct depending on what I guess.")
    input("Please think of a number and press enter when ready: ")
    return

def generateNumbersList():
    return [i for i in range(1,101)]

def binary_search(low: int, high: int, g: int, nums: list):
    mid = int((low + high) / 2)
    g += 1
    
    print(f"I guess: {nums[mid]}")
    ans = input().lower()
   
    if 'high' in ans:
        return binary_search(mid + 1, high, g, nums)
    elif 'low' in ans:
        return binary_search(low, mid - 1, g, nums)
    else:
        print(f"I guessed your number, {nums[mid]}, in {g} guesses!")


if __name__ == "__main__":
    numbers = generateNumbersList()
    low_index = 0
    high_index = (len(numbers) - 1)
    guesses = 0

    instructions()
    binary_search(low_index, high_index, guesses, numbers)