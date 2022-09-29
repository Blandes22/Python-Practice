# This program utilizes recursion to find all possible integers of length 'string_size' 
# containing only numbers "0 to 'nums_used'-1" (if nums_used equals 4, [0, 1, 2, 3] will be used)
class Solution():
    def __init__(self, string_size, nums_used):
        # generates empty list of size 'string_size' to store permutations
        self.arr = [None for i in range(string_size)]
        # generates list of all integers that will be used in permustations
        self.k = range(0, nums_used)
        # list for storage of permutations
        self.storage = []
    
    def strings_of_n_size(self, n: int):
        # n is used to track how many digits left need to be changed, for example:
        # in list [None, None, None] 3 digits will need to changed still, so 'n' is 3
        # in list [None, 2, 1] 1 digit needs to be changed so 'n' is 1. 
        # base case, if 'n' is 0 (all digits have values, print )
        if (n == 0):
            # list is reversed only for aesthetic purposes:
            # (list will be ordered '00, 01, 02... n' instead of '00, 10, 20... n') 
            self.storage.append(''.join(self.arr[::-1]))
        # recursive case
        else:
        # arr will start as [None, None, None] -> [None, None, 0] -> [None, 0, 0] -> [0, 0, 0] -> [1, 0, 0]...
        # once arr[0] reaches the last number of 'k' it will move back to arr[1] and cycle through again:
        # [9, 0, 0] -> [None, 1, 0] -> [0, 1, 0]... and so forth until until every iteration has been made and stored
            for i in range(len(self.k)):
                # n is the decimal place, so n-1 is the index of the decimal place
                self.arr[n-1] = str(i)
                # call function again with n-1 to get to the next decimal place
                self.strings_of_n_size(n-1)

def main():
    string_size = 3
    nums_used = 4
    sol = Solution(string_size, nums_used)
    sol.strings_of_n_size(string_size)
    print(sol.storage)

if __name__ == "__main__":
    main()