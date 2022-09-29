# The Goldbach conjecture states "every even counting number greater than 2 is equal to the sum of two prime numbers."
# This program intends to mimic this and find the smallest set of primes that add up to any even number 'n'
# due to the brute force solution of the problem being very expensive, two shortcuts are used:
# Sieve of Eratosthenes solution to find all the primes of a number and a hash map to find the pair
class Solution:
    def prime_sum(self, n):
        primes = self.sieves_primes_below_n(n)
        for n_key in primes.values():
            # the n_key is paired to the number that will add to 'n'
            # use hash map to check if n_key has a prime counterpart
            try:
                return [primes[n_key], n_key]
            except KeyError:
                continue

    def sieves_primes_below_n(self, n):
        # generate a list of booleans the size of n all set to True.
        # This list will be used to track all ints below n and by the end, only indices marked as True will be prime
        is_prime = [True for i in range(n)]
        # set base cases (0, 1) to False as they are not prime
        is_prime[0] = is_prime[1] = False
        # iterate through a range of all number from 2 (bases cases 0 and 1 are set) to sqrt(n)
        # numbers higher than sqrt(n) will not need to be checked in the first loop because sqrt(n) * sqrt(n) is the
        # largest factor pair and all factors will be check 
        for i in range(2, int(n**0.5) + 1):
            if is_prime[i]:
                # mark all numbers that are multiples of 'i' as False due to them not being prime (having a factor of 'i')
                for j in range(i**2, n-1, i):
                    is_prime[j] = False
        # return all indices marked as True in an ordered list
        return {i : n-i for i in range(n-1) if is_prime[i]}

def main():
    sol = Solution()
    # run tests
    test_dict = {
        4: [2, 2],
        6: [3, 3],
        10: [3, 7],
        20: [3, 17],
        22: [3, 19]
    }
    count = 0
    for key, val in test_dict.items():
        count += 1
        assert sol.prime_sum(key) == val, f"Prime sum for {key} returned {sol.prime_sum(key)} instead of {val}"
        print(f"Test {count}: passed")
    print('All tests passed')

if __name__ == "__main__":
    main()