# a function to find all factors of any number 'n' in O(sqrt(n)) time

def all_factors(n):
    # initialize empty list
    factors = []
    # split factors into two list, factors_left contains all factors of 'n' less or euqal to the sqrt(n)
    factors_left = [x for x in range(1, int(n**0.5) + 1) if n%x == 0]
    # using the factors in factors_left, factors_right will be found
    # for all factors in factors_left, n//x must also be a factor (where x is any integer in factors_left)
    # this will create a list of factors from sqrt(n)+1 to n in reverse order
    factors_right = [n//x for x in factors_left if n//x != x]
    # once both list are made, reverse factors_right, add factors_left and factors_right, then put them into one list
    factors.extend(factors_left + factors_right[::-1])
    return factors

def run_tests():
    test_dict = {
        1: [1],
        2: [1, 2],
        4: [1, 2, 4],
        36: [1, 2, 3, 4, 6, 9, 12, 18, 36]
    }
    count = 0
    for n, factors in test_dict.items():
        count += 1
        assert all_factors(n) == factors, f"Factors of n = {n} should be {factors} not {all_factors(n)}"
        print(f"Test {count} passed")
    print("All tests passed :)")

if __name__ == "__main__":
    run_tests()