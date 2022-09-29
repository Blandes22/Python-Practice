# Python class that will take two integers and add them together without using arithmetic
# randint used for test cases
from random import randint

class Solution:
    def add_numbers(self, a, b):
        a, b = self.convert_nums_to_bin(a, b)

        # added will be used to save answer after the two strings are added
        added = ''  
        # carry will be used if there is an overflow in the binary spot and carry the overflow to the the next digit
        carry = 0
        # iterate through the range of both ints (len(a) = len(b)) backwards 
        # because the first digits to be added will be on the right of the string
        for i in range(len(a)-1, -1, -1):
            # new variable 'result' will store the result of adding each place from both strings
            result = carry
            result += 1 if a[i] == '1' else 0
            result += + 1 if b[i] == '1' else 0
            # check whether or not next number in the added string will be 0 or 1 and add it to the front of the string
            added = ('1' if result % 2 == 1 else '0') + added
            # check if there is any overflow and add overflow to 'carry'
            carry = 1 if result > 1 else 0
		
        # after for loop is executed, check if there is any overflow from the last two digits added
        if carry > 0:
            added = '1' + added
        
        # (int(added, 2)) takes the binary number and converts it to decimal
        return (int(added, 2))

    def convert_nums_to_bin(self, a, b):
        # ints 'a' and 'b' both translated to binarys in the "0bxxxx" format
        a = bin(a).replace('0b', '')
        b = bin(b).replace('0b', '') #.replace() remove the "0b" from the string
		# find which binary string is longer in length to fill strings
        size = max(len(a), len(b))
        # fill both strings with 0's left of the string to get strings to equal length 
        b = '0' * (size - len(b)) + b
        a = '0' * (size - len(a)) + a
        return a, b

def main():
    sol = Solution()
    run_tests(sol)
    print("All tests have passed :)")

def run_tests(sol: Solution):
    # generate dictionary of random ints (x, y) which will be added using the sol.add_numbers() function
    # pythons built in addition operator will be used to test if each test is true
    test_dict = {randint(0, 1_000_000_000) : randint(0, 1_000_000_000) for i in range(500)}
    count = 0
    for x, y in test_dict.items():
        count += 1
        assert sol.add_numbers(x, y) == x + y , f"result equals {sol.add_numbers(x, y)}, should have been {x + y} for {x} + {y}"
        print(f"Test {count}: passed")

if __name__ == "__main__":
    main()