# Given a string, find the rank of the string amongst its permutations sorted lexicographically.
# For string 'bac' the rank among permtations would be 3
# First rank would be "abc" then "acb" and finally "bac" would be the third

# factorial used in calculating current rank of permutation
from math import factorial 

def find_rank(s):
    # tracks rank of permutation
    rank = 0
    # tracks current position of 's' that needs to be found
    position = 0
    # used for calculating rank
    size = len(s)
    # all elements in of s sorted into alphabetical order
    # used for tracking which elements are still needed
    elements = sorted(list(s))
    while True:
        # base case
        if len(elements) == 0:
            return rank
        # psuedo-recursive case
        for count, val in enumerate(elements, 1):
            if val == s[position]:
                # if size is less than 1, add one as there is only one possible rank to choose from
                # otherwise, take x*(n-1)! where x is the number of elements that came before the current
                # and n is the is the (inclusive) remaining number of elements needed to be found
                # x*(n-1)! will result in the number of permutations not needed to search for
                # therefore, giving a rank to the current permutation.
                x = count - 1
                rank += x * factorial(size-1) if (size > 1) else 1
                # update remaining variables
                position += 1
                size -= 1
                # remove the value used from the list of characters
                #  preventing the characters from being used twice
                elements.remove(val)
                break

def main():
    test_dict = {
        'bac' : 3,
        'acb' : 2,
        'view': 15,
        'asdfe' : 20,
        'table' : 98
    }
    # run tests
    count = 0
    for key, val in test_dict.items():
        count += 1
        assert find_rank(key) == val, f"key '{key}' returned {find_rank(key)} instead of {val}"
        print(f'Test {count} passed')
    print('All tests passed')

if __name__ == "__main__":
    main()