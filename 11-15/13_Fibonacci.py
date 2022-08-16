"""
def fib(n: int):
    if n == 1 or n == 2:
        return (n - 1)  
    
    return fib(n - 1) + fib(n - 2)

in a naive approach to a fibonacci function, we would use a recursive function to call itself until
it reaches the first two numbers of its search, 0 and 1, respectively.

below is an image of how a search tree would look when searching for the 5th number of the fibonacci sequence
the number on the tree shown is the current call that the function is on
the letter 'E' represents the end of the tree and no call is needed this step

                  ______5_____
                 /            \
                4              3
             /     \         /   \
            3       2       2      1
          /   \    / \     / \    / \
         2     1  E   E   E   E  E   E
        / \   / \
       E   E E   E

with memoization, we can eliminate most of the tree by checking if a value has been stored in our memo
in the below tree, we can see this in effect
the letter 'M' will represent where a search ends after being found in our cache


                  ______5_____
                 /            \
                4              M
             /     \    
            3       M   
          /   \    
         2     1     
        / \   / \
       E   E E   E




"""




def fib_memoized(n: int):
    if n in memo:
        return memo[n] #checks if value is already stored and returns its paired value from the dictionary
    
    if n == 1 or n == 2:
        return (n - 1)  #returns the first two values of fib 0 and 1 respectively
    elif n > 2:
        x = fib_memoized(n - 1) + fib_memoized(n - 2)
    memo[n] = x         # stores values of the the fib call if it has not been found yet
    return x            

memo = {}               #initialize dictionarie for value storing 
i = 200
print(fib_memoized(i))